class QuizBrain:

    def __init__(self, request,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.q_text = ''
        self.q_answer = ''

        self.session = request.session
        quiz = self.session.get('session_key')

        if 'session_key' not in request.session:
            quiz = self.session['session_key'] = {}

        self.quiz = quiz

    def still_has_question(self):
        length = len(self.question_list)
        if length-1 > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        question_text = current_question.text
        self.q_text = question_text
        question_answer = current_question.answer
        self.q_answer = question_answer
        self.question_number += 1

        self.session.modified = True
       



    def score_check(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            return 1
        else:
            return 0