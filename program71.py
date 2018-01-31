#Arnez Dillard 2339394

def main():
    print("Initial list of state abbreviations")
    states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA'] #create a list of states
    outfile = open("states.txt", "w") #Writing the list onto a txt

    for item in states:
        outfile.write(item + ' ')

    outfile.close()
main()
