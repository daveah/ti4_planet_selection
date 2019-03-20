#!/usr/bin/env python


# Return tile information
def _ti4_load_configs():
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
    return {
        # 3 player game with all wormholes and 6 blanks/anomolies in play.
        # Moderate resources.
        (3, "default"): {
            "num_players": 3,
            "num_tiles": 8,
            "resource_influence_allocations": [(13, 14), (13, 14), (13, 14)],
            "specials_shuffled": [(2, 1, 1), (2, 1, 1), (2, 1, 1)],
        },
        # 3 player game with all wormholes and 4 other red tiles in play.
        # High resources.
        # Uses base rules for red system allocation.
        # No balancing of blanks and anomalies.
        (3, "original"): {
            "num_players": 3,
            "num_tiles": 8,
            "resource_influence_allocations": [(14, 15), (14, 15), (14, 15)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(1, 0, 0), (2, 0, 0), (1, 0, 0)],
        },
        # 4 player game with all tiles in play.
        (4, "default"): {
            "num_players": 4,
            "num_tiles": 8,
            "resource_influence_allocations": [(11, 13), (11, 12), (12, 12), (12, 12)],
            "specials_shuffled": [(3, 1, 1), (3, 1, 1), (2, 1, 1), (2, 1, 1)],
        },
        # 4 player game with all tiles in play.
        # Uses base rules for red system allocation.
        # No balancing of blanks and anomalies.
        (4, "original"): {
            "num_players": 4,
            "num_tiles": 8,
            "resource_influence_allocations": [(11, 13), (11, 12), (12, 12), (12, 12)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(3, 0, 0), (3, 0, 0), (2, 0, 0), (2, 0, 0)],
        },
        # 5 player game with one blank and one 1/1 system removed.
        (5, "default"): {
            "num_players": 5,
            "num_tiles": 6,
            "resource_influence_allocations": [(9, 10), (9, 10), (9, 10), (9, 9), (9, 9)],
            "specials_shuffled": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 1, 0), (1, 1, 0)],
            "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 0, 1)]
        },
        # 5 player game with two 1/1 systems removed.
        # Uses base rules for red system allocation.
        # No balancing of blanks and anomalies
        (5, "original"): {
            "num_players": 5,
            "num_tiles": 6,
            "resource_influence_allocations": [(10, 9), (9, 10), (9, 10), (9, 10), (9, 10)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0), (2, 0, 0)]
        },
        # 5 player game configured for use with a warp zone.
        (5, "warp"): {
            "num_players": 5,
            "num_tiles": 5,
            "resource_influence_allocations": [(8, 9), (8, 9), (8, 9), (8, 9), (8, 9)],
            "specials_shuffled": [(1, 1, 0), (1, 1, 0), (1, 1, 0), (1, 0, 1), (1, 0, 1)],
            "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 0)]
        },
        # 6 player game with two blank systems removed.
        (6, "default"): {
            "num_players": 6,
            "num_tiles": 5,
            "resource_influence_allocations": [(8, 8), (8, 8), (8, 8), (8, 8), (7, 8), (7, 9)],
            "specials_shuffled": [(1, 1, 0), (1, 1, 0), (1, 1, 0), (1, 0, 1), (1, 0, 1), (1, 0, 1)],
            "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 0), (1, 1, 0)]
        },
        # 6 player game with two 1/1 systems removed.
        # Uses base rules for red system allocation.
        # No balancing of blanks and anomalies.
        (6, "original"): {
            "num_players": 6,
            "num_tiles": 5,
            "resource_influence_allocations": [(8, 7), (8, 8), (7, 8), (7, 8), (7, 8), (7, 8)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0), (2, 0, 0), (2, 0, 0)]
        },
    }
