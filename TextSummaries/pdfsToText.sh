#!/bin/zsh

input_dir="$1"
output_dir="$2"

# Enable nullglob to avoid issues when no matching files are found
setopt NULL_GLOB

for f in "$input_dir"/*.pdf "$input_dir"/*.PDF
do
  if [ -f "$f" ]; then
    outfile="$output_dir/${f:t:r}.txt"
    /opt/homebrew/bin/pdftotext "$f" "$outfile"
  fi
done

# Disable nullglob after processing the files
unsetopt NULL_GLOB
