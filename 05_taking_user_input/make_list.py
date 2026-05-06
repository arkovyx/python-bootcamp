def get_list():
    alphabets = []

    word = "wertyuioplkjhgfdsazxcvbnmWERTYUIOPLKJHGFDSAZXCVBNM"
    for letter in word:
        alphabets.append(letter)
        if 'M' in alphabets:
            print(alphabets)

get_list()
