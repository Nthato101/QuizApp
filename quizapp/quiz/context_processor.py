from .quiz_logic import QuizBrain
from .question_set import Question


def quiz_setup():
    question_list =[ 
                            {
                                'question':'David Beckham became president of which newly founded club in 2018?',
                                'opt1':'Bergamo Calcio',
                                'opt2':'Inter Miami',
                                'opt3':'West London Blue',
                                'opt4': 'The Potteries',
                                'answer':'Inter Miami' 
                            },
                            {
                                'question':'Who won the Man of the Match award in the 2014 World Cup final?',
                                'opt1':'Mario Goetze',
                                'opt2':'Sergio Aguero',
                                'opt3':'Lionel Messi',
                                'opt4': 'Bastian Schweinsteiger',
                                'answer':'Lionel Messi'
                            },
                            {
                                'question':'Which footballer holds the record for the highest number of assists in the Premier League?',
                                'opt1':'Cesc Fabregas',
                                'opt2':'Ryan Giggs',
                                'opt3':'Frank Lampard',
                                'opt4': 'Paul Scholes',
                                'answer':'Ryan Giggs' 
                            },
                            {
                                'question':'Jamie Vardy was signed by Leicester from which non-league side?',
                                'opt1':'Ketting Town',
                                'opt2':'Alfreton Town',
                                'opt3':'Grimsby Town',
                                'opt4': 'Fleetwood Town',
                                'answer':'Fleetwood Town'
                            },
                            {
                                'question':' Chelsea beat which team 8-0 to secure the 2009-10 Premier League title on the final day of the season?',
                                'opt1':'Blackburn',
                                'opt2':'Hull',
                                'opt3':'Wigan',
                                'opt4': 'Norwich',
                                'answer':'Wigan' 
                                },
                            {
                                'question':'Manchester United beat which team in the 2017 Europa League final?',
                                'opt1':'Villarreal',
                                'opt2':'Chelsea',
                                'opt3':'Ajax',
                                'opt4': 'Borussia Dortmund',
                                'answer':'Ajax'
                            },
                            {
                                'question':'Which team did Porto beat in the 2004 Champions League final?',
                                'opt1':'Bayern Munich',
                                'opt2':'Deportivo La Coruña',
                                'opt3':'Barcelona',
                                'opt4': 'Monaco',
                                'answer':'Monaco' 
                            },
                            {
                                'question':'What was the score in the Euro 2012 final?',
                                'opt1':'1-0',
                                'opt2':'3-0',
                                'opt3':'5-0',
                                'opt4': '4-0',
                                'answer':'4-0'
                            },]
    question_bank = []
    for item in question_list:
        new_question = Question(item)
        question_bank.append(new_question)
    return question_bank


def quiz_brain(request):
    quiz_questions = quiz_setup()
    quiz_run = QuizBrain(request,quiz_questions)
    index = quiz_run.question_number
    context = {
        'question': quiz_questions[index].text,
        'question_number':index + 1,
        'total_questions':len(quiz_questions)
    }


    return context
    