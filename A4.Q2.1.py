#Input Sequence
ml = ['ab','cde','erty']

#Function that maps
def My_Func(lst):
        output = list(map(lambda x:len(x),lst))
        return output

print(My_Func(ml))
