#Arnez Dillard 2339394
import random #This program displays a random number

def main():
    file_size = random.randint(4,7) #Random number ranges
    odd_nums = range(5,20,2) #displays odd numbers only
    with open("number.txt", "w") as f: #opens the new file
        for _ in range(file_size): #displays the numbers
            n = random.choice(odd_nums)
            f.write('{}\n'.format(n)) #displays with spacing

if __name__ == '__main__':

    main() #Call the main function
