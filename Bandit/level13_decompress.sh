#!/bin/bash

file="data.txt"
# cd $(mktemp -d) && cp "$HOME/$file" .

xxd -r "$file" > stage.bin
file="stage.bin"

while true; do
        magic=$(xxd -p -l 3 "$file")

        echo "Processing: $file (Magic: $magic)"

        if [[ $magic == "1f8b"* ]]; then
                mv "$file" "$file.gz"
                gunzip "$file.gz"
                file="${file%.gz}"
        elif [[ $magic == "425a68" ]]; then
                mv "$file" "$file.bz2"
                bzip2 -d "$file.bz2"
                file="${file%.bz2}"
        elif file "$file" | grep -qi "tar archive"; then
                tar -xf "$file"
                file=$(tar -tf "$file" | head -n 1)
        else
                echo "Final file: $file"
                break
        fi
done