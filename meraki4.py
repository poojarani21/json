a=open("exercise4.txt","r")
f1=open("delhi.txt","w")
f2=open("shimla.txt","w")
f3=open("other.txt","w")
b=a.read()
c=b.split("\n")
i=0
while i<len(c):
    if "delhi" in c[i]:
        f1.write(c[i])
        f1.write("\n")
    elif "shimla" in c[i]:
        f2.write(c[i])
        f2.write("\n")
    else:
        f3.write(c[i])
        f3.write("\n")
    i=i+1
a.close()

        





# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())
