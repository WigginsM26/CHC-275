names = ["John", "Paul", "Luke"]
gradelevels = [12,11,10]
GPAs = [90,74,65]
print (f"Student records for {names[0]}). {gradelevels[0]}. {GPAs[0]}")
for i in range (len(names)):
    print (f"Student records for {names[i]}. {gradelevels[i]}. {GPAs[i]}")