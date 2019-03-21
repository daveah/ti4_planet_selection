#!/usr/bin/env python
import random
from _ti4_load_planets import _ti4_load_planets
from _ti4_load_configs import _ti4_load_configs
from _ti4_get_formatter import _ti4_get_formatter

# Reference data - immutable
num_iterations = 100

# Load tile information
tiles = _ti4_load_planets()

# Load configurations
allocations = _ti4_load_configs()

# Extract reference data into working vectors
# All tile names
names = [tile[0] for tile in tiles]
# Resources for each tile
resource = [tile[1] for tile in tiles]
# Influence for each tile
influence = [tile[2] for tile in tiles]
# Indices of wormhole systems
wormhole = [ii for ii in range(0, len(tiles)) if tiles[ii][3]]
# Indices of anomaly systems (red border)
anomaly = [ii for ii in range(0, len(tiles)) if tiles[ii][4]]
# Indices of blank systems
blank = [ii for ii in range(0, len(tiles)) if tiles[ii][5]]


# Hold a set of results
class Results:
    # Number of players
    num_players = None
    # Vector of amount of resources for each player
    player_resource = None
    # Vector of amount of inflience for each player
    player_influence = None
    # Vector of planets indices for each player
    player_planets = None
    # Number of tiles to be allocated to each player
    num_tiles = 0
    # Tiles that are considered "shared"
    #   Includes Mecatol Rex,
    #   one tile to be placed next to Mecatol Rex in 5 player game and
    #   unused tiles
    shared_planets = None
    # Vector of whether a tile has been allocated
    #   set to zero for unallocated, one for allocated
    used = None

    def __init__(self, config):
        self.num_players = None
        self.player_resource = None
        self.player_influence = None
        self.player_planets = None
        self.shared_planets = []
        self.used = [0 for ii in range(0, len(tiles))]
        self._allocate_planet(0, -1)
        self._configure(config)

    # Allocate a planet to a given player (-1 for shared)
    def _allocate_planet(self, planet_num, player_num):
        if self.used[planet_num] == 1:
            raise RuntimeError("Attempt to allocate already used tile: {}".
                               format(planet_num))
        self.used[planet_num] = 1
        if player_num >= 0:
            if len(self.player_planets[player_num]) >= self.num_tiles:
                raise RuntimeError("Too many tiles allocated to player: {}".
                                   format(player_num))
            self.player_planets[player_num].append(planet_num)
            self.player_resource[player_num] = (
                self.player_resource[player_num] - resource[planet_num])
            self.player_influence[player_num] = (
                self.player_influence[player_num] - influence[planet_num])
        else:
            self.shared_planets.append(planet_num)

    # Allocate remaining tiles to players
    # Return true on success, false on failure
    def allocate(self):
        for player in range(0, self.num_players):
            if not self._fill_player(player, self._get_unused_vector(),
                                     self.player_resource[player],
                                     self.player_influence[player],
                                     self.num_tiles -
                                     len(self.player_planets[player]),
                                     []):
                return False
        return True

    # Sweep unused tiles into shared_planets
    def check_all_used(self):
        for ii in range(0, len(self.used)):
            if not self.used[ii]:
                self._allocate_planet(ii, -1)

    # Return a shuffled vector of unused tile indices
    def _get_unused_vector(self):
        unused_tiles = []
        unused_tiles = [ii for ii in range(
            0, len(self.used)) if self.used[ii] == 0]
        random.shuffle(unused_tiles)
        return unused_tiles

    # Attempt to allocate tiles to a player
    #   such that resource and influence totals are correct
    #   Return True on success, False on failure
    #   State should only be updated on success
    def _fill_player(self, player_num, unused_tiles,
                     resources_required, influence_required,
                     num_planets, player_planets):
        # Terminate on fail in num_planets is below 0
        if num_planets < 0:
            return False
        # Terminate on success if we have successfully allocated everything
        if (num_planets == 0 and
                resources_required == 0 and
                influence_required == 0):
            for planet in player_planets:
                self._allocate_planet(planet, player_num)
            return True
        # Remove tiles that cannot be allocated
        new_unused_tiles = [tile
                            for tile in unused_tiles
                            if (resources_required >= resource[tile] and
                                influence_required >= influence[tile])]
        # Iterate until we have successfully allocated a planet
        while (True):
            if len(new_unused_tiles) == 0:
                return False
            # Select first tile and allocate
            candidate_tile = new_unused_tiles[0]
            new_unused_tiles = new_unused_tiles[1:]
            # Take a deep copy so the loop throws away failed allocations
            new_player_planets = list(player_planets)
            new_player_planets.append(candidate_tile)
            # Recurse, on false remove first tile
            if self._fill_player(player_num, new_unused_tiles,
                                 resources_required - resource[candidate_tile],
                                 influence_required -
                                 influence[candidate_tile],
                                 num_planets - 1, new_player_planets):
                return True

    # Configure the results and allocate special tiles depending on number of players
    def _configure(self, config):
        # Set the number of players
        self.num_players = config["num_players"]
        # Set the number of tiles to allocate to each player
        self.num_tiles = config["num_tiles"]
        # Set resources and influence budget for each player
        self._configure_rip(list(config["resource_influence_allocations"]))
        # Allocate wormholes to the players
        self._configure_w()
        # Specials are allocated in two sets, one randomised, and one fixed
        # left over specials are put in shared_planets
        specials_r = list(config["specials_shuffled"])
        random.shuffle(specials_r)
        specials = None
        if "specials_fixed" in config:
            specials_f = list(config["specials_fixed"])
            specials = [
                (
                    specials_r[ii][0] + specials_f[ii][0],
                    specials_r[ii][1] + specials_f[ii][1],
                    specials_r[ii][2] + specials_f[ii][2]
                ) for ii in range(0, self.num_players)
            ]
        else:
            specials = specials_r
        self._configure_ab(specials)

    # Given a vector of tuples of (resource, influence) set up internal vectors
    #   for resource, influence and player_planets
    def _configure_rip(self, res_infls):
        random.shuffle(res_infls)
        self.player_resource = [res_infl[0] for res_infl in res_infls]
        self.player_influence = [res_infl[1] for res_infl in res_infls]
        self.player_planets = [[] for res_infl in res_infls]

    # Configure wormholes, allocating evenly to players
    def _configure_w(self):
        jj = 0
        for ii in range(0, len(wormhole)):
            self._allocate_planet(wormhole[ii], jj)
            jj = jj + 1
            if jj >= self.num_players:
                jj = 0

    # Given a vector of tuples configure anomalies and blanks
    #   the tuples are (total number of anomalies and blanks,
    #                   minimum number of anomalies,
    #                   minimum number of blanks)
    #   to be allocated to each player
    def _configure_ab(self, abs):
        num_total = [ab[0] for ab in abs]
        num_anoms = [ab[1] for ab in abs]
        num_blank = [ab[2] for ab in abs]
        # Allocate reds to fixed players
        reds = list(anomaly)
        random.shuffle(reds)
        for ii in range(0, len(num_anoms)):
            for _ in range(0, num_anoms[ii]):
                self._allocate_planet(reds[0], ii)
                reds = reds[1:]
                num_total[ii] = num_total[ii] - 1
        # Allocate blanks to fixed players
        blanks = list(blank)
        for ii in range(0, len(abs)):
            for _ in range(0, num_blank[ii]):
                self._allocate_planet(blanks[0], ii)
                blanks = blanks[1:]
                num_total[ii] = num_total[ii] - 1
        # Allocate remaining tiles randomly to players with allocation
        remain = list(reds)
        remain.extend(blanks)
        random.shuffle(remain)
        for ii in range(0, len(num_total)):
            for _ in range(0, num_total[ii]):
                self._allocate_planet(remain[0], ii)
                remain = remain[1:]
        for rem in remain:
            self._allocate_planet(rem, -1)


# Print out planets given a vector of planet indices
def print_planets(name, planets, formatter):
    output = "{}{}{}{}".format(
        formatter["Title Pre"],
        name,
        formatter["Title Post"],
        formatter["Table Pre"],
    )
    total_resource = 0
    total_influence = 0
    num_planets = len(planets)
    for ii in planets:
        worm = " "
        anom = " "
        blnk = " "
        if ii in wormhole:
            worm = "W"
        if ii in anomaly:
            anom = "A"
        if ii in blank:
            blnk = "B"
        total_resource = total_resource + resource[ii]
        total_influence = total_influence + influence[ii]
        planet_name = formatter["Planet Formatter"].format(
            names[ii])
        output = (output +
                  "{}{}{}{}{}{}{}{}{}{}{}{}{}{}".
                  format(
                      formatter["System Pre"],
                      formatter["Col1 Pre"], planet_name,
                      formatter["Col2 Pre"], resource[ii],
                      formatter["Col3 Pre"], influence[ii],
                      formatter["Col4 Pre"], worm,
                      formatter["Col5 Pre"], anom,
                      formatter["Col6 Pre"], blnk,
                      formatter["System Post"]))
    output = (output +
              ("{}{}Number of systems {}, total resource: {}, " +
               "total influence {}{}").
              format(formatter["Table Post"], formatter["Summary Pre"],
                     num_planets, total_resource, total_influence,
                     formatter["Summary Post"]))
    return output


# Select tiles for each player for a given number of players
def ti4_planet_selection(num_players, style, formatter_name=None):
    config = (int(num_players), str(style))
    # By default use an html formatter
    formatter = None
    if formatter_name is None:
        formatter = _ti4_get_formatter("HTML")
    else:
        formatter = _ti4_get_formatter(formatter_name)
    results = None
    success = False
    if config not in allocations:
        return "{}Invalid configuration {}, try another configuration{}".format(
            formatter["Error Pre"], config, formatter["Error Post"])
    for _ in range(0, num_iterations):
        results = Results(allocations[config])
        if results.allocate():
            success = True
            break
    if not success:
        return "{}Unable to converge in {} iterations{}".format(
            formatter["Error Pre"], num_iterations, formatter["Error Post"])
    results.check_all_used()
    output = print_planets(
        "Shared planets:", results.shared_planets, formatter)
    for nn in range(0, results.num_players):
        output = (output +
                  print_planets("Player {}".
                                format(nn + 1),
                                results.player_planets[nn],
                                formatter))
    return output


# Return a list of all possible configs
def config_options():
    return list(allocations.keys())
