from newquiz.enter_input import Enter


class Start(Enter):
    def __init__(self):
        self.quiz_list = []
    
    def start_game(self):
        print("\n------<3------\nWelcome!!")
        self.item = input("What do you want to do?\na)Play an existing quiz\nb)Create a new game\n")
        self.error_act(valid_ans = {
            "a": ("Perfect", self.display_quiz),
            "b": ("Perfect", self.start_create)
            })
       
    



