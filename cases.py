a = 3;

match a:
     case 1 :
         print("Case is 1")
     case 2 :
         print("Case is 2")
     case 3 :
         print("Case is 3")
     case _:
         print("Default case")

# Write a program to print table of number which lies betweeen 1 to 10;
table = int(input("Please enter number for which you need table : "))
match table:
     case 1:
         print(" 1 2 3 4 5 6 7 8 9 10")
     case 2:
         print("2 4 6 8 10 12 14 16 18 20")
     case _:
         print("Number was out of range")