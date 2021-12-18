#! /bin/bash

function file_extension {
   if [[ -f $1 ]]; then
      case "$1" in
         *.png) echo 'png' ;;
         *.jpg) echo 'jpg' ;;
         *) echo "$1 is not JPG or PNG file" ;;
      esac
   else
      echo "$1 : file extension not valid"
   fi
}

function save {
   origin=$1
   dest="$2/$3"
   /bin/mv $origin $dest
}

function parse {
   INDEX=0
   FORMAT=$2
   for FILE in $1/*; do
      if [[ -f $FILE ]]; then 
         EXT="$(file_extension $FILE)"
         INDEX=$((INDEX+1))
         PATH=${FILE%/*} 
         F="$INDEX.$EXT"
         if [[ -n $FORMAT ]]; then
            F="$PRE-$INDEX.$EXT"
         fi
         save $FILE $PATH $F
      else
         echo "$FILE is not valid"
      fi
   done
   echo "$INDEX file(s) successfully renamed"
}


FOLDER="$1"
PRE="$2"

if [[ $# -lt 1 ]]; then
   echo "usage : rename.sh folder [prepend]"
else
   if [[ -d $FOLDER ]]; then
      parse $FOLDER $PRE
   else
      echo "$FOLDER is not a folder."
   fi
fi




