#!/bin/bash

FOLDER="$1"

if [[ $# -lt 1 ]]; then
   echo "missing foldername arg"
fi

if [[ -d $FOLDER ]]; then
   parse $FOLDER
else
   echo "$FOLDER is not a folder."
fi

function file_extension {
   if [[ -f $1 ]]; then
      case "$1" in
         *.png) echo "$1 is a PNG file" ;;
         *.jpg) echo "$1 is a JPG file" ;;
         *) echo "$1 is not JPG or PNG file" ;;
      esac
   else
      echo "$1 : file extension not valid"
   fi

}

function parse {
   for FILE in $1/*; do
      if [[ -f $FILE ]]; then
         file_extension $FILE
      else
         echo "$FILE is not valid"
      fi
   done
}



