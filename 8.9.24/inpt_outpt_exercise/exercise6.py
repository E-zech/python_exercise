# Write all content of a given file into a new file by skipping line number 5

given_file_path = 'test.txt'
new_file_path = 'new_file.txt'
content = []
count = 1

with open(given_file_path, 'r') as file:
    content = file.readlines()

with open(new_file_path, 'x') as newFile:
    for line in content:
        if count == 5:
            count += 1
        else:
            count += 1
            newFile.write(line)