#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#  diapo.py
#  
#  Copyright 2016 valentin basel <valentinbasel@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
###############################################################################

"""
Diapo string
"""
import configparser
import argparse

from diapocls import Diapo
from parser import ParserGenerator
from os import path


class ConfigDiapo(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ConfigDiapo, self).__init__()
        self.arg = arg
        self.Config = configparser.ConfigParser()
        self.Config.read(self.arg)

    def create_config(self, section):
        """docstring for fname"""
        dict = {}
        options = self.Config.options(section)
        for option in options:
            dict[option] = self.Config.get(section, option)
        return dict


def main(args):
    config_descrpt = 'Diapo, program from convert txt in svg sozi presentation'
    parserarg = argparse.ArgumentParser(description=config_descrpt)
    parserarg.add_argument('-c', '--config', 
                           help='Config file for SVG', required=True)
    parserarg.add_argument('-s', '--source', 
                           help='File .txt with source code', required=True)
    parserarg.add_argument('-f', '--file', 
                           help='File .svg with filename', required=True)
    parserarg.add_argument('-p', '--prepare', 
                           help='create a template from image directory', 
                           required=False)
    args = vars(parserarg.parse_args())
    confile = args["config"]
    diaposource = args["source"]
    diaponame = args["file"]
    if path.exists(confile) and path.isfile(confile):
        try:
            CONFIG = ConfigDiapo(confile)
            conf = CONFIG.create_config("general")
            DIAPO = Diapo(conf)
        except:
            print("config file ist not valid .ini file")
            #print(e)
            exit(1)
            #raise e
    else:
        print("error confif file not exist")
        exit(1)
    if path.exists(diaposource) and path.isfile(diaposource):    
        file = open(diaposource, "r")
        txt = file.read()
        file.close()
    else:
        print("error, file not exist")
        exit(1)
    gen = ParserGenerator(DIAPO)
    gen.parsed_diapo(txt)
    DIAPO.save(diaponame)
    return 0 


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


