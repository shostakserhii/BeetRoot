import os.path


def count_lines(name):
    name.seek(0)
    lines = len(name.readlines())
    return lines

def count_chars(name):
    name.seek(0)
    chars = len(name.read())
    return chars


while True:

    filename = input("File name: ")
    filename = 'Task1_main.py'
    if os.path.isfile(filename):
        print("Success")
        break
    else:
        raise FileNotFoundError

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
            print(f"{count_chars(our_file)} {count_lines(our_file)} {filename}")
        
        else:
            print("no result")
            continue