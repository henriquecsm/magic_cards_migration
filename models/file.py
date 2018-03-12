import json

def read_file(file):
    with open(file, 'r') as input:
        text = input.read()
    return text

def write_file(file, text):
    with open(file, "w") as fp:
        #fp.write(text + "\n")
        fp.write(text)

