#!/usr/bin/env python


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
     # Allocations of wormholes, -1 signifies remaining wormholes can be randomised
#   }
#   "specials_fixed" is optional

def get_allocations():
    NUM_LEGENDARIES = 2

    allocations_3_base = {
        # 3 player game with all wormholes and 6 blanks/anomolies in play.
        # Moderate resources.
        (3, "base", "default", 0): {
            "version": "base",
            "style": "default",
            "num_players": 3,
            "num_tiles": 8,
            "resource_influence_allocations": [(13, 14), (13, 14), (13, 14)],
            "specials_shuffled": [(2, 1, 1), (2, 1, 1), (2, 1, 1)],
            "wormholes": [0, 1, 3, 2],
            "notes": "",
            "min_legendaries": 0,
        },
        # 3 player game with all wormholes and 4 other red tiles in play.
        # High resources.
        # Uses base rules for red system allocation.
        # No balancing of blanks and anomalies.
        (3, "base", "original", 0): {
            "version": "base",
            "style": "original",
            "num_players": 3,
            "num_tiles": 8,
            "resource_influence_allocations": [(14, 15), (14, 15), (14, 15)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(1, 0, 0), (2, 0, 0), (1, 0, 0)],
            "wormholes": [0, 1, 3, 2],
            "notes": "",
            "min_legendaries": 0,
        },
    }

    allocations_3_pok = {
        (3, "pok", "default", 0): {
            "version": "pok",
            "style": "default",
            "num_players": 3,
            "num_tiles": 8,
            "resource_influence_allocations": [(14, 15), (14, 15), (14, 15)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(1, 0, 1), (2, 1, 1), (2, 1, 1)],
            "wormholes": [0, 3, 4, 5, -1, -1],
            "notes": "Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (3, "pok", "original", 0): {
            "version": "pok",
            "style": "original",
            "num_players": 3,
            "num_tiles": 8,
            "resource_influence_allocations": [(14, 15), (14, 15), (14, 15)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(1, 0, 0), (1, 0, 0), (1, 0, 0)],
            "wormholes": [0, 3, 4, 5, -1, -1],
            "notes": "Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
    }

    allocations_4_base = {
        # 4 player game with all tiles in play.
        (4, "base", "default", 0): {
            "version": "base",
            "style": "default",
            "num_players": 4,
            "num_tiles": 8,
            "resource_influence_allocations": [(11, 13), (11, 12), (12, 12), (12, 12)],
            "specials_shuffled": [(3, 1, 1), (3, 1, 1), (2, 1, 1), (2, 1, 1)],
            "wormholes": [0, 1, 2, 3],
            "notes": "",
            "min_legendaries": 0,
        },
        # 4 player game with all tiles in play.
        # Uses base rules for red system allocation.
        # No balancing of blanks and anomalies.
        (4, "base", "original", 0): {
            "version": "base",
            "style": "original",
            "num_players": 4,
            "num_tiles": 8,
            "resource_influence_allocations": [(11, 13), (11, 12), (12, 12), (12, 12)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(3, 0, 0), (3, 0, 0), (2, 0, 0), (2, 0, 0)],
            "wormholes": [0, 1, 2, 3],
            "notes": "",
            "min_legendaries": 0,
        },
    }

    allocations_4_pok = {
        (4, "pok", "default", 0): {
            "version": "pok",
            "style": "default",
            "num_players": 4,
            "num_tiles": 8,
            "resource_influence_allocations": [(14, 14), (14, 14), (14, 14), (14, 14)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(3, 1, 1), (3, 1, 1), (3, 1, 1), (2, 0, 1)],
            "wormholes": [0, 4, 1, 5],
            "notes": "Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (4, "pok", "original", 0): {
            "version": "pok",
            "style": "original",
            "num_players": 4,
            "num_tiles": 8,
            "resource_influence_allocations": [(14, 14), (14, 14), (14, 14), (14, 14)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(3, 0, 0), (3, 0, 0), (3, 0, 0), (2, 0, 0)],
            "wormholes": [0, 4, 1, 5],
            "notes": "Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
    }

    allocations_5_base = {
        # 5 player game with one blank and one 1/1 system removed.
        (5, "base", "default", 0): {
            "version": "base",
            "style": "default",
            "num_players": 5,
            "num_tiles": 6,
            "resource_influence_allocations": [(9, 10), (9, 10), (9, 10), (9, 9), (9, 9)],
            "specials_shuffled": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 1, 0), (1, 1, 0)],
            "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 0, 1)],
            "wormholes": [0, 1, 2, 3],
            "notes": "Place one red tile from shared next to Mecatol Rex.",
            "min_legendaries": 0,
        },
        # 5 player game with two 1/1 systems removed.
        # Uses base rules for red system allocation.
        # No balancing of blanks and anomalies
        (5, "base", "original", 0): {
            "version": "base",
            "style": "original",
            "num_players": 5,
            "num_tiles": 6,
            "resource_influence_allocations": [(10, 10), (9, 10), (9, 10), (9, 10), (9, 9)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0), (2, 0, 0)],
            "wormholes": [0, 1, 2, 3],
            "notes": "Place one red tile from shared next to Mecatol Rex.",
            "min_legendaries": 0,
        },
        # 5 player game configured for use with a warp zone.
        (5, "base", "hyperlane", 0): {
            "version": "base",
            "style": "hyperlane",
            "num_players": 5,
            "num_tiles": 5,
            "resource_influence_allocations": [(8, 9), (8, 9), (8, 9), (8, 9), (8, 9)],
            "specials_shuffled": [(1, 1, 0), (1, 1, 0), (1, 1, 0), (1, 0, 1), (1, 0, 1)],
            "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 0)],
            "wormholes": [0, 1, 2, 3],
            "notes": "Include hyperlanes 83A, 84A, 85A, 86A, 87A, 88A.",
            "min_legendaries": 0,
        },
    }

    allocations_5_pok = {
        (5, "pok", "default", 0): {
            "version": "pok",
            "style": "default",
            "num_players": 5,
            "num_tiles": 6,
            "resource_influence_allocations": [(10, 10), (10, 10), (10, 10), (10, 10), (10, 10)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 0, 1), (1, 1, 0)],
            "wormholes": [0, 4, 1, 5, -1],
            "notes": "Place one red tile from shared next to Mecatol Rex.  Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (5, "pok", "original", 0): {
            "version": "pok",
            "style": "original",
            "num_players": 5,
            "num_tiles": 6,
            "resource_influence_allocations": [(10, 10), (10, 10), (10, 10), (10, 10), (10, 10)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 0, 0), (2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0)],
            "wormholes": [0, 4, 1, 5, -1],
            "notes": "Place one red tile from shared next to Mecatol Rex.  Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (5, "pok", "hyperlane", 0): {
            "version": "pok",
            "style": "hyperlane",
            "num_players": 5,
            "num_tiles": 5,
            "resource_influence_allocations": [(9, 9), (9, 9), (9, 9), (9, 9), (9, 9)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 0, 1), (1, 1, 0)],
            "wormholes": [0, 4, 1, 5, -1],
            "notes": "Include hyperlanes 83A, 84A, 85A, 86A, 87A, 88A.  Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
    }

    allocations_6_base = {
        # 6 player game with two blank systems removed.
        (6, "base", "default", 0): {
            "version": "base",
            "style": "default", 
            "num_players": 6,
            "num_tiles": 5,
            "resource_influence_allocations": [(8, 8), (8, 8), (8, 8), (8, 8), (7, 8), (7, 9)],
            "specials_shuffled": [(1, 1, 0), (1, 1, 0), (1, 1, 0), (1, 0, 1), (1, 0, 1), (1, 0, 1)],
            "specials_fixed": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (1, 1, 0), (1, 1, 0)],
            "wormholes": [0, 1, 2, 3],
            "notes": "",
            "min_legendaries": 0,
        },
        # 6 player game with two 1/1 systems removed.
        # Uses base rules for red system allocation.
        # No balancing of blanks and anomalies.
        (6, "base", "original", 0): {
            "version": "base",
            "style": "original",
            "num_players": 6,
            "num_tiles": 5,
            "resource_influence_allocations": [(8, 7), (8, 8), (7, 8), (7, 8), (7, 8), (7, 8)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0), (2, 0, 0), (2, 0, 0)],
            "wormholes": [0, 1, 2, 3],
            "notes": "",
            "min_legendaries": 0,
        },
    }

    allocations_6_pok = {
        (6, "pok", "default", 0):  {
            "version": "pok",
            "style": "default",
            "num_players": 6,
            "num_tiles": 5,
            "resource_influence_allocations": [(8, 8), (8, 8), (8, 8), (8, 8), (8, 8), (8, 8)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 0, 1), (2, 1, 1), (2, 1, 1)],
            "wormholes": [0, 4, 1, 5, -1, -1],
            "notes": "Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (6, "pok", "original", 0):  {
            "version": "pok",
            "style": "original",
            "num_players": 6,
            "num_tiles": 5,
            "resource_influence_allocations": [(8, 8), (8, 8), (8, 8), (8, 8), (8, 8), (8, 8)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 0, 0), (2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0)],
            "wormholes": [0, 4, 1, 5, -1, -1],
            "notes": "Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (6, "pok", "large", 2): {
            "version": "pok",
            "style": "large",
            "num_players": 6,
            "num_tiles": 9,
            "resource_influence_allocations": [(15, 15), (15, 15), (15, 15), (15, 14), (15, 14), (15, 14)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(3, 1, 1), (3, 1, 1), (3, 1, 1), (2, 0, 1), (2, 1, 0), (2, 1, 0)],
            "wormholes": [0, 4, 1, 5, -1, -1],
            "notes": "4 ring galaxy.  Optionally include 82 Mallice.",
            "min_legendaries": 2,
        },
    }

    allocations_7_pok = {
        (7, "pok", "default", 0): {
            "version": "pok",
            "style": "default",
            "num_players": 7,
            "num_tiles": 6,
            "resource_influence_allocations": [(11, 11), (11, 11), (11, 11), (11, 11), (11, 11), (11, 11), (11, 11)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 0), (2, 1, 1)],
            "wormholes": [0, 4, 1, 5, -1, -1],
            "notes": "Place 2 red and 3 blue tiles from shared adjacent to Mecatol Rex.  Include hyperlanes 83A, 84A, 85A, 86A, 87A, 88A.  Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (7, "pok", "original", 0): {
            "version": "pok",
            "style": "original",
            "num_players": 7,
            "num_tiles": 6,
            "resource_influence_allocations": [(11, 11), (11, 11), (11, 11), (11, 11), (11, 11), (11, 11), (11, 11)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 0, 0), (2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0), (2, 0, 0)],
            "wormholes": [0, 4, 1, 5, -1, -1],
            "notes": "Place 2 red and 3 blue tiles from shared adjacent to Mecatol Rex.  Include hyperlanes 83A, 84A, 85A, 86A, 87A, 88A.  Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (7, "pok", "alternate", 0): {
            "version": "pok",
            "style": "alternate",
            "num_players": 7,
            "num_tiles": 5,
            "resource_influence_allocations": [(9, 9), (9, 9), (9, 9), (9, 9), (9, 9), (9, 9), (9, 9)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 0), (2, 1, 1)],
            "wormholes": [0, 4, 1, 5, -1, -1],
            "notes": "Include hyperlanes 83B, 84B, 85B, 86B, 88B, 90B.  Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
    }

    allocations_8_pok = {
        (8, "pok", "default", 0): {
            "version": "pok",
            "style": "default",
            "num_players": 8,
            "num_tiles": 6,
            "resource_influence_allocations": [(10, 10), (10, 10), (10, 10), (10, 10), (10, 10), (10, 10), (10, 10), (10, 10)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 0), (2, 1, 1), (2, 1, 1)],
            "wormholes": [0, 4, 1, 5, -1, -1],
            "notes": "Place 2 red and 2 blue tiles from shared adjacent to Mecatol Rex.  Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (8, "pok", "original", 0): {
            "version": "pok",
            "style": "original",
            "num_players": 8,
            "num_tiles": 6,
            "resource_influence_allocations": [(10, 10), (10, 10), (10, 10), (10, 10), (10, 10), (10, 10), (10, 10), (10, 10)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 0, 0), (2, 0, 0), (2, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0), (2, 0, 0), (2, 0, 0)],
            "wormholes": [0, 4, 1, 5, -1, -1],
            "notes": "Place 2 red and 2 blue tiles from shared adjacent to Mecatol Rex.  Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
        (8, "pok", "alternate", 0): {
            "version": "pok",
            "style": "alternate",
            "num_players": 8,
            "num_tiles": 5,
            "resource_influence_allocations": [(9, 8), (9, 8), (9, 8), (9, 8), (9, 8), (9, 8), (9, 8), (9, 8)],
            "specials_shuffled": [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            "specials_fixed": [(2, 1, 1), (2, 1, 1), (2, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 0), (2, 1, 1), (2, 1, 1)],
            "wormholes": [0, 4, 1, 5, -1, -1],
            "notes": "Include hyperlanes 83B, 85B, 87A, 88A, 89B, 90B.  Optionally include 82 Mallice.",
            "min_legendaries": 0,
        },
    }

    ALL_ALLOCATIONS = [
        allocations_3_base,
        allocations_3_pok,
        allocations_4_base,
        allocations_4_pok,
        allocations_5_base,
        allocations_5_pok,
        allocations_6_base,
        allocations_6_pok,
        allocations_7_pok,
        allocations_8_pok,
    ]

    return {
        (v["num_players"], v["version"], v["style"], leg): v
        for alloc in ALL_ALLOCATIONS
        for _, v in alloc.items()
        for leg in range(NUM_LEGENDARIES + 1)
        if (v["min_legendaries"] <= leg and v["version"] == "pok") or (leg == 0 and v["version"] == "base")
    }
