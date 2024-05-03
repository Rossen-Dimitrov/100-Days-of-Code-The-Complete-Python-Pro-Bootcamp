class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number} - {question.q_txt} (True/False): ')
        self.check_answer(answer, question.q_answer)

    def check_answer(self, c_answer, question_answer):
        if c_answer.lower() == question_answer.lower():
            print('Correct')
            self.score += 1
            print(f'{self.score}/{len(self.question_list)}')
            return True
        else:
            print('Wrong')
            return False
