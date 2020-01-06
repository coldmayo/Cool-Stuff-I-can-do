from itertools import permutations
n1=int(input('Put in how many words you are typing in'))
a=[]
def fun(n1):
    count=0
    cun=[]
    for i in range(n1):
        n=input('Put in the words')
        a.append(n)
        for j in a:
            j=list(j)
            perm=permutations(j)
        for k in perm:
            count+=1
            k=''.join(k)
            print(k)
    print("There are",count,"anagrams")
fun(n1)
