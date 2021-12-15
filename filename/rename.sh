#!/bin/bash

FOLDER="$1"

if [[ $# -lt 1 ]]; then
   echo "missing foldername arg"
else
   if [[ -d $FOLDER ]]; then
      parse $FOLDER
   else
      echo "$FOLDER is not a folder."
   fi
fi

function file_extension {
   if [[ -f $1 ]]; then
      case "$1" in
         *.png) echo '.png' ;;
         *.jpg) echo '.jpg' ;;
         *) echo "$1 is not JPG or PNG file" ;;
      esac
   else
      echo "$1 : file extension not valid"
   fi
}

function save {
   origin=$1
   dest="$2/$3$4"
   /bin/mv $origin $dest
}

function parse {
   i=0
   for FILE in $1/*; do
      if [[ -f $FILE ]]; then 
         EXT="$(file_extension $FILE)"
         i=$((i+1))
         EXTENT=${FILE##*.} # echo 'png'
         PATH=${FILE%/*} 
         save $FILE $PATH $i $EXT
      else
         echo "$FILE is not valid"
      fi
   done
   echo "$i file(s) successfully renamed"
}



