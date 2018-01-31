
#Displaying the title of quiz 
print("Short Civics Quiz")
print ("question 1:")
print ("What is Jury duty?")
print ("a. cleaning up trash") #Displaying question choices
print ("b. reasponsiblity of a citizen to participate in the legal process.")
print ("c. a series of task to brain wash you")
answer = input("Which letter is the correct choice? ") #Getting answer
if answer =="b":
    print ("You answer is correct!")#Determines if the answer is right
else:
      print ("Sorry, but this is the wrong answer")
print ("question 2:") #Displaying question two
answer = input("Enter an age that your allowed to vote which is supported by the 26th Amendment?:")

if answer <="18": #Determines numeric answer
        print ("You are allowed to vote")
else:
    print ("Sorry, but this answer is wrong and you would not be allowed to vote")
