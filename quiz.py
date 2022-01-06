#random quiz generator
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz in range(35):
    quizFile = open(f'capitalsquiz{quiz + 1}.txt', 'w')
    answerkey = open(f'capitalsanswers{quiz + 1}.txt' , 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Version{quiz + 1})')
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)
    for question in range(50):
        correct = capitals[states[question]]
        wrong = list(capitals.values())
        del wrong[wrong.index(correct)]
        wrong = random.sample(wrong, 3)
        answers = wrong + [correct]
        random.shuffle(answers)

        quizFile.write(f'{question + 1}. What is the capital of {states[question]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. { answers[i]}\n")
        quizFile.write('\n')
        answerkey.write(f"{question + 1}. {'ABCD'[answers.index(correct)]}\n")

quizFile.close()
answerkey.close()