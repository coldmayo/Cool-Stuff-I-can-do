mes=input('Type in your message').upper()
output=""
#letter stands for the letters in the word from mes
for letter in mes:
#You take the ord number (the number the corresponds a letter) and add it by 13 and uncrypt it
  val=ord(letter)+13
  letter=chr(val)
  #If the letter is in lower case we subtract by 26 to get the correct letter
  if not letter.isupper():
    val-=26
    letter=chr(val)
  #We do this part bellow to get all the letters on one line
  output+=letter
print (output.lower())
#We then ask if you want to do it again and this loops infinitly
oof=input("Do you want to try again?").lower()
while oof=="yes" or oof=="y":
  mes=input('Type in your message').upper()
  output=""
  for letter in mes:
    val=ord(letter)+13
    letter=chr(val)
    if not letter.isupper():
      val-=26
      letter=chr(val)
    output+=letter
  print (output.lower())
  oof=input("Do you want to try again?").lower()
if oof=="no" or oof=="n":
  print("ok")