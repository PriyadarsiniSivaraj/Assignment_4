def Vowel_Test(a):
    a = input("Enter the alphabet to be checked:")
    if a.isalpha() == True:
        if len(a)>1:
            print("The input contains more than 1 element")
        else:
            if a in ('a','e','i','o','u'):
                return True
            else:
                return False
    else:
        print("The entered element is not an alphabet")
print(Vowel_Test(''))
