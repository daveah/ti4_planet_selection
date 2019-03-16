#!/usr/bin/env python
from os import listdir, system
from os.path import isfile, join
import argparse
import sys

from transcrypt.__main__ import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Build and upload website")
    parser.add_argument("action", choices=["build", "upload", "all"])
    parser.add_argument("-l", "--url", default="")
    parser.add_argument("-u", "--username", default="")
    parser.add_argument("-p", "--password", default="")
    parser.add_argument("-d", "--directory", default="")
    args = parser.parse_args()
    if args.action in ["build", "all"]:
        sys.argv = ["", "-b", "-m", "-n", "_ti4_planet_selection.py"]
        main()
    if args.action in ["upload", "all"]:
        file_list = ["index.html", "ti4.css"]
        file_list = file_list + [
            str(join("__target__", ff))
            for ff in listdir("__target__")
            if isfile(join("__target__", ff))]
        file_list_bin = ["ti4.jpg"]
        ftp_cmd_line = (
            "verbose\n" +
            "open {}\n".format(args.url) +
            "user {} {}\n".format(args.username, args.password) +
            "cd {}\n".format(args.directory) +
            "mkdir -p __target__\n" +
            "ascii\n")
        for file in file_list:
            ftp_cmd_line = (ftp_cmd_line +
                            "put {}\n".format(file))
        ftp_cmd_line = ftp_cmd_line + "bin\n"
        for file in file_list_bin:
            ftp_cmd_line = (ftp_cmd_line +
                            "put {}\n".format(file))
        ftp_cmd_line = ftp_cmd_line + "bye\n"
        print(ftp_cmd_line)
        system("echo \"{}\" | ftp -n".format(ftp_cmd_line))
