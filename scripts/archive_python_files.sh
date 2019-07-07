# Create a text file with the list of files
find ./repos -name "*.py" > ./python_files.txt
# Split the files in to a smaller files with 5000 lines each
split -l 5000 python_files.txt files_part.
# Iterate through each of those files
for filename in ./files_part.*; do
    echo $filename
    # Archive the files
    tar -czvf "$filename".tar.gz -T $filename
done
