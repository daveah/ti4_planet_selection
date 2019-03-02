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
        "Table Pre": "",
        "System Pre": "  ",
        "Col1 Pre": "Name: ",
        "Col2 Pre": "; Resource: ",
        "Col3 Pre": "; Influence: ",
        "Col4 Pre": "; ",
        "Col5 Pre": "",
        "Col6 Pre": "",
        "System Post": "\n",
        "Table Post": "",
        "Summary Pre": "  ",
        "Summary Post": "\n",
        "Planet Formatter": "{:22}",
    }
    print(ti4_planet_selection(args.num_players, formatter))

if __name__ == "__main__":
    main()
