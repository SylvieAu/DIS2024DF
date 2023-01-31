print ("welcome to my book title computer!")
answer = input("Do you want me to count the characters of a book title for you? (yes/no) ").upper()
if answer == "Yes" or "yes":
     book = input("What is the title of the book?")
     length = str(len(book))
     print("There are " , length, symbols in the book title " , book, including the spaces.")
else:
    input("Ok")
     
