#Task1
sample_string = input("Enter word: ")
if sample_string.isalpha():
    if len(sample_string)<2:
        print("Try longer word")
    elif len(sample_string)>=2:
        print(sample_string[:2]+sample_string[-2:])    
elif sample_string[0]==' ' or sample_string[1]==' ':
      sample_string="Empty String"# or sample_string=' '
      print(sample_string)
else: print("Come on! u failed even to write a word!?")