class Question:

    def __init__(self, quest):
        self.text = quest['question']
        self.option1 = quest['opt1']
        self.option2 = quest['opt2']
        self.option3 = quest['opt3']
        self.option4 = quest['opt4']
        self.answer = quest['answer']
        self.user_answer = ''