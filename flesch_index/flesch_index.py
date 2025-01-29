text=open("flesch_index.txt","r")
s=text.read()
w=s.split()
total_sentence=0
total_syllable=0
total_words=len(w)
for char in s:
    if char in ["?", "!", ";", ":", "."]:
        total_sentence=total_sentence+1
    if char.lower() in ["a", "e", "i", "o", "u","A","E","I","O","U"]:
        total_syllable=total_syllable+1
score=206.835-(1.015*(total_words/total_sentence))-(84.6*(total_syllable/total_words))
grade=(0.39*(total_words/total_sentence))+(11.8*(total_syllable/total_words))-15.59
print("Score: ",score)
print("Grade: ",grade)
if score>=0 and score<30:
    print("COLLEGE LEVEL")
        
elif score>=50 and score<60:
    print("HIGH SCHOOL")

elif score>=90 and score<=100:
    print("FORTH GRADE")
