# Create a function with variable length of arguments

def args(*arguments):
    
    for item in arguments:
        print(item)


args(20,30,80)
args('a','b')
args('a','b',20,30,80)