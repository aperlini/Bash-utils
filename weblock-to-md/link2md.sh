#! /bin/bash

set -e

folder="exports"
declare -i counter

if [[ ! -d "$folder" ]]; then
	mkdir $folder
fi

for entry in *; do
    if [[ ! -d "$entry" ]] && [[ "${entry##*.}" == "webloc" ]]; then
        link=$(cat "$entry" | grep -oP '(?<=<string>).*?(?=</string>)')
        title=$(basename -s '.webloc' "$entry") 
        echo "[$title]($link)" >> $folder/links.md
        rm "$entry"
        counter+=1
    fi
done

if [[ $counter -eq 0 ]]; then
    echo "no .webloc file present"
else
    echo "===================================================================="
    echo "${counter} links where extracted and saved here => ./export/links.md"
    echo "===================================================================="
fi
