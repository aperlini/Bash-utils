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


def update_presets(filename:str, alias:str, key_index:str, action:int, index:int='0')->Pattrstorage:

   slots = Slots()
   
   with open(filename, 'r') as f:
      data = json.load(f)
      for _, slot in data['pattrstorage']['slots'].items():
         file_index = slot['data'][key_index][0]
         if action == 0: 
            if file_index != index:
               if file_index > index:
                  slot['data'][key_index][0] = slot['data'][key_index][0] - 1
               slots.update(slot['id'], slot['data'])
         else:
            if file_index > index:
               slot['data'][key_index][0] = slot['data'][key_index][0] + 1
            slots.update(slot['id'], slot['data'])

   return Pattrstorage(alias, slots)


def get_audiofile_at_index(alias:str, file_index:int)->str :
   cmd = "ls "+ alias + " | sort -f | sed -n '"+str(file_index)+"p'"
   ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
   output = ps.communicate()[0].decode("utf-8")
   return output


if __name__ == "__main__":

   # Workflow :
   # 1. read current .json presets
   # 2. update preset list and save new preset .json
   # 3. rm audiofile (bash subprocess) if needed

   ext=".json"

   if len(sys.argv)!= 4:
      print("bad usage: python3 script.py <filename.json> <file_index:int> <action:int[0:rm, 1:add]")
      sys.exit(1)

   filename = sys.argv[1]
   file_index = int(sys.argv[2])
   action = int(sys.argv[3])

   ext_index = filename.find(ext)
   alias = filename[:ext_index]
   
   # check arg preset file is json
   if ext_index == -1:
      print("invalid file type (not json file)")
      sys.exit(1)

   # check if preset file exists
   if os.path.isfile(filename) is not True:
      print(filename +" does not exist")
      sys.exit(1)

   # check if folder exists
   if os.path.exists("sources/"+alias) is not True:
      print(alias +" folder does not exist")
      sys.exit(1)

   
   audio_filename=""
   
   # id action == remove, check if audiofile exists
   if action == 0:
      # get audio file from folder
      audio_filename = get_audiofile_at_index("sources/"+alias, file_index)
      
      # check if audio file present in folder
      if len(audio_filename) == 0:
         print("no file in folder at index: "+str(file_index))
         sys.exit(1)

   # generate new preset.json file
   key_filename_index = alias + '_index'
   presets = update_presets(filename, alias, key_filename_index, action, file_index)
   serialized = PattrstorageEncoder(indent=3).encode(presets)

   # print(serialized)

   subprocess.run(['mv', filename, alias+'_old.json'])

   with open(filename, 'w') as f:
      f.write(serialized)
   
   print("preset: " + filename + " updated!")
   
   # remove file if needed
   if action == 0:
      file_to_remove = ("sources/"+alias+'/'+audio_filename).rstrip()
      subprocess.run(['rm', file_to_remove])
      print(file_to_remove + " was successfully deleted!")

   print("=============================")
   print("FOR CHANGES TO BE EFFECTIVE : ")
   print("-----------------------------")
   print("# 1) RELOAD SOUND FOLDER (from patch)")
   print("# 2) READ " + filename + " AGAIN")
   print("-----------------------------")
   
   
