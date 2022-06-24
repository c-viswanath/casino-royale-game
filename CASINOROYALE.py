import time,sys,os
CREDITS=5000
wins = 0
losses = 0
x='''  _____           _____ _____ _   _  ____    _____   ______     __      _      ______ 
 / ____|   /\    / ____|_   _| \ | |/ __ \  |  __ \ / __ \ \   / //\   | |    |  ____|
| |       /  \  | (___   | | |  \| | |  | | | |__) | |  | \ \_/ //  \  | |    | |__   
| |      / /\ \  \___ \  | | | . ` | |  | | |  _  /| |  | |\   // /\ \ | |    |  __|  
| |____ / ____ \ ____) |_| |_| |\  | |__| | | | \ \| |__| | | |/ ____ \| |____| |____ 
 \_____/_/    \_\_____/|_____|_| \_|\____/  |_|  \_\\____/  |_/_/    \_\______|______|
'''
def typewritermessage(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.00001)
    time.sleep(0.0001)   
    print()
typewritermessage(x) 
def BLACKJACK():
    import os
    import random
    import sys
    import time
    global wins
    global losses
    
    #text animation typewriter
    def typewritermessage(text):
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)   
        print()
    
    message_rules_1="Want To Play In The Blackjack Table?"
    typewritermessage(message_rules_1)
    
    username=input("Enter Your Name:")
    a="BLACKJACK"
    if type(username)==type(a):
        message_hi="HELLO  " + username.capitalize()  
        print(message_hi)
        message_rules='''1.The goal of blackjack is to beat the dealer's hand without going over 21.
    2.Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
    3.Each player starts with two cards, one of the dealer's cards is hidden until the end.
    4.To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
    5.If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
    6.If you are dealt 21 from the start (Ace & 10), you got a blackjack.
    7.Blackjack usually means you win 1.5 the amount of your bet.
    8.Dealer will hit until his/her cards total 17 or higher.
    9.Doubling is like a hit, only the bet is doubled and you only get one more card.
    Values Of Cards Are As Follows:
    1.All JACKS,KINGS AND QUEENS HAVE A VALUE OF 10 POINTS
    2.ALL NUMBER CARDS HAVE A VALUE CORRESPONDING TO THEIR NUMBER
    3.THE VALUE OF ACES WILL BE DECIDED BY THE COMPUTER EITHER 1 OR 11'''
        print(message_rules)               
    
    decks = input("Enter number of decks to use: ")
    # user chooses number of decks of cards to use
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)
    

   # initialize scores
   #initialize credits

    
    def deal(deck):
        hand = []
        for i in range(2):
            random.shuffle(deck)
            card = deck.pop()
            if card == 11:card = "J"
            if card == 12:card = "Q"
            if card == 13:card = "K"
            if card == 14:card = "A"
            hand.append(card)
        return hand
    
    def play_again():
        again = input("Do you want to play again? (Y/N) : ").lower()
        print("CREDITS LEFT=",CREDITS)
        if CREDITS==0:
            print("INSUFFICIENT CREDITS LEFT!")
            print("THANK YOU FOR PLAYING THE GAME!")
            sys.exit()
        if again == "y":
            bet=int(input("ENTER THE AMOUNT YOU WANT TO BET:"))
            if bet<=CREDITS:
                dealer_hand = []
                player_hand = []
                deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
                game()
        else:
            print("Bye!")
            print("CREDITS LEFT=",CREDITS)
            sys.exit()
    
    def total(hand):
        total = 0
        for card in hand:
            if card == "J" or card == "Q" or card == "K":
                total+= 10
            elif card == "A":
                if total >= 11: total+= 1
                else: total+= 11
            else: total += card
        return total
    
    def hit(hand):
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
        return hand
    
    def clear():
        if os.name == 'nt':
            os.system('CLS')
        if os.name == 'posix':
            os.system('clear')
    
    def print_results(dealer_hand, player_hand):
        clear()
    
        print("\n    WELCOME TO BLACKJACK!\n")
        print("-"*30+"\n")
        print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
        print("-"*30+"\n")
        print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    
    def blackjack(dealer_hand, player_hand):
        global wins
        global losses
        global CREDITS
        global bet
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Congratulations! You got a Blackjack!\n")
            wins += 1
            CREDITS+=bet
            play_again()
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry, you lose. The dealer got a blackjack.\n")
            losses += 1
            CREDITS=CREDITS-bet
            play_again()
    
    def score(dealer_hand, player_hand):
            # score function now updates to global win/loss variables
            global wins
            global losses
            global CREDITS
            global bet
            if total(player_hand) == 21:
                print_results(dealer_hand, player_hand)
                print ("Congratulations! You got a Blackjack!\n")
                wins += 1
                CREDITS=CREDITS+bet
            elif total(dealer_hand) == 21:
                print_results(dealer_hand, player_hand)
                print ("Sorry, you lose. The dealer got a blackjack.\n")
                losses += 1
                CREDITS=CREDITS-bet
            elif total(player_hand) > 21:
                print_results(dealer_hand, player_hand)
                print ("Sorry. You busted. You lose.\n")
                losses += 1
                CREDITS=CREDITS-bet
            elif total(dealer_hand) > 21:
                print_results(dealer_hand, player_hand)
                print ("Dealer busts. You win!\n")
                wins += 1
                CREDITS=CREDITS+bet
            elif total(player_hand) < total(dealer_hand):
                print_results(dealer_hand, player_hand)
                print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
                losses += 1
                CREDITS=CREDITS-bet
            elif total(player_hand) > total(dealer_hand):
                print_results(dealer_hand, player_hand)
                print ("Congratulations. Your score is higher than the dealer. You win\n")
                wins += 1
                CREDITS=CREDITS+bet
    
    def game():
        global wins
        global losses
        global CREDITS
        global bet
        choice = 0
        clear()
        print("\n    WELCOME TO BLACKJACK!\n")
        print("-"*30+"\n")
        print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
        print("-"*30+"\n")
        bet=int(input("ENTER THE AMOUNT YOU WANT TO BET:"))
        dealer_hand = deal(deck)
        player_hand = deal(deck)
        print ("The dealer is showing a " + str(dealer_hand[0]))
        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        quit=False
        while not quit:
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
            if choice == 'h':
                hit(player_hand)
                print(player_hand)
                print("Hand total: " + str(total(player_hand)))
                if total(player_hand)>21:
                    print('You busted')
                    losses += 1
                    CREDITS=CREDITS-bet
                    play_again()
            elif choice=='s':
                while total(dealer_hand)<17:
                    hit(dealer_hand)
                    print(dealer_hand)
                    if total(dealer_hand)>21:
                        print('Dealer busts, you win!')
                        wins += 1
                        CREDITS=CREDITS+bet
                        play_again()
                score(dealer_hand,player_hand)
                play_again()
            elif choice == "q":
                print("Bye!")
                quit=True
                sys.exit()
    
    
    if __name__ == "__main__":
       game()
def SLOTMACHINE():
    import random
    import sys, time
    name=input("Enter Your Name:")
    name1='Hello '+name.capitalize()
    typewritermessage1(name1)
    
    #game variables

    BET = 0
    SCORE = 0
    
    
    #function to draw slot machine
    #i know its cool :0
    def slot(x,y,z):
        print("\n")
        print("+---------------------------------------+")
        print("|         $$$  SLOT MACHINE $$$		|")
        print("+-------+-------+-------+-------+-------+")
        print("|   S	| ^^^^^	| ^^^^^	| ^^^^^ |   P	|")
        print("|   P	|   {0}	|   {1}	|   {2}	|   L	|".format(x,y,z))
        print("|   I	| .....	| .....	| .....	|   A	|")
        print("|   N	| =====	| =====	| =====	|   Y	|")
        print("+-------+-------+-------+-------+-------+")
        print("	\___WIN CASH WIN CASH___/")
        print("\n")
    
    
    
    #fucnction for animating slot in the terminal
    def slotAnimaiton(a,b,c):
        ct = 2
        while ct >= 0:
            text = "SPINNING SPINNING ........"
            textAnimation(text)
    
            if ct == 2:
                # time fucntion to wait and draw at random intervals
                time.sleep(random.randint(1,5)/10)
                slot(a,"?","?")
                ct-=1
            elif ct == 1:
                time.sleep(random.randint(1, 5)/10)
                slot(a,b,"?")
                ct-=1
            elif ct ==0:
                time.sleep(random.randint(1, 5)/10)
                slot(a,b,c)
                ct-=1
    
    
    # fucntion to animate text like mission impossible xD
    def textAnimation(msg):
    
        for i in msg:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.01)
    
        print()
    
    
    # the name is suggestive enough.....
    
    INSTRUCTION_MSG = """
    So you wish to test your skills in the slot machine
    Alright then, but first keep this in mind.
    
    Here are the rules champ:-
    
    1. The only time you win is when all the slots show same value, that is from 0 to 5.
       Yes, you read that right, i.e from 0 to 5. You have a higher chance of winning.
    
    2. If you happen to get three 0s or three 5s, you have won the jackpot, you earn a total of 2000 credits and 
       twice the amount of money you have bet.
    
    3. If you get any other numbers other than mentioned above, then the amount you have betted will be added your credits.
    
    4. Any type of foul play/ illegal methods will not be tolerated and will lead to disqualification.
    
    5. Last but not least, enjoy the game and max out your luck stats.
    
    HAPPY GAMBLING :) 
    """
    # a menu which will appear every time...
    
    OPTION_MENU = ("""
     When prompt appears please enter the options as required.
    
        -:OPTIONS:-
    
     1. To set the bet amount.
     2. To spin the slot machine
     3. To read the instructions
     4. To show stats / credit balance
     5. To quit / go to main menu
    """)
    
    
    # function will show the amount to be bet and total credits...
    def showStats():
        print()
        print("|>> AMOUNT TO BET:{0}     TOTAL CREDITS:{1}    SCORE:{2} <<|".format(BET,CREDITS,SCORE))
        print()
    
    
    #function to check the result if the player has won or not and give him rewards
    def result(x,y,z):
        global CREDITS,BET,SCORE
        
        if x == y ==z == 5 or x == y == z == 0:
            print("HURRAY!!! ~~`")
            print("YOU WON THE JACKPOT")
            CREDITS += 2000 + (BET*2)
            print("YOU JUST WON",CREDITS , "credits.")
            print("Enter 4 to view your credit balance.")
            SCORE+= 5000
    
        elif x==y==z:
            print("HURRAY!! ~~~")
            print("YOU WON")
            CREDITS+=BET
            print(BET, "credits have been added to your account.")
            SCORE+= 2000
    
        else:
            CREDITS -=BET
            print("Tough luck!!")
            print("Let's give it another shot.")
     
    #main proogram
    def game():
        global CREDITS,BET,SCORE
    
        textAnimation(INSTRUCTION_MSG)
        #note windows mein os.system("cls") use karna linux mein main os.system("clear") use kiya hun
    
        while CREDITS > 0:
            print(OPTION_MENU)
            user_input = int(input("~PROMT:- Please enter your choice:- "))
            if user_input == 1:
                os.system("cls")
                BET = int(input("~PROMPT:- Please enter the bet amount:- "))
            elif user_input ==2:
                os.system("cls")
                if BET == 0:
                    print("Please enter a bet amount before proceeding.")
                elif BET > CREDITS:
                    print("Low credit balance....")
                    print("Please decrease the bet amount...")
                else:
                    a = random.randint(0, 5)
                    b = random.randint(0, 5)
                    c = random.randint(0, 5)
                    slotAnimaiton(a,b,c)
                    result(a,b,c)
            elif user_input == 3:
                os.system("cls")
                print(INSTRUCTION_MSG)
            elif user_input == 4:
                os.system("cls")
                showStats()
            elif user_input == 5:
                os.system("cls")
                showStats()
                print("SAYONARA!!")
                sys.exit()
            else:
                os.system("cls")
                print("The user entered option is invalid....")
                print("Please try again")
    
        # end credits message to player
        if CREDITS <= 0:
            time.sleep(2)
            
            os.system("clear")
            showStats()
    
    
            ENDING_MSG1 = "Oops you have exhausted your credit score..."
            SCORE_MSG = "YOUR TOTAL SCORE IS " + str(SCORE)
        
            ENDING_MSG2 = """
    Well played champ
    Hope we see you again!! And until then,
    HAPPY GAMBLING!!! ;)
        """
            #animation for the ending credits msg
            textAnimation(ENDING_MSG1)
            textAnimation(SCORE_MSG)
            textAnimation(ENDING_MSG2)
    
    
    #running the program
    if __name__ == "__main__":
        game()
x='''WELCOME TO CASINO ROYALE...Here's a hearty welcome, big and warm enough to encompass you! To say we are thrilled to see you is an understatement.
This Is A Premium Game Of Casino , Which includes TWO Games..
1.BLACKJACK
2.SLOT MACHINE '''
def typewritermessage1(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)   
    print()
typewritermessage1(x)
y=0
text='''
_   _   _   _   _        _   _   _   _
 / \ / \ / \ / \ / \    / \ / \ / \  
( T | H | A | N | K |  ( Y | O | U | 
 \_/ \_/ \_/ \_/ \_/    \_/ \_/ \_/
-   -   -  -  - -    - - - -    - - - - 
'''
while y==0:    
    x=int(input("TO PLAY BLACKJACK ENTER 1 , TO PLAY SLOT MACHINE ENTER 2 , TO QUIT ENTER 3: "))
    if x==1:
        BLACKJACK()
    if x==2:
        SLOTMACHINE()
    if x==3:
        typewritermessage(text)
        sys.exit()
