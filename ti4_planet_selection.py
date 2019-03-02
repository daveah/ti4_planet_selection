#!/usr/bin/env python
import argparse
from _ti4_planet_selection import ti4_planet_selection, player_numbers

# Main function
def main():
    parser = argparse.ArgumentParser(description="Allocate tiles for TI4")
    parser.add_argument("num_players", type=int, choices=player_numbers())
    args = parser.parse_args()
    formatter = {
        "Title Pre": "",
        "Title Post": "\n",
        "System Pre": "  ",
        "System Post": "\n",
        "Summary Pre": "  ",
        "Summary Post": "\n",
        "Planet Formatter": "{:22}",
    }
    print(ti4_planet_selection(args.num_players, formatter))

if __name__ == "__main__":
    main()
