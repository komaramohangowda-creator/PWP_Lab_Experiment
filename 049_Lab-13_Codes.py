file = open("Komara.txt",'w')
file.write("ICT ICT ICT \n")
file.write("ICT abcd ICT ICT ICT ICT")
file.close()

with open("ICT.text","w") as f: 
    f.write("Hello World") 
    f.close()
    
file1 = open(r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Komara.txt")

f1 = open(r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Komara.txt")
for each in f1:
    print (each)

f1 = open(r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Komara.txt")
print (f1.read())


with open(r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Komara.txt",'r') as f1:  
    data = f1.read() 
print(data)

f1 = open(r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Komara.txt")
print (f1.read(6))

with open(r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Komara.txt",'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

file = open("ICT.txt",'a')
file.write("\n ICT Department")
file.close()

with open(r'C:\Users\KOMARA MOHAN GOWDA\Downloads\KMG.tiff','rb') as file:
    binary_data = file.read()
    print(binary_data)
    
with open('KMG.tiff', 'wb') as f:
    f.write(binary_data) 
    f.close()

  

import csv
with open(r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\file.csv",'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
import csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Subject', 'Mark'])
    writer.writerow(['Mohan', 'PWP', 9])
    writer.writerow(['Gowda', 'COA', 20])
    file.close()


file1 = open(r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Example.txt.txt")
for each in file1:
    print(each)
    
with open(r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Example.txt.txt", "r") as file1:
    text = file1.read()
    
lines = text.splitlines()
words =text.split()
characters = len(text)

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Nuber of characters:", characters )    


file1 = (r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Example.txt")
lines_list = []
with open(file1, "r") as file:
    for line in file:
        lines_list.append(line.strip())
print("List of lines:", lines_list)

import csv
file_path =r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\file.csv"
with open(file1, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
file1_path =r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\Example.txt"
file2_path =r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\ICT.txt"
merged_path = r"C:\Users\KOMARA MOHAN GOWDA\OneDrive\Desktop\merged.txt"

with open(file1_path,"r") as f1, open(file2_path, "r") as f2, open(merged_path, "w") as fout:
   fout.write(f1.read())
   fout.write("\n")
   fout.write(f2.read())
print("Files merged successfully into merget.txt")     
        
    
