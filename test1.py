print("Hello there!")
text = ""
pat = "@"
with open("Classes.py", 'r+') as f:
    for line in f:
        # line = line.rstrip()
        text += line

    print(text)
    print(type(text))

    text = text.replace('@', "OBLADI-OBLADA!")
    # print(text)
    # print
    print(5)

    print(text)
