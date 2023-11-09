#!usr/bin/env python3

import os
import sys
import json
import subprocess
from typing import List, Union
from json import JSONEncoder

class Slots:
   def __init__(self, dict=None, key='1'):
      self.__dict__ = {}
    
   def update(self, key, dict):
      self.__dict__[key] = {
         "id": key,
         "data" : dict
      }

class Pattrstorage:
    def __init__(self, name:str, slots:Slots):
        self.pattrstorage = {
           "name" : name,
           "slots" : slots
        }

class PattrstorageEncoder(JSONEncoder):
   def default(self, obj):
      return obj.__dict__


def update_presets(filename:str, alias:str, key_index:str, index:int='0')->Pattrstorage:

   slots = Slots()
   # open and read json,
   # create pattrstorage representation of presets
   # find audiofile index and remove from pattrstorage
   # decrement indexes after current index
   with open(filename, 'r') as f:
      data = json.load(f)
      for _, slot in data['pattrstorage']['slots'].items():
         if slot['data'][key_index][0] != index:
            if slot['data'][key_index][0] > index:
               slot['data'][key_index][0] = slot['data'][key_index][0] - 1
            slots.update(slot['id'], slot['data'])

   return Pattrstorage(alias, slots)


if __name__ == "__main__":

   list_file = subprocess.run(['rm', 'myfile.txt'])

   # Workflow :
   # 1. read current .json presets
   # 2. find audiofile index
   # 3. rm audiofile (bash subprocess)
   # 4. update preset list and save new preset .json

   # if len(sys.argv)!= 3:
   #    print("bad usage: python3 -m main <filename.json> <file_index:int>")
   #    sys.exit()

   # ext=".json"
   # filename = sys.argv[1]
   # file_index = int(sys.argv[2])
   # ext_index = filename.find(ext)

   # if ext_index == -1:
   #    print("invalid file type (not json file)")
   #    sys.exit()

   # alias = filename[:ext_index]
   # key_filename_index = alias + '_index'

   # storage = update_presets(filename, alias, key_filename_index, file_index)
   # serialized = PattrstorageEncoder(indent=3).encode(storage)
   # # print(serialized)

   # # open and write new json
   # with open("new.json", 'w') as f:
   #    f.write(serialized)
   
