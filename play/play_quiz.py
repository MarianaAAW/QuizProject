import json
import time
from play.check_input import Check


class Display(Check):
    def __init__(self):
        pass#no needed


    def read_json(self): #reads json file
        with open("quiz.json", "r") as file:
            data = json.load(file) 
        return data
    
    
    def find_quiz_by_title(self, title): #search a specific quiz by title given in display_quiz()
        data = self.read_json()
        for quiz in data:
            if title in quiz:
                return quiz[title]
        return None #return none if no quiz has that title


    def show_quiz(self, quiz): #prints the quiz and saves score
        print("\nQuiz:\n")
        score = 0
        for item in quiz: #goes trough each Q
            print("---<3---")
            print(f"Question: {item['question']}")
            for index, option in enumerate(item['options'], 1): #arranges the opt of ans to print 
                print(f"{index}. {option}")
            valid_answers = [str(i) for i in range(1, len(item['options']) + 1)]#a list of all the possible ans since the amount of opt is define by the user when creating the quiz
            answer_index = self.error("Enter the number of your answer: ", valid_ans=valid_answers)#method from Check to only accept the criteria of valid_answers
            if item['options'][int(answer_index) - 1] == item['answer']:#checks if it is the same as the correct ans so adds the score
                score += 1
        print(f"Your score: {score}/{len(quiz)}")
        time.sleep(2)
        print("---<3---\nHope you liked it and come back later <3\n---<3---")
        time.sleep(4)

    
    def display_quiz(self):
        data = self.read_json()#gets quizzes
        while True:
            time.sleep(1)
            title = input("Enter the full title of the quiz you want to play or press Enter to see all the quizzes availables: ")#ask for title desired
            quiz = self.find_quiz_by_title(title)#search it in json file
            if quiz is not None:
                self.show_quiz(quiz)#goes to print
                break
            else:
                print(f"No quiz found with the title '{title}'")
                available_titles = [list(quiz.keys())[0] for quiz in data]#shows all the quizzes' titles
                time.sleep(1)
                print(f"Available quiz titles: {', '.join(available_titles)}")
