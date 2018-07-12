def filter_long_words(lst,n):
    long_words = []

    for i in lst:
        if len(i) > n:
            long_words.append(i)
        else:
            continue


    return long_words

myList = ['abc','abcd','abcde','abcdef','abcdefg','abcdegfh']
print(filter_long_words(myList,4))
