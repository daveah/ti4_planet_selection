#!/usr/bin/env python
import random

from _tiles import tiles
from _allocations import allocations


# Reference data - immutable
num_iterations = 100


# Configurations of various formatters
formatters = {
    "Text": {
        "Title Pre": "",
        "Title Post": "\n",
        "Table Pre": "",
        "System Pre": "  ",
        "Col0 Pre": "Num: ",
        "Col1 Pre": "; Name: ",
        "Col2 Pre": "; Resource: ",
        "Col3 Pre": "; Influence: ",
        "Col4 Pre": "; ",
        "Col5 Pre": "",
        "Col6 Pre": "",
        "Col7 Pre": "; ",
        "Col8 Pre": "; ",
        "System Post": "\n",
        "Table Post": "",
        "Summary Pre": "  ",
        "Summary Post": "\n",
        "Planet Formatter": "{:22}",
        "Error Pre": "",
        "Error Post": "\n",
    },
    "HTML": {
        "Title Pre": "<h2>",
        "Title Post": "</h2>",
        "Table Pre": (
            "<table><tr>"
            + "<th>Num</th>"
            + "<th>System Name</th>"
            + "<th>Resources</th>"
            + "<th>Influence</th>"
            + "<th>Wormhole</th>"
            + "<th>Anomaly</th>"
            + "<th>Blank</th>"
            + "<th>Trait</th>"
            + "<th>Technology</th>"
            + "</tr>"
        ),
        "System Pre": "<tr><td>",
        "Col0 Pre": "",
        "Col1 Pre": "</td><td>",
        "Col2 Pre": "</td><td>",
        "Col3 Pre": "</td><td>",
        "Col4 Pre": "</td><td>",
        "Col5 Pre": "</td><td>",
        "Col6 Pre": "</td><td>",
        "Col7 Pre": "</td><td>",
        "Col8 Pre": "</td><td>",
        "System Sep": "",
        "System Post": "</td></tr>",
        "Table Post": "</table>",
        "Summary Pre": "<p><i>",
        "Summary Post": "</i></p>",
        "Planet Formatter": "{}",
        "Error Pre": "<h2>Error</h2><p>",
        "Error Post": "</p>",
    },
}

expansion_number = {"base": 0, "pok": 1}

# Hold a set of results
class Results:
    def __init__(self, config, expansion, legendary):
        # Extract reference data into working vectors
        # All tile numbers
        self.numbers = [tile[0] for tile in tiles if tile[11] <= expansion]
        # All tile names
        self.names = [tile[1] for tile in tiles if tile[11] <= expansion]
        # Resources for each tile
        self.resource = [tile[2] for tile in tiles if tile[11] <= expansion]
        # Influence for each tile
        self.influence = [tile[3] for tile in tiles if tile[11] <= expansion]
        # Indices of wormhole systems
        self.wormhole = [ii for ii in range(0, len(tiles)) if tiles[ii][4] and tiles[ii][11] <= expansion]
        # Indices of anomaly systems (red border)
        self.anomaly = [ii for ii in range(0, len(tiles)) if tiles[ii][5] and tiles[ii][11] <= expansion]
        # Indices of blank systems
        self.blank = [ii for ii in range(0, len(tiles)) if tiles[ii][6] and tiles[ii][11] <= expansion]
        # Indices of always shared systems
        self.force_shared = [ii for ii in range(0, len(tiles)) if tiles[ii][7] and tiles[ii][11] <= expansion]
        # Indices of legendary systems
        self.legendary = [ii for ii in range(0, len(tiles)) if tiles[ii][8] and tiles[ii][11] <= expansion]
        # Traits for each tile
        self.traits = [tile[9] for tile in tiles if tile[11] <= expansion]
        # Technology for each tile
        self.technologies = [tile[10] for tile in tiles if tile[11] <= expansion]
        # Expansion number
        self.expansion = [tile[11] for tile in tiles if tile[11] <= expansion]

        non_shared_legendary = [ii for ii in self.legendary if ii not in self.force_shared]
        if legendary == 0:
            self.force_shared.extend(non_shared_legendary)
        elif legendary == 1:
            random.shuffle(non_shared_legendary)
            self.force_shared.append(non_shared_legendary[0])

        # Number of players
        self.num_players = None
        # Vector of amount of resources for each player
        self.player_resource = None
        # Vector of amount of influence for each player
        self.player_influence = None
        # Vector of planets indices for each player
        self.player_planets = None
        # Number of tiles to be allocated to each player
        self.num_tiles = 0
        # Tiles that are considered "shared"
        #   Includes Mecatol Rex,
        #   one tile to be placed next to Mecatol Rex in 5 player game and
        #   unused tiles
        self.shared_planets = []
        # Vector of whether a tile has been allocated
        #   set to zero for unallocated, one for allocated
        self.used = [0 for ii in range(0, len(tiles)) if tiles[ii][11] <= expansion]
        for tile in self.force_shared:
            self._allocate_planet(tile, -1)
        self._configure(config)

    # Allocate a planet to a given player (-1 for shared)
    def _allocate_planet(self, planet_num, player_num):
        if self.used[planet_num] == 1:
            raise RuntimeError("Attempt to allocate already used tile: {}".format(self.names[planet_num]))
        self.used[planet_num] = 1
        if player_num >= 0:
            if len(self.player_planets[player_num]) >= self.num_tiles:
                raise RuntimeError("Too many tiles allocated to player: {}".format(player_num))
            self.player_planets[player_num].append(planet_num)
            self.player_resource[player_num] = self.player_resource[player_num] - self.resource[planet_num]
            self.player_influence[player_num] = self.player_influence[player_num] - self.influence[planet_num]
        else:
            self.shared_planets.append(planet_num)

    # Allocate remaining tiles to players
    # Return true on success, false on failure
    def allocate(self):
        for player in range(0, self.num_players):
            if not self._fill_player(
                player,
                self._get_unused_vector(),
                self.player_resource[player],
                self.player_influence[player],
                self.num_tiles - len(self.player_planets[player]),
                [],
            ):
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
    def _fill_player(
        self, player_num, unused_tiles, resources_required, influence_required, num_planets, player_planets
    ):
        # Terminate on fail in num_planets is below 0
        if num_planets < 0:
            return False
        # Terminate on success if we have successfully allocated everything
        if num_planets == 0 and resources_required == 0 and influence_required == 0:
            for planet in player_planets:
                self._allocate_planet(planet, player_num)
            return True
        # Remove tiles that cannot be allocated
        new_unused_tiles = [
            tile
            for tile in unused_tiles
            if (resources_required >= self.resource[tile] and influence_required >= self.influence[tile])
        ]
        # Iterate until we have successfully allocated a planet
        while True:
            if len(new_unused_tiles) == 0:
                return False
            # Select first tile and allocate
            candidate_tile = new_unused_tiles[0]
            new_unused_tiles = new_unused_tiles[1:]
            # Take a deep copy so the loop throws away failed allocations
            new_player_planets = list(player_planets)
            new_player_planets.append(candidate_tile)
            # Recurse, on false remove first tile
            if self._fill_player(
                player_num,
                new_unused_tiles,
                resources_required - self.resource[candidate_tile],
                influence_required - self.influence[candidate_tile],
                num_planets - 1,
                new_player_planets,
            ):
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
        self._configure_w(list(config["wormholes"]))
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
                    specials_r[ii][2] + specials_f[ii][2],
                )
                for ii in range(0, self.num_players)
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
    def _configure_w(self, w):
        wormholes = []
        indices = list(range(len(self.wormhole)))
        for ii in range(len(w)):
            if w[ii] != -1:
                wormholes.append(self.wormhole[w[ii]])
                indices.remove(w[ii])
            else:
                random.shuffle(indices)
                index = indices[0]
                wormholes.append(self.wormhole[index])
                indices.remove(index)
        jj = 0
        for ii in range(0, len(wormholes)):
            self._allocate_planet(wormholes[ii], jj)
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
        reds = list(self.anomaly)
        random.shuffle(reds)
        for ii in range(0, len(num_anoms)):
            for _ in range(0, num_anoms[ii]):
                self._allocate_planet(reds[0], ii)
                reds = reds[1:]
                num_total[ii] = num_total[ii] - 1
        # Allocate blanks to fixed players
        blanks = list(self.blank)
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


def _print_traits(trait):
    name = ("cul", "haz", "ind")
    res = []
    for ii in range(0, 3):
        if trait[ii] > 0:
            res.append(f"{trait[ii]} {name[ii]}")
    if len(res) == 0:
        return ""
    return f"({', '.join(res)})"


def _sum_traits(lhs, rhs):
    return (lhs[0] + rhs[0], lhs[1] + rhs[1], lhs[2] + rhs[2])


def _print_technology(tech):
    name = ("red", "grn", "blu", "yel")
    res = []
    for ii in range(0, 4):
        if tech[ii] > 0:
            res.append(f"{tech[ii]} {name[ii]}")
    if len(res) == 0:
        return ""
    return f"({', '.join(res)})"


def _sum_technology(lhs, rhs):
    return (lhs[0] + rhs[0], lhs[1] + rhs[1], lhs[2] + rhs[2], lhs[3] + rhs[3])


# Print out planets given a vector of planet indices
def print_planets(name, planets, formatter, results):
    output = "{}{}{}{}".format(formatter["Title Pre"], name, formatter["Title Post"], formatter["Table Pre"],)
    total_resource = 0
    total_influence = 0
    total_traits = (0, 0, 0, 0)
    total_technology = (0, 0, 0, 0)
    num_planets = len(planets)
    for ii in planets:
        worm = " "
        anom = " "
        blnk = " "
        if ii in results.wormhole:
            worm = "W"
        if ii in results.anomaly:
            anom = "A"
        if ii in results.blank:
            blnk = "B"
        trait = results.traits[ii]
        technology = results.technologies[ii]
        total_resource = total_resource + results.resource[ii]
        total_influence = total_influence + results.influence[ii]

        total_traits = _sum_traits(total_traits, trait)
        total_technology = _sum_technology(total_technology, technology)
        planet_number = results.numbers[ii]
        planet_name = formatter["Planet Formatter"].format(results.names[ii])
        output = output + "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
            formatter["System Pre"],
            formatter["Col0 Pre"],
            planet_number,
            formatter["Col1 Pre"],
            planet_name,
            formatter["Col2 Pre"],
            results.resource[ii],
            formatter["Col3 Pre"],
            results.influence[ii],
            formatter["Col4 Pre"],
            worm,
            formatter["Col5 Pre"],
            anom,
            formatter["Col6 Pre"],
            blnk,
            formatter["Col7 Pre"],
            _print_traits(trait),
            formatter["Col8 Pre"],
            _print_technology(technology),
            formatter["System Post"],
        )
    output = output + (
        "{}{}Number of systems {}, total resource: {}, "
        + "total influence {}, total traits: {}, total technology: {}{}"
    ).format(
        formatter["Table Post"],
        formatter["Summary Pre"],
        num_planets,
        total_resource,
        total_influence,
        _print_traits(total_traits),
        _print_technology(total_technology),
        formatter["Summary Post"],
    )
    return output

# Select tiles for each player for a given number of players
def ti4_planet_selection(num_players, expansion, style, legendary, formatter_name=None):
    config = (int(num_players), str(expansion), str(style), int(legendary))
    # By default use an html formatter
    formatter = None
    if formatter_name is None:
        formatter = formatters["HTML"]
    else:
        formatter = formatters[formatter_name]
    results = None
    success = False
    if config not in allocations:
        return "{}Invalid configuration {}, try another configuration{}, valid configs".format(
            formatter["Error Pre"], config, formatter["Error Post"]
        )
    for _ in range(0, num_iterations):
        results = Results(allocations[config], expansion=expansion_number[expansion], legendary=legendary)
        if results.allocate():
            success = True
            break
    if not success:
        return "{}Unable to converge in {} iterations{}".format(
            formatter["Error Pre"], num_iterations, formatter["Error Post"]
        )
    results.check_all_used()
    output = print_planets("Shared planets:", results.shared_planets, formatter, results)
    for nn in range(0, results.num_players):
        output = output + print_planets("Player {}".format(nn + 1), results.player_planets[nn], formatter, results)
    return output


# Return a list of all possible configs
def config_options():
    return list(allocations.keys())
