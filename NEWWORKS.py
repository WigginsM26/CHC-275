file = open("days.txt","r") #open("<filename>","<mode>") 


""" 
When we call the open function, the contents of your file is buffered in memory. 
"""

buffer = file.readlines() #this will take in our list of names and make each line an item inside our list 
names = [] #This would be account names
grades = [] #this would be balance
print(buffer) 
file.close() #flush the buffered memory being used for the contents of the files 
for line in buffer: #for each makes more sense here because we don't want to introduce
#index based technical overhead that is irrelevant to our program
    line = line.strip() #This removes white space
    line = line.split(",") #line is a list of two elements
                            #line[0] is the name
                            #line[1] is the grade value
    names.append(line[0])
    grades.append(line[1])
    

try: #i'm gouing to wrap this inside of a try-except because we might get an unexpected error, we haven't 
    #closed the file yet
    for i in range(len(grades)): #for-i loop because I'm modifying the grades directly
        grades[i] = int(grades[i]) #typecast
except ValueError:
    print("grade must be a number")

print(names)
print(grades)


""" 
What if we want two separate lists of related information? 

what if we wanted to have names,grade in the class? We could run two parallel
lists that are joined together by their specific indices. 

1. opening the file
2. reading it into a list called buffer
3. preproccessing the data such that we can use it in our program 

"""


""" 
We can read from a file, what about writing to a file? 
"""

names.append("Trevis")
grades.append(95)

names.append("David")
grades.append(42)


print("after adding new people")
print(names)
print(grades)




""" 
Python writemode on a file completely overwrites the file 
"""
""" 
because write mode is really a full overwrite, we need to be able to process our data into a writeable format

{name},{grade}\n <= this is the generic model for our data. 

We need to transform our names list and our grades list so that we can write it back into the file
the way to


The idea is: we want to undo our preprocesing step. If your writing into the file step is not a logical
inverse of the preprocessing step, then when we open the file again, our preprocessing procedure
might not work again. 
"""

file = open("names.txt","w") #this is going to open our file in write mode. 

#writing into file step.

buffer = [] #creating a new buffer and making it empty
#we want our lines to look like {name},{grade}\n
#each object in the parallel lists have the same index 
#for i or for-each?

for i in range(len(names)):
        #pulling out all indices within the names list(which is also the same as the grades list)
        line =  f"{names[i]},{grades[i]}\n" #this is the format we want for our file 
        buffer.append(line) #just add the line back into buffer

buffer[-1] = buffer[-1].strip() #this will pull the last whitespace off in the last element
#of our buffer


file.writelines(buffer)
file.close()

""" 
Writing this whole postprocessing step is pretty convoluted. What if nothing changed about our file
other than adding a single new record?

There is as third mode for opening a file called append mode. 
"""

names.append("james")
grades.append(-4)


file = open("names.txt","a") #a is for appendmode
line = f"\n{names[-1]},{grades[-1]}"
file.write(line)
file.close()

""" 
So now I want to grade report and export it into a textfile. 
"""

mean = sum(grades)/len(grades) #this takes the mean

""" 
Opening a file in write mode 
    1) checks if the file exists
        i)if it exists, opens the file in overwrite mode 
    2) if the file doesn't exist
        i)create a new file with filename specified in writemode.
"""

#I can write to a file that did not previously exist while also using write mode. 
grade_filename = "report_0.txt"
file = open(grade_filename,"w")
line = f"The average gpa on 11/3/2025 is {mean}"
file.write(line)
file.close()

