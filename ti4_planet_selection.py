#!/usr/bin/env python
import argparse
from _ti4_planet_selection import ti4_planet_selection, config_options


# Main function
def main():
    parser = argparse.ArgumentParser(description="Allocate tiles for TI4")
    options = config_options()
    num_players_options = sorted(list(set([option[0] for option in options])))
    style_options = sorted(list(set([option[1] for option in options])))
    parser.add_argument("num_players", type=int, choices=num_players_options)
    parser.add_argument(
        "-s", "--style", choices=style_options, default="default")
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
        "Error Pre": "",
        "Error Post": "\n",
    }
    option = (args.num_players, args.style)
    if option in options:
        print(ti4_planet_selection(args.num_players, args.style, formatter))
    else:
        raise RuntimeError(
            "Invalid configuration, valid choices are:\n{}".format(options))


if __name__ == "__main__":
    main()
