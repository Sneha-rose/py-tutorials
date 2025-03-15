from breezypythongui import EasyFrame
import random
class GuessingGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Guessing Game")

        self.num=random.randint(1,100)
        self.count=0

        greet="Guess a no. btw 1 and 100"
        self.hintLabel=self.addLabel(text=greet,row=0,column=0,sticky="NSEW",columnspan=2)

        self.addLabel(text="Your Guess",row=1,column=0)
        self.guessfield=self.addIntegerField(value=0,row=1,column=1)

        self.nextButton=self.addButton(text="Next Guess",row=2,column=0,command=self.nextG)
        self.newButton=self.addButton(text="New Game",row=2,column=1,command=self.newG)

    def nextG(self):
        self.count +=1
        guess=self.guessfield.getNumber()

        if guess==self.num:
            self.hintLabel["text"]="You've guessed in"+str(self.count)+"attempt!"
            self.nextButton["state"]="disabled"

        elif guess < self.num:
            self.hintLabel["text"]="Sorry, too small!"

        else:
            self.hintLabel["text"]="Sorry, too high!"

    def newG(self):
        self.num=random.randint(1,100)
        self.count=0
        greet="Guess a no. btw 1 and 100"
        self.hintLabel["text"]=greet
        self.nextButton["state"]="normal"

GuessingGame().mainloop()
