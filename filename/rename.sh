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
   IGNORE=$3
   EXT=""
   for FILE in $1/*; do
      if [[ -f $FILE ]]; then 
         EXT="$(file_extension $FILE)"
         if [[ "$EXT" == "png" || "$EXT" == "jpg"  ]]; then
            INDEX=$((INDEX+1))
            PATH=${FILE%/*} 
            F="$INDEX.$EXT"
            if [[ -n $FORMAT ]]; then
               F="$PRE-$INDEX.$EXT"
            fi
            save $FILE $PATH $F
         else
            if [[ -z "${IGNORE}" ]]; then
               echo $EXT
            fi
         fi
      else
         echo "$FILE is not valid"
      fi
   done
   echo "$INDEX file(s) successfully renamed"
}

# -- MAIN -- #

FOLDER="$1"
PRE="$2"
IGNORE=""

## Parsing Options ##
while getopts 'i:h' opt; do
   case "$opt" in
      i) 
         FOLDER="$2"
         PRE="$3"
         IGNORE="I"
         ;;
   esac
done
shift "$(($OPTIND -1))"

usage() { echo "Usage: $0 [-i] <path-to-folder> [prefix]" 1>&2; exit 1; }

if [ -z "${FOLDER}" ]; then
   usage
else
   if [[ -d $FOLDER ]]; then
      parse $FOLDER $PRE $IGNORE
   else
      echo "$FOLDER is not a folder."
   fi
fi






