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
#   dictionary of player number to a dictionary of allocations
#   {
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
    4: {
        "num_tiles": 8,
        "resource_influence_allocations": [(11, 13), (11, 12), (12, 12), (12, 12)],
        "specials_shuffled": [(3, 1, 1), (3, 1, 1), (2, 1, 1), (2, 1, 1)],
    },
    5: {
        "num_tiles": 6,
        "resource_influence_allocations": [(9, 10), (9, 10), (9, 10), (9, 9), (9, 9)],
        "specials_shuffled": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 1, 0), (1, 1, 0)],
        "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 0, 1)]
    },
    6: {
        "num_tiles": 5,
        "resource_influence_allocations": [(8, 8), (8, 8), (8, 8), (8, 8), (7, 8), (7, 9)],
        "specials_shuffled": [(1, 1, 0), (1, 1, 0), (1, 1, 0), (1, 0, 1), (1, 0, 1), (1, 0, 1)],
        "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 0), (1, 1, 0)]
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

    def __init__(self, num_players):
        self.player_resource = None
        self.player_influence = None
        self.player_planets = None
        self.shared_planets = []
        self.used = [0 for ii in range(0, len(tiles))]
        self._allocate_planet(0, -1)
        self._configure(num_players)

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
    def allocate(self, num_players):
        for player in range(0, num_players):
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
    def _configure(self, num_players):
        player_allocations = allocations[num_players]
        # Set the number of tiles to allocate to each player
        self.num_tiles = player_allocations["num_tiles"]
        # Set resources and influence budget for each player
        self._configure_rip(list(player_allocations["resource_influence_allocations"]))
        # Allocate wormholes to the players
        self._configure_w(num_players)
        # Specials are allocated in two sets, one randomised, and one fixed
        # left over specials are put in shared_planets
        specials_r = list(player_allocations["specials_shuffled"])
        random.shuffle(specials_r)
        specials = None
        if "specials_fixed" in player_allocations:
            specials_f = list(player_allocations["specials_fixed"])
            specials = [
                (
                    specials_r[ii][0] + specials_f[ii][0],
                    specials_r[ii][1] + specials_f[ii][1],
                    specials_r[ii][2] + specials_f[ii][2]
                ) for ii in range(0, num_players)
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
    def _configure_w(self, num_players):
        for ii in range(0, len(wormhole)):
            self._allocate_planet(wormhole[ii], ii % num_players)

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
        remain.append(blanks)
        random.shuffle(remain)
        for ii in range(0, len(num_total)):
            for jj in range(0, num_total[ii]):
                self._allocate_planet(remain[0], ii)
                remain = remain[1:]
        for rem in remain:
            self._allocate_planet(rem, -1)

    # Four player configuration
    #   Place Mecatol Rex in shared_planets
    #   Allocate one wormhole to each player
    #   Allocate one random anomaly to each player, the 5th to a random player
    #   Allocate one blank to each player, the 5th to a random player
    #   The random players selected for the 5th anomaly and blank should be different
    def _configure_4_players(self):
        self.num_tiles = 8
        res_infls = [(11, 13), (11, 12), (12, 12), (12, 12)]
        self._configure_rip(res_infls)
        # Allocate wormholes
        self._configure_w();
        # Allocate anomalies and blanks
        abs = [(3, 1, 1), (3, 1, 1), (2, 1, 1), (2, 1, 1)]
        random.shuffle(abs)
        self._configure_ab(abs)

    # Five player configuration
    #   Place Mecatol Rex, one (1, 1) planet and a blank in shared_planets
    #   Allocate one wormhole to each of players 1-4
    #   Allocate one random anomaly to each player
    #   Allocate one blank to player 5, the remainder to 3 random players
    def _configure_5_players(self):
        self.num_tiles = 6
        self._allocate_planet(lowest[random.randint(0, 1)], -1)
        res_infls = [(9, 10), (9, 10), (9, 10), (9, 9), (9, 9)]
        self._configure_rip(res_infls)
        # Allocate wormholes
        self._configure_w()
        # Allocate anomalies and blanks
        abs = [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 1, 0), (1, 1, 0)]
        random.shuffle(abs)
        abs[4] = (abs[4][0] + 1, abs[4][1], abs[4][2] + 1)
        self._configure_ab(abs)

    # Six player configuration
    #   Place Mecatol Rex and two blanks in shared_planets
    #   Allocate one wormhole to each of players 1-4
    #   Allocate two random anomalies, one each, to players 5-6
    #   Allocate three anomalies to random players
    #   Allocate three blanks to remaining 3 players
    def _configure_6_players(self):
        self.num_tiles = 5
        res_infls = [(8, 8), (8, 8), (8, 8), (8, 8), (7, 8), (7, 9)]
        self._configure_rip(res_infls)
        # Allocate wormholes
        self._configure_w()
        # Allocate anomalies and blanks
        abs = [(1, 1, 0), (1, 1, 0), (1, 1, 0), (1, 0, 1), (1, 0, 1), (1, 0, 1)]
        random.shuffle(abs)
        abs[4] = (abs[4][0] + 1, abs[4][1] + 1, abs[4][2])
        abs[5] = (abs[5][0] + 1, abs[5][1] + 1, abs[5][2])
        self._configure_ab(abs)


# Print out planets given a vector of planet indices
def print_planets(name, planets):
    output = "<h2>{0}</h2>".format(name)
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
        output = output + "<p>Name: {}; Resource: {}; Influence: {}; {}{}{}</p>".format(names[ii], resource[ii],
                                                                                           influence[ii], worm, anom,
                                                                                           blnk)

    output = output + "<p/><i>Number of systems {}, total resource: {}, total influence {}</i></p>".format(num_planets,
                                                                                                       total_resource,
                                                                                                       total_influence)

    return output


# Select tiles for each player for a given number of players
def ti4_planet_selection(num_players):
    results = None
    success = False
    for num_attempts in range(0, num_iterations):
        results = Results(num_players)
        if results.allocate(num_players):
            success = True
            break
    if not success:
        raise RuntimeError("Unable to converge in {} iterations")
    results.check_all_used()
    output = print_planets("Shared planets:", results.shared_planets)
    for nn in range(0, num_players):
        output = output + print_planets("Player {}".format(nn + 1), results.player_planets[nn])

    return output
