
# Standard library
import argparse

# Project
import zoonibot

parser = argparse.ArgumentParser("Welcome to the ZooniBot master!")
parser.add_argument("--debug", action="store_true", dest="debug", default=False,
                    help="Run ZooniBot in debug mode")

args = parser.parse_args()

