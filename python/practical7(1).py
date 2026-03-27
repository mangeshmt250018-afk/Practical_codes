with open ("text.txt","r") as file:
    text=file.read()
    print("File contant :\n",text)
    tabs=0
    spaces=0
    newlines=0
    for char in text:
        if char == "\n":
            newlines += 1
        elif char == "\t":
            tabs += 1
        elif char == " ":
            spaces += 1

print("Total numbers of tabs :",tabs)
print("Total numbers of spaces :",spaces)
print("Total numbers of newline :",newlines)
