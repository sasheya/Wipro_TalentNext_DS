'''
Project: 1 
Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and his or her interesting fact to the screen. Next, change a fact about one 
of the people. Also add an additional person and corresponding fact. Display the new list of 
people and facts. Run the program multiple times and notice if the order changes.
Sample :
Input : 
Jeff: Is afraid of Dogs.
David: Plays the piano.
Jason: Can fly an airplane

Output :
jeff: Is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance
'''

facts = {
    "Jeff": "is afraid of Dogs",
    "David": "has a pet alligator",
    "Jason": "flies aeroplane"
}

print("Initial facts:")
for person, fact in facts.items():
    print(f"{person} : {fact}")
print('\n')

facts["David"] = "can hula dance"

facts["Jill"] = "is afraid of heights"

print("Updated facts:")
for person, fact in facts.items():
    print(f"{person} : {fact}")
print('\n')

print("Multiple runs:")
for _ in range(2):
    for person, fact in facts.items():
        print(f"{person} : {fact}")
    print('\n')


'''
Project: 2
Given the participant’s score sheet for your University Sports Day, you are required to find the 
runner-up score. You have scores. Store them in a list and find the score of the runner-up.
Sample input:[2, 3, 6, 6, 5]
Sample output: 5
Explanation: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we 
print 5 as the runner-up score
'''

scores = input('Enter the scores').split()
scores = [int(x) for x in scores]
scoresSet = set(scores)
sortedScores = sorted(scoresSet)
print(sortedScores[-2])


'''
Project: 3
You have a record of n students. Each record contains the student's name, and their percent marks in 
Math, Physics and Chemistry. The marks can be floating values.You are required to save the record in a 
dictionary data type.Student’s name is the key. Marks stored in a list is the value. The userenters a 
student's name. Output the average percentage marks obtained by that student.
Formula:(sum of marks) / (no of subjects)

Sample input: { 
“Krishna” : [67,68,69],
“Arjun” :[70,98,63],
“Malika” : [52,56,60] }
Sample output:
Enter a name: Malika
Average percentage mark: 56 
Explanation:Marks for Malika are [52, 56, 60] whose average is(52 + 56 + 60)/3 => 56
'''
records = {
    'Krishna' : [67, 68, 69],
    'Arjun' : [70, 98, 63],
    'Malika' : [52, 56, 60]
}

studentName = input("Enter a name: ")
marks = records[studentName]
marksSum = sum(marks)
subjects = len(marks)
print(f'Average percentage mark: {marksSum / subjects}')


'''
Project: 4
Given a string of n words, help Alex to find out how many times his name appears in the string. 
Constraint:1 <= n <= 200
Sample input:Hi Alex Welcome Alex Bye Alex.
Sample output:3
Explanation:Alex name appears 3 times in the string. Hi AlexWelcomeAlexBye Alex.
'''
n = input('Enter the string:')
words = n.split()
word = 'Alex'
count = words.count(word)
print(f'The name {word} appears {count} times in the string {n}')

