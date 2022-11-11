print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")
x = input("Type in your name: ")
print(f"{x}, do you think you can find the goblin hiding in the kitchen cupboards?")
print ("|__| |__| |__| |__| |__|")
y = int(input("Which cupboard do you think the goblin is in [type in number]: "))
#if y == 1:
#    print("Sorry! The goblin is still lurking somewhere else.")
#else:
#    print("Well done!! You have found the goblin. He was so scared he ran away.")
i = 1
while i < 5:
    if y == 1:
        print ("Well done!! You have found the goblin. He was so scared he ran away.")
        i = i + 1
        break
    else:
        print("Sorry! The goblin is still lurking somewhere else.")
        i = i + 1
        y = int(input("Which cupboard do you think the goblin is in [type in number]: "))
        continue

