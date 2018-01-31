

value = 100 #the value
over40 = 1.09 # Variables representing different ranges
over20 = .99
under20 = .89

value = int(input("Enter the value of your order $")) #Get the value and pounds

pounds = int(input("Enter the weight "))


if value >= 100:#Calculating the purchase and charges
        print("There are no shipping charges")
else:
    if pounds < 40:
        pounds = over40 * value
    else:
        if pounds > 20:
            pounds >= over20 * value
        else:
            if pounds < 20:
                 pounds <= under20 * value
print("The shipping charges along with the value is $", format(pounds,  ",.2f"), sep="")#displaying the purchase and charges
