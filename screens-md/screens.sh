#!/bin/bash

set -e

if [ $# -lt 2 ]
then
	echo -e "Missing file"
	echo -e "Usage: $0 <filename> <folder>"
	exit 1
else
	filename=$1
	folder=$2
	folder=${folder////} # remove "/"
fi

patterns=$(grep -E '^\!\[(.*?)\]$' $filename)

for old in $patterns
do
	echo $old
	# name=${old[@]:2:-1}
	# new="${old}($folder/$name.png)"
	# sed -i "s/${old//[-!\[\]\/]/\\&}/${new//[-!\[\]\/]/\\&}/g" $filename
	# echo -e $new
done

echo -e "\ndone"

