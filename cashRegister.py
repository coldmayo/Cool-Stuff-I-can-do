start=input("How much money is in your account?")
start=int(start)
withdrawlOrPutIn=input("If you are going to withdrawl money type 'withdrawl' and if you are putting in money type 'put in'")
if withdrawlOrPutIn=="withdrawl":
    minus=input("How much do you want to take out?")
    minus=int(minus)
    money=start-minus
    print(money,'dollars are still in your account')
elif withdrawlOrPutIn=="put in":
    plus=input("How much do you want to put in?")
    plus=int(plus)
    money=start+plus
    print(money,'dollars are still in your account')
else:
    print("ERROR: Not a valid answer")
