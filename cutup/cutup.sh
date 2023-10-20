#!/bin/bash

# count args
if [[ $# -lt 1 ]]; then
    echo "wrong usage" 1>&2; exit 1;
fi

declare -i wc
Words=()

for file in $@; do
    # echo $file
    # check file (must be readable file type)
    if [ -f "$file" ] && [ -r $file ]; then

        # read each word
        while read -r line; do
            for word in $line; do
                ((wc++))
                Words=("${Words[@]}" "$word")
            done
            # echo $line
        done <$file
        
    else
        echo "$file does not exist" 1>&2; exit 1;
    fi
done

tmp=$wc
indexes=()
inc=0

# gen rand unique indexes
while [ $wc -ne 0 ]; do

    index=$((RANDOM%tmp))
    
    while [[ " ${indexes[*]} " =~ " ${index} " ]]; do
        index=$((RANDOM%tmp))
    done

    indexes=("${indexes[@]}" "${index}")

    ((wc--))
done

str=""
for i in "${indexes[@]}"; do
    str+="${Words[$i]} "
done

echo "==============================" 
echo "$tmp word(s) found"
# echo "==============================" 

echo "==============================" 
echo "OUTPUT :" 
echo "==============================" 
printf '%s\n' "$str"
echo "=============================="



