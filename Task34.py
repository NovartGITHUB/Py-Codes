list = ['a','bb','c','dddd','ee']

print(sorted(list))
def Sorting(list):
    list2 = sorted(list, key=len)
    return list2

# Driver code
list = ["rohan", "amy", "sapna", "muhammad",
       "aakash", "raunak", "chinmoy"]
print(Sorting(list))

