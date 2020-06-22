# MB-Lab
#
# MB-Lab fork website : https://github.com/animate1978/MB-Lab
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#
# ManuelbastioniLAB - Copyright (C) 2015-2018 Manuel Bastioni

import logging

import os
import json
import array
import time

import mathutils
import bpy

from . import utils
from .utils import get_object_parent


logger = logging.getLogger(__name__)

def save_json_data(json_path, char_data):
    try:
        with open(json_path, "w") as j_file:
            json.dump(char_data, j_file, indent=2)
    except IOError:
        if json_path != "":
            logger.warning("File can not be saved: %s", json_path)
    except Exception:
        logger.warning("The data are not serializable: %s", json_path)

def load_json_data(json_path, description=None):
    try:
        time1 = time.time()
        with open(json_path, "r") as j_file:
            j_database = json.load(j_file)
            if not description:
                logger.info("Json database %s loaded in %s secs",
                            json_path, time.time()-time1)
            else:
                logger.info("%s loaded from %s in %s secs",
                            description, json_path, time.time()-time1)
            return j_database
    except IOError:
        if json_path != "":
            logger.warning("File not found: %s", json_path)
    except json.JSONDecodeError:
        logger.warning("Errors in json file: %s", json_path)
    return None

