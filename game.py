import random 

def game(user):
    computer=random.choice([-1,0,1])
    l=["snake","gun","water"]
    if user not in l:
        print(f"invalid entry,enter values in{l}")
        return
    
    dict={"snake":1,"water":0,"gun":-1}
    undict={1:"snake",0:"water",-1:"gun"}
    user_di=dict[user]
    print(f"user choice is {user}")
    print(f"computer choice is {undict[computer]} ")
    
    if(computer==user_di):
        print("tie")
    else:
        if (computer-user_di)==1 or (computer-user_di)==-2 :
            print("user lose")
        elif (computer-user_di)==-1 or (computer-user_di)==2:
            print("user win")

user=input("enter your choice: ")
game(user)