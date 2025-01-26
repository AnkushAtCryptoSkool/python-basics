
# with open("text.txt","w") as f:
#      f.write("Ankush is creator of this program")
#
#
# fp = open("test1.txt","w")
# fp.write("Hi I am test1")
# fp.close()
#
# with open("text.txt","r") as f:
#  a = f.read()
#  print(a)
# fp = open("test1.txt","r")
# a = fp.read()
# print(a)
# fp.close()

with open("text.txt","a") as f:
     f.write("Ankush is creator of this program why I dont know")


fp = open("test1.txt","a")
fp.write("Hi I am test2")
fp.close()
