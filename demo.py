#Sample code
print("\nHello Word!\n")
for i in range(0,10):
    for j in range(0,i+1):
        print("* ", end="")
    print(" ")
print("\nEnd of the star pattern")
print("Done by Naga Aravind Kundeti")
n=int(input("Enter the year: "))
if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print("Its a leap year")
else:
    print("Not a Leap year")
