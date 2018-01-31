#Arnez Dillard 2339394
def main():
    celeb = input("Enter celebrity name or Enter to quit ")
    #open a file named celebs.txt
   
    myfile = open("celebs.txt" , "w")
    myfile.write(celeb +"\n")
    
    #Close the file
    myfile.close()

    print("File was created and closed ")
#Call the main function
main()

