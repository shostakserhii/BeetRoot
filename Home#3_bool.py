sample_string = input("Enter word: ")
if sample_string.isalpha():
    if len(sample_string)<4:
        print("Try longer word")
    elif len(sample_string)>=4:
        print(sample_string[:2]+sample_string[-2:])     
else : print("Come on! u failed even to write a word!?")