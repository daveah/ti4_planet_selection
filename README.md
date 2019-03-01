# ti4_planet_selection
Allocate system tiles with balanced resource and influence for Twilight Imperium 4

Use from the command line with a single parameter, to specify the number of players (only 4, 5, 6 are supported).

The script will allocate wormholes, anomalies and blank tiles using a simple heuristic to mean that each player has a similar total number of non-planet tiles, and each player has at most one wormhole.

The available resource and influence is balanced across all players, and a simple recursive backtracking alogrithm used to pick a randomised set of tiles that balances resource and influence between players.  Technology, planet traits, and number of planets are not balanced.

Tile descriptions, and the heuristics to allocate non-planet tiles are factored out to ease upgrades when TI4 expansions are released.

## Compilation

You can compile the python code by running

```bash
python -m transcrypt -b -m -n ti4_planet_selection.py 
```
