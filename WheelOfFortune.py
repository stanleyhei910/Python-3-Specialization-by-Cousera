# I believe this is the first long assignment in the specialization that learners might find it challenging.
# I will try to make comments to make these code more understandable

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    prizeMoney = 0
    prizes = []                                     #Create an empty list as a class variable. Such that all the instances of this class will have these variables. (Inherited class as well)
    
    def __init__(self, name):
        self.name = name
        # creating copies from the self.prizes list everytime we create a new instance.
        self.prizes = self.prizes[:]                # If we don't do this, any changes to the class variable: WOFplayer.prizes will affect all the instances of the class. (Remember shallow copy and deep copy)
    
    def addMoney(self, amt):
        self.prizeMoney += int(amt)
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)        # Use formatted string to return the result
    
    
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscuredPhrase, guessed):           #The only purpose of this function is to get the input from users(Human), we supposed the HumanPlayer knows the rules to the gameplay
        move = input()
        return move

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE" # Creating a class variable
    
    def __init__(self, name, diff):
        WOFPlayer.__init__(self, name)          # Use class inheritance so that we don't have to type it all over again.
        self.difficulty = diff                  # This is a new instance variable
    
    def smartCoinFlip(self):
        randnum = random.randint(1,10)          # Remember here: don't call random.randint more than 1 time, because everytime you invoke the function, it generates a new rand. num.
        if randnum > self.difficulty:           # if randnum is larger than self.difficulty, it is a GOOD move, else: it is a BAD move
            return True
        else: 
            return False
    
    def getPossibleLetters(self, guessed):
        # Use list comprehension to create a lst of letters for later to return
        lst_letters = [ch for ch in self.SORTED_FREQUENCIES if ch not in guessed]           # Here I combined it with a conditional statements. 
        if self.prizeMoney < 250:               # Another condition.
            for ch in VOWELS:
                try:                            # As ch might not be in lst_letters (It is guessed already). We use a try and except here.
                    lst_letters.remove(ch)      # If the COMPlayer has less than 250, remove VOWELS letters from the list so that it cannot be return.
                except:                         # You can be more specific to which type of errors you want to catch, read the documentations.
                    continue                    # If ch not in lst_letters, do the next ch.
        return lst_letters
    
    def getMove(self, category, obscuredPhrase, guessed):
        goodOrBad = self.smartCoinFlip()        # Creating a variable to store the Bool
        lst_letters = self.getPossibleLetters(guessed)
        if len(lst_letters) == 0:
            return "pass"
        else:
            if goodOrBad == True:
                return lst_letters[-1]          # As the list is sorted already, you can just return the last letter in the list
            else:
                return random.choice(lst_letters)
