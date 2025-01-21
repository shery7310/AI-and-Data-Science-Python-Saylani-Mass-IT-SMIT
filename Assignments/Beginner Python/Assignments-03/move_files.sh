#!/bin/bash
# The 30 files were then move to respective folders using bash
# Define folder names and the corresponding file ranges
declare -A folder_ranges=(
    ["Basic Operations"]="Q01.py Q02.py Q03.py Q04.py Q05.py"
    ["Iterating through Dictionaries"]="Q06.py Q07.py Q08.py Q09.py Q10.py"
    ["Advanced Dictionary Usage"]="Q11.py Q12.py Q13.py Q14.py Q15.py"
    ["Nested Dictionaries"]="Q16.py Q17.py Q18.py Q19.py Q20.py"
    ["Applications of Dictionaries"]="Q21.py Q22.py Q23.py Q24.py Q25.py"
    ["Challenging Problems"]="Q26.py Q27.py Q28.py Q29.py Q30.py"
)

# Create folders and move files to the correct folder
for folder in "${!folder_ranges[@]}"; do
    mkdir -p "$folder" # Create the folder if it doesn't exist
    echo "Created folder: $folder"

    # Move the files to the folder
    for file in ${folder_ranges[$folder]}; do
        if [ -f "$file" ]; then
            mv "$file" "$folder"
            echo "Moved $file to $folder"
        else
            echo "File $file does not exist!"
        fi
    done
done

echo "All files moved successfully!"
