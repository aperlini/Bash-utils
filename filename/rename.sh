#! /bin/bash

set -e

function rename {
   count=0
   prefix=$1   
   ignore=$2
   for entry in *; do
      if [[ -f $entry ]]; then 
         file_ext="${entry##*.}"
         if [[ "$file_ext" == "png" || "$file_ext" == "jpg"  ]]; then
            count=$((count+1))
            F="$count.$file_ext" 
            if [[ -n $prefix ]]; then
               F="$prefix-$count.$file_ext"
            fi
            $(mv "$entry" "$F") 
         else
            if [[ -z "${ignore}" ]]; then
               echo $file_ext
            fi
         fi
      else
         echo "$entry is not valid"
      fi
   done
   if [[ "$count" -gt 0 ]]; then
      echo "$count file(s) successfully renamed"
   fi
}

# -- MAIN -- #

PRE="$1"
IGNORE=""

## Parsing Options ##
while getopts 'i:h' opt; do
   case "$opt" in
      i) 
         PRE="$2  "
         IGNORE="I"
         ;;
   esac
done
shift "$(($OPTIND -1))"

rename $PRE $IGNORE
# usage() { echo "Usage: $0 [-i] [prefix]" 1>&2; exit 1; }








