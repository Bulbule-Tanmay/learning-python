# Write a Python program to do arithmetical operations addition to division

#for Add 

a = int(input("First Number :- "))
b = int(input("Secand Number :- "))





print("\n")
print(f"the Addition is {a+b} \n")
print(f"the Subtraction is {a-b}\n")
print(f"the Multiplication is {a*b}\n")

#now if the number b is 0 then it will not work for divion so 
if b == 0:
    print("can't divid using  0 ")
else:
    print(f"the divion is {a/b}")




