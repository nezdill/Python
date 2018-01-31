#Arnez Dillard 2339394
def main():#
    
    for row in range(1,10):#loops that uses numbers for chart
        for column in range(1,10):
            print(format(row * column,'4d'),end='')
        print() #displaying the chart
main()
