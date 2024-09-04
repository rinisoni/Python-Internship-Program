# AND OR NOT
physics=int(input("enter marks of physics"))
chem=int(input("enter marks of chemistry"))
if physics>=33 and chem>=33:
    print("pass")
else:
    print("fail")

#OR
if physics>=33 or chem>=33:
    print("pass")
else:
    print("fail")

#NOT
phy=55
chem=99
print(33>=phy)

print(not(physics>33 and chem>33))


