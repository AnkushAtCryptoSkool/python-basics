# tuples are immutables just like strings
from pprint import pformat

t = (23,1,34,33)
print(t)

#set
set = {1,2,3}
set2 = {2,3,4,4,5}
print(set)
print(set2)
print(set.union(set2))
print(set.intersection(set2))

#dictonary | just like maps in java
del set

dict = {}
a = set()
print(type(dict))
print(a,type(a))

ans = {"1" : "Harry","2" : "Ankush"}
print(ans["2"])
print(ans.get("1"))
print(ans.keys())
print(ans.values())
print(ans.items())