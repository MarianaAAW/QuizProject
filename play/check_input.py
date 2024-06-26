import time
#Class with the methods that check that the inputs are specifically what the code needs 
#All methods of this class do basically the same, a loop that only stops until the input is correct
class Check:
    
    def __init__(self): #init all attributes to none
        self.item = None 
        self.resp = None
        self.check_in = None
        self.p = None

    
    def error(self, check_in , valid_ans=[]): #checks inputs are what expected(valid_ans)
        self.resp = input(check_in)
        while True:
            if self.resp.lower() in valid_ans :
                return self.resp
            else:
                  self.resp = input(f"\nPlease enter {valid_ans} as your answer: ") 
                  
                  
    def error_act(self, valid_ans): #checks and follows a message and an action 
        while True:
            if self.item.lower() in valid_ans:
                message, action = valid_ans [self.item.lower()]
                print(message)
                action()
                return self.item
            else:
                k_valid_ans = list(valid_ans.keys())
                self.item = input(f"\nPlease enter {k_valid_ans} as your answer: ")
                
                
    def mandatory(self, prompt): #makes sure is not empty
        while True:
            self.p = input(prompt)
            if len(self.p) == 0:
                print("This cannot be empty")  
            else:
                return self.p


    def interger(self,to_check): #an integer needed as input
        while True:
            try :
                to_check = int(to_check)
                return to_check
            except :
                print("Your answer needs to be a valid integer")
                time.sleep(1)
                to_check = input("Please enter a number as your answer:")
