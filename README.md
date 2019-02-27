# Twilight Imperium 4 Tile Allocations
Allocate system tiles with balanced resource and influence for Twilight Imperium 4.  Each run of the script generates a new set of decks, randomised within the constraints.

Use from the command line with a single parameter, -n, to specify the number of players (only 4, 5, 6 are supported).

The script will allocate wormholes, anomalies and blank tiles using a simple heuristic to mean that each player has a similar total number of non-planet tiles, and each player has at most one wormhole.

The available resource and influence is balanced across all players, and a simple recursive backtracking alogrithm used to pick a randomised set of tiles that balances resource and influence between players.  Technology, planet traits, and number of planets are not balanced.

Tile descriptions, and the heuristics to allocate non-planet tiles are factored out to ease upgrades when TI4 expansions are released.

## Background
The base rules of both Twilight Imperium 3 and 4 involve building a deck of tiles to use for the game and then randomly allocating them to players.  The group we normally play with found, over time, that this often resulted in very unbalanced games.  In Twilight Imperium 3 we found that balancing resources between each deck of tiles was sufficient to balance the game.  But with the increased importance of influence in Twilight Imperium 4, we found that balancing both resource and influence helped to create a balanced game.

There is already an excellent universe builder available online for players who would prefer to skip the universe building stage of the game.  Our group enjoys building a universe; hence this script.  Running the script provides a list of systems to allocate to each player.  What we normally do is build these decks, then randomly allocate each deck out to a player.

In order to not have too many constraints, we do not balance technology traits, planet traits, or the number of planets.  Since these are primarily used to score secret objectives, and TI4 now involves a deck building component to TI4, we are comfortable with that limitation.

## How does it work?
Firstly, depending on the number of players, a simple set of rules are used to allocate wormholes, anomalies and blank tiles.  Each player is allocate a resource and influence budget, and the number of tiles required are recorded.

Secondly, each player in turn takes a shuffled deck of remaining tiles (all planet tiles) and uses a simple back-tracking recursion to find a set of tiles that exactly matches the resource and influence budget.  It is feasible that selection of planets for an early player creates a situation whether the resource and influence budget can no longer be exactly matched for a later player.  When this occurs the solution is thrown away and recomputed.  The shuffling of the deck allows the system to converge on a feasible solution.  Testing on the base TI4 game tiles has shown that the 4 player version solves 90% of the time and the 5/6 player version 35-40% of the time.  Therefore, we expect rapid generation of a valid solution.
