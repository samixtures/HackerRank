# Enter your code here. Read input from STDIN. Print output to STDOUT
num = input()
thisdict = { }
for x in range(int(num)):
    newinp = input().split()
    thisdict[newinp[0]]=newinp[1]
# print(thisdict)
for y in range(int(num)):
    newerinp = input()
    if newerinp in thisdict.keys():
        print(newerinp+"="+thisdict.get(newerinp))
    else: print("Not found")