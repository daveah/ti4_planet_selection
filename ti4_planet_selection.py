#!/usr/bin/env python
import argparse
from _ti4_planet_selection import ti4_planet_selection, config_options


# Main function
def main():
    parser = argparse.ArgumentParser(description="Allocate tiles for TI4")
    options = config_options()
    num_players_options = sorted(list(set([option[0] for option in options])))
    expansion_options = sorted(list(set([option[1] for option in options])))
    style_options = sorted(list(set([option[2] for option in options])))
    parser.add_argument("num_players", type=int, choices=num_players_options)
    parser.add_argument("-e", "--expansion", choices=expansion_options, default="base")
    parser.add_argument("-s", "--style", choices=style_options, default="default")
    parser.add_argument("-l", "--legendary", type=int, choices=[0, 1, 2], default=0)
    args = parser.parse_args()
    formatter = "Text"
    option = (args.num_players, args.expansion, args.style, args.legendary)
    if option in options:
        print(ti4_planet_selection(args.num_players, args.expansion, args.style, args.legendary, formatter))
    else:
        raise RuntimeError("Invalid configuration, valid choices are:\n{}".format(options))


if __name__ == "__main__":
    main()
