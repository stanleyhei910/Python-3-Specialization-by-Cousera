# I believe this is the first long assignment in the specialization that learners might find it challenging.
# I will try to make comments to make these code more understandable

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    prizeMoney = 0
    prizes = []
    
    def __init__(self, name):
        self.name = name
        self.prizes = self.prizes[:]
    
    def addMoney(self, amt):
        self.prizeMoney += int(amt)
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
    
    
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscuredPhrase, guessed):
        move = input()
        return move

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
    
    def __init__(self, name, diff):
        WOFPlayer.__init__(self, name)
        self.difficulty = diff
    
    def smartCoinFlip(self):
        randnum = random.randint(1,10)
        if randnum > self.difficulty:
            return True
        else:
            return False
    
    def getPossibleLetters(self, guessed):
        lst_letters = [ch for ch in self.SORTED_FREQUENCIES if ch not in guessed]
        if self.prizeMoney < 250:
            for ch in VOWELS:
                try:
                    lst_letters.remove(ch)
                except:
                    continue
        return lst_letters
    
    def getMove(self, category, obscuredPhrase, guessed):
        goodOrBad = self.smartCoinFlip()
        lst_letters = self.getPossibleLetters(guessed)
        if len(lst_letters) == 0:
            return "pass"
        else:
            if goodOrBad == True:
                return lst_letters[-1]
            else:
                return random.choice(lst_letters)
