grade = []
hrs = []

while True:

    x = input("_")

    if x == "end":
        break

    x = x + " "

    temp1 = ""
    temp2 = ""
    i = 0

    for l in x:
        if(l != " "):
            if i == 0:
                temp1 = temp1 + l
            else:temp2 = temp2 + l
        else:
            if(i == 0):
                grade.append(temp1)
                i = i + 1
            else:
                hrs.append(temp2)
    
    
    
print(grade, hrs)

link = "./out.js"
#reset the out file 
with open (link, 'w') as out :
    out.write("")


# start writing the code 
with open (link , "a") as out :

    out.write("export const out=[ \n")


    for i in range (0, len(grade)):
        out.write("["+str(grade[i])+ ","+ str(hrs[i])+ "], \n" )


    out.write("]")

print()
print("Done!")
