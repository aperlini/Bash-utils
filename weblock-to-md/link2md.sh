#! /bin/bash

set -e

folder="exports"

if [[ ! -d "$folder" ]]; then
	mkdir $folder
fi

for entry in *; do
    echo "$entry"
    if [[ ! -d "$entry" ]] && [[ "${entry#*.}" == "webloc" ]]; then
        link=$(cat "$entry" | grep -oP '(?<=<string>).*?(?=</string>)')
        title=$(basename -s '.webloc' "$entry") 
        echo "[$title]($link)" >> $folder/links.md
        rm "$entry"
    fi
done

echo "========================================================"
echo "all links where extracted and saved => ./export/links.md"
echo "========================================================"

