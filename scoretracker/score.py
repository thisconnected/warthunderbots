#!/usr/bin/env python3

from urllib.request import urlopen
import os
import configparser


config = configparser.ConfigParser()
config.read("../config.ini")

url = "https://warthunder.com/en/community/claninfo/" + config['OPTIONS']['squadron']
