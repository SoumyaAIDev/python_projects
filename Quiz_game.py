print("Do you want to computer quiz? ")
playing =input("Do you want play?")

if playing != "yes":
    quit()
print("okey ! Let's play:)")
score = 0

answer =input("what does CPU stand for?  ")
if answer=="central processind unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer =input("what does GPU stand for? ")
if answer =="graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer =input("what does RAM stand for? ")
if answer =="random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer =input("what does PSU stand for? ")
if answer =="power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer =input("what does HDD stand for? ")
if answer =="hard disk drive":
    print("correct!")
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct!")
print("you got "+ str(score/5*100)+ "%.")
