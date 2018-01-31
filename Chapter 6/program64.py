#Arnez Dillard 2339394
def main():
    infile = open("number1.txt","r") #open the new file to be read

    num1 = int(infile.readline()) #Read the name of the file
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    num4 = int(infile.readline())
    num5 = int(infile.readline())
    infile.close()              #close file
    total = num1 + num2 + num3 + num4 + num5 #Adding the numbers displayed
    print( "the number are ", num1, num2, num3, num4, num5) #displaying the number
    print("Numbers in file add up to ", total) #Displaying the numbers added up

main() #Call the main function
