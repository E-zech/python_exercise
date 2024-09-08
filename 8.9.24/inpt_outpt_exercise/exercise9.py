import os
# Check file is empty or not
size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')

# check if file exxists
file = 'amiexists.txt'
def check_exists(file):
    return os.path.exists(file)
print(check_exists(file))
