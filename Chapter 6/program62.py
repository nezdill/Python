#Arnez Dillard 2339394
def main():
    infile = open("celebs.txt",'r') #open the file celebs.txt
    print("You entered these clebrity names")
    
    line1 = infile.readline() #name of each celeb on line
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()

    line1 = line1.rstrip("\n") #strips the new line for the name of each celeb
    line2 = line2.rstrip("\n")
    line3 = line3.rstrip("\n")
    line4 = line4.rstrip("\n")
    line5 = line5.rstrip("\n")

    infile.close() #close the file

    print(line1) #displays the name of each celeb
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print("file created was close")

main() #call the main function
