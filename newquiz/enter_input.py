from play.play_quiz import Display 
import json
import time #just to have cuter output in the executable

class Save():#saving to the json file
    
    def __init__(self):
        pass#no needed
        
    
    def save_to_json(self):
        with open("/Users/marianaaguerrevere/Documents/2nd Semester/adv_cod_project/quiz_project/quiz.json", "r") as file: #reads the json file (it was not working only with the name so i worked with the full path)
            data = json.load(file)
            
        data.extend(self.quiz_list) #add the new data to the existing data
        #write the updated data back to the file
        with open("/Users/marianaaguerrevere/Documents/2nd Semester/adv_cod_project/quiz_project/quiz.json", "w") as file:
            json.dump(data, file, indent=2)
   

class Enter(Save, Display): #manage creation of new quiz
    #inheriting a method from display and also takes the methods from Check through Display
    
    def __init__(self):
        self.quiz_list = []#Empty dictionary to save all the questions, options and correct answers
        self.title = None
    
    
    def detail(self):#first data needed when creating a quiz
        self.mandatory("First of all, what will be the title to save your quiz?")
        self.title = self.p

        self.n_ask = input("How many questions will your quiz have?")
        self.n_ask = self.interger(self.n_ask)#making sure that the answer is an int
                
        self.n_ans = input("How many options of answers will each question have?")
        self.n_ans = self.interger(self.n_ans)#making sure that the answer is an int
        
        return self.n_ask, self.n_ans#will be used in enter()

    
    def followup(self):
        print(f"This are your saved Q&A: {self.quiz_list}")
        self.item = input("Would you like to (a)Store your quiz and leave (b)Store your quiz and play it? ") 
        self.error_act(valid_ans = {
            "a": ("You're quiz is saved", lambda:time.sleep(2)),
            "b": ("Let's go", self.display_quiz)
                    }) #takes you out or to play the quiz 
    
    
    def enter(self):#collects and saves the data in a python format
       self.detail()
       questions = []#empty list for the dict of Q, opt and ans
       for x in range(1, self.n_ask+1):#so it easier to enumerate later
           print("---<3---")
           question = self.mandatory("Enter the quiz question: ")
           options = [] #empty list 
           for x in range(1, self.n_ans+1): #so it prints the numbers from 1 but still completing all the user's choice
               self.mandatory(f"Enter your option {x} of answer: ") 
               options.append(self.p) #into options list
           while True:
               answer = input("Enter the correct answer to the question: ")
               if answer in options:#makes sure the correct answer is provided inside the options
                   break
               else:
                   print("Please enter as your correct answer one of your previous options")
                   
           questions.append({'question': question, 'options': options, 'answer': answer})
       
       self.quiz_list.append({self.title: questions})
       
       
          
        
    def start_create(self): #calls the methods needed in order
        print("You will be able to create your own quiz with a lot of freedom and possibility of customizing")
        time.sleep(2)
        self.enter() #calls detail()
        self.save_to_json() #first saves
        self.followup() #then this
    
