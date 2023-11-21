#! /bin/bash

set -e

folder="exports"
value=$(cat * | grep -oP '(?<=<string>).*?(?=</string>)')
if [[ ! -d "$folder" ]]; then
	mkdir $folder
fi

for v in $value; do
   echo "[$v]($v)" >> $folder/links.md
done
