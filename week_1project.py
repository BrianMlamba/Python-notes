
#Question 1
Question_1 = input("What is the capital city of Ghana?")
print( "A. Accra")
print ("B. Nairobi")
print ("C. Dakar ")
print( "D. Kampala")
answer = input ("your answer :  ") 
score = 1
if answer == "A ":
  score +=  1 
    #Question 2
Question_2 = input("What is the capital city of Kenya?")
print("A. Addis Ababa")
print("B.Kigali")
print("C.Nairobi")
print ("D.Abuja")
answer = input(" your answer : ")
if answer == "C" :
     score += 1
    #Question3
Question_3 = input("Which year did Kenya gain independence?")
print("A.1962")
print(" B.1963")
print("C.1964")
print("D.1960")
answer = input(" your answer : ")
if answer == "B": 
    score += 1
    #Question4
Question_4 = input("How many colours does the Kenyan flag have?")
print("A.1")
print("B.2")
print("C.3")
print("D.4")
answer = input(" your answer : ")
if answer == "D":
    score += 1
    #Question5
Question_5 = input("Which is the largest country in Africa?")
print("A.SouthAfrica")
print("B.Uganda")
print("C.Algeria")
print("D.Tanzania")
answer = input(" your answer : ")
if answer == "C":
    score += 1
elif answer != "C" :
    score += 0
    #TOTAL SCORE
    print("\nFinal_score : " , score , "5")
if score == 5 :
    print( "excellent")
elif score == 4 :
    print("Good")
else :
    print(" try again")
    import random
    questions = {1,2,3,4,5}
    random.shuffle (questions)
    print(questions)

  
  
     


        
