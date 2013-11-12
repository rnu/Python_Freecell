  ##################################################################
  #  Section 3
  #  Computer Project #8
  ##################################################################
 #  Algorithm
#    1.Call main()
#    2. Build game board
#    3. Print Gameboard()
#    4. Ask user input.
#    5. Validate user move
#    6. Perform user move, check if user won.
#    7. Repeat til user wins.


import cards
from string import punctuation

class Game( object ):
    suit_list = ['x','Clubs(1)','Diamonds(2)','Hearts(3)','Spades(4)']
    """
    Builds deck of cards, shuffles deck, initialize board dictionaries (tableau, cell, foundation), build tableaus.
    Receive: self
    Return: None

    Algorithm:
    1. Build Deck of cards.
    2. Shuffle cards.
    3. Initialize tab, cell, foundation dictionaries.
    4. Build tableaus
    5. Print help()
    """
    def __init__(self):
        #Build deck
        self.__deck = cards.Deck()
        #Shuffle deck
        self.__deck.shuffle()
        #Build Tableau, Cell and Foundation dictionaries
        self.__tab_dic={}
        self.__cell_dic={1:[],2:[],3:[],4:[]}
        self.__foundation_dic={1:[],2:[], 3:[],4:[]}
        #Build board
        self.build_Tab()
        #Print options
        self.help()
    """
    Returns None
    Receive: self
    Return: None
    """
    def __str__(self):
        return None
    """
    Returns None
    Receive: self
    Return: None
    """
    def __repr__(self):
        return None
    """
    Builds the individual tableaus.
    
    Receive: self
    Return: None

    1. Build 8 indexes for __tab_dic
    2. Populate each index with card using cards.Deck.deal()
    """
    def build_Tab(self):
        i=1
        #Build 8 Tableaus
        while i<9:
            self.__tab_dic[i]=[]
            #Add 7 cards to the first 4
            if len(self.__tab_dic)<5:
                t=0
                while t<7:
                    self.__tab_dic[i].append(self.__deck.deal())
                    t+=1
            else:
                t=0
                #Add 6 cards to the last tableaus
                while t <6:
                    self.__tab_dic[i].append(self.__deck.deal())
                    t+=1   
            i+=1
        return None
    """
    Prints current state of board
    
    Receive: self
    Return: None

    Algorithm:
    1. Print orientation directions, along with contents of tableaus
    2. Prints contents of cells.
    3. prints contents of foundations.
    """   
    def print_Board(self):
       #Print tableau
        print(" "*3,"Top", "\t"*2, "Bottom")
        for k,v in self.__tab_dic.items():
            print("{}. {}".format(k,v))
        #Print Cells
        print("-"*7+ " Cells")
        for k,v in self.__cell_dic.items():
            if len(v) == 0:
                print("Cell {}: Empty".format(k))
            else:
                print("Cell {}: {}".format(k,v))
        #Print Foundation
        print("-"*7+ " Foundation")
        for k,v in self.__foundation_dic.items():
            if len(v) == 0:
                print("{}: Empty".format(self.suit_list[k]))
            else:
                print("{}: {}".format(self.suit_list[k],v))
        print("\n\n")
        return None
    """
    Transfers card from tableau to tableau.
    
    Receive: self, tab_from, tab_to
    Return: None

    Algorithm:
    1. Pop the last card off tab_from.
    2. Pop the last card off tab_to.
    3. Check if they match in suit or rank, if they do it is an invalid move.
    4. Checks if the from_card is black and to_card is red (vice versa) and that the difference in rank is one.
    5. Append cards to approiate tableau.
    """
    def __t2t(self, tab_from ,tab_to):
         #Try to pop cards from tab
        from_card = ''
        to_card = ''
        
        from_card = self.__tab_dic[tab_from].pop()
        to_card = self.__tab_dic[tab_to].pop()
        #If tableau is empty, append
        if(len(self.__tab_dic[tab_to])==0):
                self.__tab_dic[tab_to].append(from_card)
                return
        #If ranks match, invalid move
        if(from_card.get_rank() == to_card.get_rank()):
            self.__tab_dic[tab_to].append(to_card)
            self.__tab_dic[tab_from].append(from_card)
            print("Invalid Move")
            return
        else:
            None
        #If suits match, invalid move
        if(from_card.get_suit() == to_card.get_suit()):
            self.__tab_dic[tab_to].append(to_card)
            self.__tab_dic[tab_from].append(from_card)
            print("Invalid Move")
            return
        else:
            None  
        #If from_card is black and to_card is red, and the difference is one, append
        if (from_card.get_suit() in [1,4]) and (to_card.get_suit() in [2,3]):
            if(to_card.get_rank() - from_card.get_rank())==1:
                self.__tab_dic[tab_to].append(to_card)
                self.__tab_dic[tab_to].append(from_card)
            else:
                pass
        #If from_Card is red and to_card is black, and the difference is one, append.
        elif (from_card.get_suit() in [2,3]) and (to_card.get_suit() in [1,4]):
            if(to_card.get_rank() - from_card.get_rank())==1:
                self.__tab_dic[tab_to].append(to_card)
                self.__tab_dic[tab_to].append(from_card)
            else:
                pass
        else:
            self.__tab_dic[tab_to].append(to_card)
            self.__tab_dic[tab_from].append(from_card)
            print("Invalid Move")
    """
    Transfers card from tableau to cell.
    
    Receive: self, tab, cell
    Return: None

    Algorithm:
    1. Pop the last card off tab
    2. Pop the last card off cell
    3. If there isn't a card in self.__cell_dic, than append.
    4. If there is a card in self.__cell_dic, invalid move.
    """
    def __t2c(self, tab, cell):
        if len(self.__cell_dic[cell]) == 0:
            self.__cell_dic[cell].append(self.__tab_dic[tab].pop())
        else:
            print("Invalid move\n")

    """
    Transfers card from tableau to foundation.
    
    Receive: self, tab, found
    Return: None

    Algorithm:
    1. Pop the last card off tab.
    2. Pop the last card off foundation.
    3. If the suit of the tableau card doesn't match the foundation, invalid move.
    4. If the foundation is empty, and card is an Ace, append.
    5. If the found has a card, and the difference in ranks is 1, append.
    """  
    def __t2f(self, tab, found):
        #Tableau card (tab_card)
        try:
            tab_card = self.__tab_dic[tab].pop()
        except IndexError:
            print("There is not a card here.\n")
        #If tab_card suit and 'found' don't match, return tab_card to tableau and send an error.
        if tab_card.get_suit() != found:
                self.__tab_dic[tab].append(tab_card)
                print("Error, Sent card to wrong foundation\n")
                return
        #If foundation has a card pop it.
        if len(self.__foundation_dic[found])!= 0:
                f_card = self.__foundation_dic[found].pop()
        #If it doesn't, create one.
        else:
                f_card = cards.Card()
        #If foundation is empty and tab_card is an Ace, append
        if (len(self.__foundation_dic[found])== 0) and (tab_card.get_rank() == 1):
                self.__foundation_dic[found].append(tab_card)
        #If foundation has card and the difference in values is 1, append. 
        elif tab_card.get_rank() != 1 and (tab_card.get_rank() - f_card.get_rank()) == 1:
                self.__foundation_dic[found].append(tab_card)
        #If all test fail, append tab_card back to tableau and report error
        else:
                self.__tab_dic[tab].append(tab_card)
                self.__foundation_dic[found].append(f_card)
                print("Invalid move...\n")
    """
    Transfers card from cell to tableau.
    
    Receive: self, cell, tab
    Return: None

    Algorithm:
    1. Pop the last card off tab.
    2. Pop the last card off cell.
    3. Check if they match in suit or rank, if they do it is an invalid move.
    4. Checks if the cell_card is black and tab_card is red (vice versa) and that the difference in rank is one.
    5. Append cards to approiate tableau.
    """		
    def __c2t(self,cell,tab):
        #Try to pop cards from cell 
        try:
            cell_card = self.__cell_dic[cell].pop()
            tab_card = self.__tab_dic[tab].pop()

            #if cards have same rank, don't append
            if(cell_card.get_rank() == tab_card.get_rank()):
                self.__tab_dic[tab].append(tab_card)
                self.__cell_dic[cell].append(cell_card)
                print("Invalid Move")
                return
            #If cards have same suit, don't append
            if(cell_card.get_suit() == tab_card.get_suit()):
                self.__tab_dic[tab].append(tab_card)
                self.__cell_dic[cell].append(cell_card)
                print("Invalid Move")
                return
            #If tableau is empty, append
            if(len(self.__tab_dic[tab])==0):
                self.__tab_dic[tab].append(cell_card)
                return
           #If cell_card is black and tab_card is red, and the difference is one, append
            if (cell_card.get_suit() in [1,4]) and (tab_card.get_suit() in [2,3]):
                if(tab_card.get_rank() - cell_card.get_rank())==1:
                    self.__tab_dic[tab].append(tab_card)
                    self.__tab_dic[tab].append(cell_card)
                else:
                    pass
            #If cell_card is red and tab_card is black, and the difference is one, append.
            elif (cell_card.get_suit() in [2,3]) and (tab_card.get_suit() in [1,4]):
                if(tab_card.get_rank() - cell_card.get_rank())==1:
                    self.__tab_dic[tab].append(tab_card)
                    self.__tab_dic[tab].append(cell_card)
                else:
                    pass
            else:
                self.__tab_dic[tab].append(tab_card)
                self.__cell_dic[cell].append(cell_card)
                print("Invalid Move")
        except (IndexError, UnboundLocalError):
            print("Card not found")
    """
    Transfers card from cell to foundation.
    
    Receive: self, cell, found
    Return: None

    Algorithm:
    1. Pop the last card off foundation.
    2. Pop the last card off cell.
    3. If the suit of the cell card doesn't match the foundation, invalid move.
    4. If the foundation is empty, and card is an Ace, append.
    5. If the found has a card, and the difference in ranks is 1, append.
    """	
    def __c2f(self, cell, found):
        #cell card (cell_card)
        try:
            cell_card = self.__cell_dic[cell].pop()
        except IndexError:
            print("There is not a card here.\n")
        #If cell_card suit and 'found' don't match, return cell_card to cell and send an error.
        if cell_card.get_suit() != found:
                self.__cell_dic[cell].append(cell_card)
                print("Error, Sent card to wrong foundation\n")
                return
        #If foundation has a card pop it.
        if len(self.__foundation_dic[found])!= 0:
                f_card = self.__foundation_dic[found].pop()
        #If it doesn't, create one.
        else:
                f_card = cards.Card()
        #If foundation is empty and cell_card is an Ace, append()
        if len(self.__foundation_dic[found])== 0 and (cell_card.get_value() == 1):
                self.__foundation_dic[found].append(cell_card)
        #If foundation has card and the difference in values is 1, append. (As long as cell_card isn't an Ace(1))
        elif cell_card.get_rank() != 1 and (cell_card.get_rank() - f_card.get_rank()) == 1:
                self.__foundation_dic[found].append(cell_card)
        #If all test fail, append cell_card back to cell and report error
        else:
                self.__cell_dic[cell].append(cell_card)
                self.__foundation_dic[found].append(f_card)
                print("Invalid move...\n")
    """
    Ask for user input and makes approiate actions. (Menu)
    
    Receive: self
    Return: None, (or read_player() if input isn' t correct)

    Algorithm:
    1. Ask user for input.
    2. Split user input into a list.
    3. Check user input for correct function.
    4. Ask again if user input isn't correct.
    """	
    def read_player(self):
        #Format player's input
        temp = input("Which move would you like to make\n")
        temp = temp.lower()
        temp = ''.join(ch for ch in temp if ch not in punctuation)
        choice = temp.split()
        
        #Quit -- Not working!!!!!!!!!!!!!
        if len(choice) != 3:
            if choice[0] in ['help', 'h']:
                self.help()
            elif choice[0] in ['q','quit']:
                return 'q'
            elif choice[0] in ['c']:
                self.cheat()
            else:
                print("Choice not found")
                return self.read_player()
        #T2T
        elif choice[0] in ['t2t']:
            self.__t2t(int(choice[1]), int(choice[2]))

        #T2C
        elif choice[0] in ['t2c']:
            self.__t2c(int(choice[1]), int(choice[2]))

        #T2F
        elif choice[0] in ['t2f']:
            self.__t2f(int(choice[1]), int(choice[2]))

        #C2T
        elif choice[0] in ['c2t']:
            self.__c2t(int(choice[1]), int(choice[2]))

        #C2F
        elif choice[0] in ['c2f']:
            self.__c2f(int(choice[1]), int(choice[2]))

        #Non-valid choice
        else:
            print("Choice not found")
            return self.read_player()
    """
    Print instructions
    
    Receive: self
    Return: None

    Algorithm:
    1.Print instructions
    """	        
    def help(self):
        print("*"*10)
        print("t2t tableau1 tableau2 (Tableau to Tableau)\n"\
              "t2c tableau cell (Tableau to Cell)\n"\
              "t2f tableau foundation (Tableau to Foundation\n"\
              "c2t cell tableau (Cell to Tableau)\n"\
              "c2f cell foundation (Cell to Foundation)\n"\
              "h (Help)\n"\
              "q (Quit)")
        print("*"*10,"\n")
        
    """
    Check if user has won.
    
    Receive: self, temp
    Return: has_won

    Algorithm:
    1. For every king in foundation, add won to has_won.
    2. 'q' automatically sets has_won to 5, to exit program.
    """	
    def game_Won(self, temp = 0):
        #If foundations all have Aces, game has been won
        has_won = 0
        for k,v in self.__foundation_dic.items():
            if len(v) != 0:
                #If top card is a King
                if v[0].get_rank() == 13:
                    has_won +=1
                else:
                    pass
        if temp > 0:
            has_won = temp
            print("Good Bye")
        return has_won
    """
    Debug function. Cheater.
    
    Receive: self
    Return: has_won

    Algorithm:
    1. It's called.
    2. It wins. (By setting foundation to all kings.)
    """	
    def cheat(self):
        for k,v in self.__foundation_dic.items():
            newCard = cards.Card(rank = 13, suit = k)
            self.__foundation_dic[k].append(newCard)

            
                 
###
"""
Main game cycle

Receive: None
Return: None

Algorithm:
1. Initialize game.
2. Loop through test.print_Board() and test.read_player()
"""
def main():
    #Initialize board
    test  = Game()

    while test.game_Won() < 4:
        test.print_Board()
        if test.read_player() == 'q':
            break
    print("You won!")
    
main()      

    

        

