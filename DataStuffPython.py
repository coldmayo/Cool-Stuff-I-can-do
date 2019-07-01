#This shows you how many letters are in Banana.
fruit = 'banana'
B= len(fruit)
print(B)
#This prints Old Town Roads next to its corresponding number starting at 0.
person = 'OldTownRoads'
index = 0
print("")
while index < len(person):
  letter= person[index]
  print(index, letter)
  index=index+1
#This shows you how to find the smallest values, largest values, mean, median, mode, and range in an array.
print ("")
myArray=[4728,88,69,4,69,54]
smallestval=myArray[0]
largestval=myArray[0]
#What I did here was start at the begining of the list and work my way down seeing which value is the smallest
for i in range(len(myArray)):
  if myArray[i]<smallestval:
    smallestval=myArray[i]
#Did the same thing but tried to find the biggest value, only difference is < is this > now
for i in range(len(myArray)):
  if largestval>myArray[i]:
    largestestval=myArray[i]
print (myArray)
#Used info above to find the range (largest value/smallest value)
suum=largestval-smallestval
print ("The smallest value is:",smallestval)
print("The largest value is:",largestval)
#I found Mean, Medain, and Mode here using import statistics instead of doing the math in the code.
import statistics  
x = statistics.mean(myArray) 
print("Mean is :", x) 
z = statistics.median(myArray)
print("Medain is:", z)
y=statistics.mode(myArray)
print("Mode is:", y)
print("Range is:",suum)