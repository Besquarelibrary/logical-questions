def palindrome_filter(word):
    new_word = ""

    for ele in word:
        if word.count(ele) % 2 == 0:
            new_word = new_word + ele
    print(new_word)


# calling the palindrome filter method
palindrome_filter("Maneendra")
