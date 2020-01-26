let={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26
}
message=input("message:")
char=len(message)
pad=input("The pad: (Should be as long as the message)")
arr1=[]
arr2=[]
arr3=[]
for lett in message:
    num=let.get(lett, "none")
    arr1.append(num)

for lett in pad:
    nu=let.get(lett, "none")
    arr2.append(nu)
v=0
for i in range(char):
    add=arr1[v]+arr2[v]
    if add>26:
        add-=26
    arr3.append(add)
    v+=1
print(''.join(map(str, arr3)))
