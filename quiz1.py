questions = ['Who founded python?', 'What is the shortened version of "boolean" in Python?', 'what is 23+71?',
             'when was Python created?', 'To assign a variable, do we use = or ==?']

answers = ['Guido van Rossum', 'bool', '94', '1991', '=']


def quiz (questions ,answers) :
    score = 0
    #for i in  (questions): we can't use this way to iterate since we need to use the elements according to indices
        #print (i)
    for i in range (len(questions)) : # we use range(len) in order to access the elements of a particular index later
        print (questions[i])
        user = input('Give the answers :')
    
        if user == answers[i] :
            print ('Great work')
            score += 1
        else:
            print ('wrong answer, you scored')

    
    print (f' The final score  is : {score} ')

quiz (questions ,answers)

#using dictionary

QUESTIONS_AND_ANSWERS = [{'question': 'Who founded python?', 'answer': 'Guido van Rossum'},
                         {'question': 'What is the shortened version of "boolean', 'answer': 'bool'},
                         {'question': 'what is 23+71?', 'answer': '94'},
                         {'question': 'To assign a variable, do we use = or ==?', 'answer': '=='}]

def quiz (QUESTIONS_AND_ANSWERS) :
    score = 0
    for i in QUESTIONS_AND_ANSWERS:
        print (i['question'])
        answers == input( 'Enter your answer : ')
        if answers == i['answer'] :
            print('correct answers ')
            score += 1
        else:
            print('not correc' , score)
    
    print(f' final sccore is {score}')

quiz(QUESTIONS_AND_ANSWERS)



