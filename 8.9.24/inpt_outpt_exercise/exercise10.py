# Read line number 4 from the following file

file_path = 'test.txt'

try:
    with open(file_path, 'r') as file:
        content = file.readlines()
        print(content[3].strip())

except FileNotFoundError:
    print(f'The file "{file_path}" does not exist.')