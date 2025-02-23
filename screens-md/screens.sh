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

regex='.*?\!\[(.*?)\]'
patterns=$(grep -E $regex $filename)

for old in $patterns
do
    name=$(echo $old | sed 's/[^a-zA-Z\-]//g')
	if [ -n "$name" ]; then
		new="${old}($folder/$name.png)"
		sed -i "s/${old//[-!\[\]\/]/\\&}/${new//[-!\[\]\/]/\\&}/g" $filename
		echo -e $new
	fi
done

echo -e "\ndone"

