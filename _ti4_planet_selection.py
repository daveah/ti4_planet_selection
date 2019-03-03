#!/usr/bin/env python
import random

# Reference data - immutable
num_iterations = 100
# tiles is a vector of tuples
#   each tuple consists of name, number of resource, number of influence,
#   bool for whether tile is a wormhole,
#   bool for whether tile is an anomaly,
#   bool for whether tile is a blank,
tiles = [
    ("Mecatol Rex", 1, 6, False, False, False),
    ("Bereg, Lirta IV", 5, 4, False, False, False),
    ("Abyz, Fria", 5, 0, False, False, False),
    ("New Albion, Starpoint", 4, 2, False, False, False),
    ("Arnor, Lor", 3, 3, False, False, False),
    ("Mellon, Zohbat", 3, 3, False, False, False),
    ("Corneeq, Resculon", 3, 2, False, False, False),
    ("Lodor", 3, 1, True, False, False),
    ("Lazar, Sakulag", 3, 1, False, False, False),
    ("Centauri, Gral", 2, 4, False, False, False),
    ("Tequ'ran, Torkan", 2, 3, False, False, False),
    ("Vefut II", 2, 2, False, False, False),
    ("Saudor", 2, 2, False, False, False),
    ("Quann", 2, 1, True, False, False),
    ("Arinam, Meer", 1, 6, False, False, False),
    ("Qucen'n, Rarron", 1, 5, False, False, False),
    ("Mehar Xull", 1, 3, False, False, False),
    ("Dal Bootha, Xxehan", 1, 3, False, False, False),
    ("Wellon", 1, 2, False, False, False),
    ("Tar'mann", 1, 1, False, False, False),
    ("Thibah", 1, 1, False, False, False),
    ("A Wormhole", 0, 0, True, False, False),
    ("B Wormhole", 0, 0, True, False, False),
    ("Asteroid Field", 0, 0, False, True, False),
    ("Asteroid Field", 0, 0, False, True, False),
    ("Supernova", 0, 0, False, True, False),
    ("Nebula", 0, 0, False, True, False),
    ("Gravity Rift", 0, 0, False, True, False),
    ("Blank", 0, 0, False, False, True),
    ("Blank", 0, 0, False, False, True),
    ("Blank", 0, 0, False, False, True),
    ("Blank", 0, 0, False, False, True),
    ("Blank", 0, 0, False, False, True),
]

# allocations of tiles by number of players
#   dictionary of config type to a dictionary of allocations
#   {
#    "num_players": number of players,
#    "num_tiles": number_of_tiles_per_player,
#    "resource_influence_allocations": [(resource_allocation_player_1, influence_allocation_player_1), ...],
#    # Wormholes will be allocated to first <num_wormholes> players
#    # Allocation of specials (other than wormholes) to be randomly shuffled
#    "specials_shuffled": [(total_specials_player_n, min_anomolies_player_n, min_blanks_player_n), ...],
#    # Allocation of specials fixed to a given player number
#    "specials_fixed": [(total_specials_player_1, min_anomolies_player_1, min_blanks_player_1), ...],
#   }
#   "specials_fixed" is optional
allocations = {
    (3, "default"): {
        "num_players": 3,
        "num_tiles": 8,
        "resource_influence_allocations": [(13, 14), (13, 14), (13, 14)],
        "specials_shuffled": [(2, 1, 1), (2, 1, 1), (2, 1, 1)],
    },
    (3, "original"): {
        "num_players": 3,
        "num_tiles": 8,
        "resource_influence_allocations": [(14, 15), (14, 15), (14, 15)],
        "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
        "specials_fixed": [(1, 0, 0), (2, 0, 0), (1, 0, 0)],
    },
    (4, "default"): {
        "num_players": 4,
        "num_tiles": 8,
        "resource_influence_allocations": [(11, 13), (11, 12), (12, 12), (12, 12)],
        "specials_shuffled": [(3, 1, 1), (3, 1, 1), (2, 1, 1), (2, 1, 1)],
    },
    (4, "original"): {
        "num_players": 4,
        "num_tiles": 8,
        "resource_influence_allocations": [(11, 13), (11, 12), (12, 12), (12, 12)],
        "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        "specials_fixed": [(3, 0, 0), (3, 0, 0), (2, 0, 0), (2, 0, 0)],
    },
    (5, "default"): {
        "num_players": 5,
        "num_tiles": 6,
        "resource_influence_allocations": [(9, 10), (9, 10), (9, 10), (9, 9), (9, 9)],
        "specials_shuffled": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 1, 0), (1, 1, 0)],
        "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 0, 1)]
    },
    (5, "original"): {
        "num_players": 5,
        "num_tiles": 6,
        "resource_influence_allocations": [(10, 10), (9, 10), (9, 10), (9, 10), (9, 9)],
        "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        "specials_fixed": [(2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0), (2, 0, 0)]
    },
    (6, "default"): {
        "num_players": 6,
        "num_tiles": 5,
        "resource_influence_allocations": [(8, 8), (8, 8), (8, 8), (8, 8), (7, 8), (7, 9)],
        "specials_shuffled": [(1, 1, 0), (1, 1, 0), (1, 1, 0), (1, 0, 1), (1, 0, 1), (1, 0, 1)],
        "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 0), (1, 1, 0)]
    },
    (6, "original"): {
        "num_players": 6,
        "num_tiles": 5,
        "resource_influence_allocations": [(8, 7), (8, 8), (7, 8), (7, 8), (7, 8), (7, 8)],
        "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
        "specials_fixed": [(2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0), (2, 0, 0), (2, 0, 0)]
    },
 }

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
                                    self.num_tiles - len(self.player_planets[player]),
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
        unused_tiles = [ii for ii in range(0, len(self.used)) if self.used[ii] == 0]
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
                                influence_required - influence[candidate_tile],
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
            for jj in range(0, num_anoms[ii]):
                self._allocate_planet(reds[0], ii)
                reds = reds[1:]
                num_total[ii] = num_total[ii] - 1
        # Allocate blanks to fixed players
        blanks = list(blank)
        for ii in range(0, len(abs)):
            for jj in range(0, num_blank[ii]):
                self._allocate_planet(blanks[0], ii)
                blanks = blanks[1:]
                num_total[ii] = num_total[ii] - 1
        # Allocate remaining tiles randomly to players with allocation
        remain = list(reds)
        remain.extend(blanks)
        random.shuffle(remain)
        for ii in range(0, len(num_total)):
            for jj in range(0, num_total[ii]):
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
def ti4_planet_selection(num_players, style, formatter=None):
    config = (int(num_players), str(style))
    # By default use an html formatter
    if formatter is None:
        formatter = {
            "Title Pre": "<h2>",
            "Title Post": "</h2>",
            "Table Pre": (
                "<table><tr>" +
                "<th>System Name</th>" +
                "<th>Resources</th>" +
                "<th>Influence</th>" +
                "<th>Wormhole</th>" +
                "<th>Anomaly</th>" +
                "<th>Blank</th>" +
                "</tr>"
            ),
            "System Pre": "<tr><td>",
            "Col1 Pre": "",
            "Col2 Pre": "</td><td>",
            "Col3 Pre": "</td><td>",
            "Col4 Pre": "</td><td>",
            "Col5 Pre": "</td><td>",
            "Col6 Pre": "</td><td>",
            "System Sep": "",
            "System Post": "</td></tr>",
            "Table Post": "</table>",
            "Summary Pre": "<p><i>",
            "Summary Post": "</i></p>",
            "Planet Formatter": "{}",
        }
    results = None
    success = False
    for num_attempts in range(0, num_iterations):
        results = Results(allocations[config])
        if results.allocate():
            success = True
            break
    if not success:
        raise RuntimeError("Unable to converge in {} iterations")
    results.check_all_used()
    output = print_planets("Shared planets:", results.shared_planets, formatter)
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
