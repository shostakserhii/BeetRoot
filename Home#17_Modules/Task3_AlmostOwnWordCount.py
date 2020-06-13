import os
import sys


def count_lines(name):
    name.seek(0)
    lines = len(name.readlines())
    return lines

def count_chars(name):
    name.seek(0)
    chars = len(name.read())
    return chars
mypath = []
structure = os.listdir(os.getcwd())
for i in structure:
    i = (f"{os.getcwd()}\{i}")
    mypath.append(i)

print(mypath)

while True:

    filename = input("File name: ")
    filename = 'Task1_main.py'
    for i in mypath:
        if i == len(mypath):
            raise FileNotFoundError
        if os.path.exists((f"{i}\{filename}")):
            print("Success")
            file_address = i
            print(file_address)
            break
        else:
            print("\nchecking....")
            print(f"{i}\{filename}")
            print("Sorry, still no")
    break

os.chdir(file_address)
print(os.getcwd())

while True:
    
    with open(filename) as our_file:
        
        choice = input("""
        what do you wanna do?
            -l  to count lines
            -c  to count chars
            -n  for both counts
        -q to Quit
        """)

        if choice.strip().lower() == 'q':
            our_file.close()
            print("quitting.....")
            break

        if choice.strip().lower() == 'l':
            print(count_lines(our_file))

        if choice.strip().lower() == 'c':
            print(count_chars(our_file))
        
        if choice.strip().lower() == 'n':
            print(f"\n{count_chars(our_file)} {count_lines(our_file)} {filename}")
        
        else:
            print("no result")
            continue