a = input("Enter the text: ")
print(a)

words = a.split(" ")

coding = False

if coding:
    new_words = []
    for word in words:
        if len(word) >= 3:
            prefix = "dggv"
            suffix = "mdjd"
            new_word = prefix + word[1:] + word[0] + suffix
            new_words.append(new_word)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))
else:
    new_words = []
    for word in words:
        if len(word) >= 3:
            new_word = word[3:-3][::-1]
            new_words.append(new_word)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))
