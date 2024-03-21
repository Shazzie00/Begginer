player = input("Are you a Marvel fan ? ")
if player.lower() == "yes":
    print("Welcome Marvel fan, let's test how well you know marvel")
else:
    print(" Oh no, well lets take a short quiz to improve your knowledge on marvel")

#Score Calculation begins at this question. Starting point form 0
score = 0

#Question 1 ( Math based Question) += Score begins to tally
print("\nFirst a quick math question")
number_question = int(input("150 + 150 = "))
if number_question == 300 :
    print("Correct")
    score += 1
else:
    print("Incorrect")

print ("\n LET'S BEGIN !")
# Question 2 ( Marvel Themed quiz begins )


print("\nWho is the actor for Captain America ")

print("A. Tony Starks")
print("B. Tom Holland")
print("C. Chris Evans")
print("D. Jason Momoa")
player = input("answer :  ")

if player.upper() == "C":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 3 ( True and false based question)
print("\nMarvels first comic book superhero was Iron Man \nTrue(A)  or False (B)  ")
player = input("answer : ")
if player.lower() == "b" :
    print("Correct")
    score += 1
else :
    print("Incorrect")


#Question 4 (multiple string or option in this statment because there are a variety of answer in same range for her name)

print ("\nWho is Spider Mans main love interest ? ")
player = input("answer :  ")
if player.lower() == "mary jane" or player.lower() == "mj" or player.lower() == "m.j" or player.lower() == "maryjane" or\
        player.lower() == "mary jane watson ":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

#Question 5 (multiple choice question)

print("\n In Which film did the character Black Widow die in ?  ")

print("A. Black Widow ")
print("B. Avengers : Endgame ")
print("C. Captain America: Civil War")
print("D. Black Panther ")
player = input("answer :  ")
if player.upper() == "B":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

#Question 6 (Extra bonus question any choice chosen gives player an additional point)

print("\nWhat is the best Marvel film? ")
print("A. Avengers : Endgame ")
print("B. Spider-man: no way home ")
print("C. Wakanda Forever ")
player = input("answer : ")
if player == "A" or "B" or "C":
    print("Correct ! That is my favourite one too ;)")
    score += 1
if not (player) :
    print("Incorrect!")


# score is shown how many question player got right
score= score
print("\nCongratulation, you got",score,"question correct")
# total shows user their percentage and introduces an if, else statment.
total = int(score/6 * 100)
print("Your score is ",total,"%")
if total > 80:
    print ("You are a true Marvel fan")
else:
    print("Thank you for participating :)")

print("Done")
