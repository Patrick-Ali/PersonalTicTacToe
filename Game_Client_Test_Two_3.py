# Help on fundamentals from http://christianthompson.com/node/40
# and https://inventwithpython.com/chapter10.html

import time

from random import *

import socket

import select

import sys

def Game():

     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     host = 'localhost'
     port = 12346
     client.connect((host, port))
    

     p = input("Do you want to play a game? Y for yes N for no: ")
     if p == "Y" or p == "y":

        PlayAgain = "Y"
        
        board = [""," "," "," "," "," "," "," "," "," "]
             
        while PlayAgain == "Y" or "y":         

            def SinglePlayerChoice():
                Player = input("Player do you want to be noughts or crossess, X or O, please use capitals ")
                Player.upper()
                if Player == "X" or Player == "x":
                    Player = "X"
                    Computer = "0"
                    CXFirst()
                    
                else:
                    Player = "O"
                    Computer = "X"
                    COFirst()

            def Choose():
                
                data = client.recv(1024)
                data = data.decode('utf-8').rstrip('\r\n')
                print(data)

                if data == 'You are O, please wait for player 1':
                    OSecond()
                    
                elif data == 'You are X, please wait for player 1':
                    XSecond() 

                mark = ' '

                if data == 'Player 2':
                    mark = client.recv(1024)
                    mark = mark.decode('utf-8').rstrip('\r\n')
                    print(mark)
                elif data == 'Player 1, Choose Marker, X or O':
                    msg = input('>')
                    client.send( msg.encode('utf-8') )
                    if msg == 'x':
                        XFirst()
                    elif msg == 'o':
                        OFirst()

                if mark == 'You are O, please wait for player 1':
                    XSecond()
                    
                elif mark == 'You are X, please wait for player 1':
                    OSecond()
                 

            def Mode():
                Mode = input("Do you want to play Multi-Player (M) or Single Player (S)")
                if Mode == "S" or Mode == "s":
                    SinglePlayerChoice()
                elif Mode == "M" or Mode == "m":
                    Choose()

            
            def Board ():
                w = '-------------'
                x = '   |   |'
                y = ' '
                z = '|'
                print (x.center(70))
                print (y.center(33) + board[1] + z.center(0) + board[2] + y.center(2) + z.center(0) + board[3])
                print (x.center(70))
                print (w.center(73))
                print (y.center(33) + board[4] + z.center(0) + board[5] + y.center(2) + z.center(0) + board[6])
                print (x.center(70))
                print (w.center(73))
                print (y.center(33) + board[7] + z.center(0) + board[8] + y.center(2) + z.center(0) + board[9])
                print (x.center(70))
            
            def Win(w):
            
                if  (board[7] == w and board[8] == w and board[9] == w) or \
                    (board[4] == w and board[5] == w and board[6] == w) or \
                    (board[1] == w and board[2] == w and board[3] == w) or \
                    (board[7] == w and board[4] == w and board[1] == w) or \
                    (board[8] == w and board[5] == w and board[2] == w) or \
                    (board[9] == w and board[6] == w and board[3] == w) or \
                    (board[7] == w and board[5] == w and board[3] == w) or \
                    (board[9] == w and board[5] == w and board[1] == w):
                        Board()
                        return "You win"
                else:
                    return



            def ComputerX():

                 for i in [1,2,3]:
                    if board[i] == "X" and board[i+3] == "X" and board[i+6] == " ":
                        return i+6
                    if board[i+3] == "X" and board[i+6] == "X" and board[i] == " ":
                        return i
                    if board[i] == "X" and board[i+6] == "X" and board[i+3] == " ":
                        return i + 3

                 for i in [1,4,7]:
                    if board[i] == "X" and board[i+1] == "X" and board[i+2] == " ":
                        return i+2
                    if board[i+1] == "X" and board[i+2] == "X" and board[i] == " ":
                        return i
                    if board[i] == "X" and board[i+2] == "X" and board[i+1] == " ":
                        return i+3
                    
                 for i in [1,2,3]:
                    if board[i] == "O" and board[i+3] == "O" and board[i+6] == " ":
                        return i+6
                    if board[i+3] == "O" and board[i+6] == "O" and board[i] == " ":
                        return i
                    if board[i] == "O" and board[i+6] == "O" and board[i+3] == " ":
                        return i + 3

                 for i in [1,4,7]:
                    if board[i] == "O" and board[i+1] == "O" and board[i+2] == " ":
                        return i+2
                    if board[i+1] == "O" and board[i+2] == "O" and board[i] == " ":
                        return i
                    if board[i] == "O" and board[i+2] == "O" and board[i+1] == " ":
                        return i+3
                    
                 for i in [1,5,9]:
                    if i == 1:
                        if board[i] == "X" and board[i+4] == "X" and board[i+8] == " ":
                            return i+8
                        if board[i+4] == "X" and board[i+8] == "X" and board[i] == " ":
                            return i
                        if board[i] == "X" and board[i+8] == "X" and board[i+4] == " ":
                            return i + 4
                    elif i == 5:
                        if board[i] == "X" and board[i-4] == "X" and board[i+4] == " ":
                            return i+4
                        if board[i-4] == "X" and board[i+4] == "X" and board[i] == " ":
                            return i
                        if board[i] == "X" and board[i+4] == "X" and board[i-4] == " ":
                            return i - 4
                    elif i == 9:
                        if board[i] == "X" and board[i-4] == "X" and board[i-8] == " ":
                            return i-8
                        if board[i-4] == "X" and board[i-8] == "X" and board[i] == " ":
                            return i
                        if board[i] == "X" and board[i-8] == "X" and board[i-4] == " ":
                            return i - 4
                        
                 for i in [3,5,7]:
                    if i == 3:
                        if board[i] == "X" and board[i+2] == "X" and board[i+4] == " ":
                            return i+4
                        if board[i+2] == "X" and board[i+4] == "X" and board[i] == " ":
                            return i
                        if board[i] == "X" and board[i+4] == "X" and board[i+2] == " ":
                            return i + 2
                    elif i == 5:
                        if board[i] == "X" and board[i-2] == "X" and board[i+2] == " ":
                            return i+2
                        if board[i-2] == "X" and board[i+2] == "X" and board[i] == " ":
                            return i
                        if board[i] == "X" and board[i+2] == "X" and board[i-2] == " ":
                            return i - 2
                    elif i == 7:
                        if board[i] == "X" and board[i-4] == "X" and board[i-2] == " ":
                            return i-2
                        if board[i-4] == "X" and board[i-2] == "X" and board[i] == " ":
                            return i
                        if board[i] == "X" and board[i-2] == "X" and board[i-4] == " ":
                            return i - 4
                        
                
                 if board[5] == " ":
                    return 5

                 AI = randint(1,9)
                    
                 if board[AI] == " ":
                    return AI
                 else:
                    ComputerX()

            def ComputerO():

                for i in [1,2,3]:
                    if board[i] == "O" and board[i+3] == "O" and board[i+6] == " ":
                        return i+6
                    if board[i+3] == "O" and board[i+6] == "O" and board[i] == " ":
                        return i
                    if board[i] == "O" and board[i+6] == "O" and board[i+3] == " ":
                        return i + 3

                for i in [1,4,7]:
                    if board[i] == "O" and board[i+1] == "O" and board[i+2] == " ":
                        return i+2
                    if board[i+1] == "O" and board[i+2] == "O" and board[i] == " ":
                        return i
                    if board[i] == "O" and board[i+2] == "O" and board[i+1] == " ":
                        return i+3

                for i in [1,2,3]:
                    if board[i] == "X" and board[i+3] == "X" and board[i+6] == " ":
                        return i+6
                    if board[i+3] == "X" and board[i+6] == "X" and board[i] == " ":
                        return i
                    if board[i] == "X" and board[i+6] == "X" and board[i+3] == " ":
                        return i + 3

                for i in [1,4,7]:
                    if board[i] == "X" and board[i+1] == "X" and board[i+2] == " ":
                        return i+2
                    if board[i+1] == "X" and board[i+2] == "X" and board[i] == " ":
                        return i
                    if board[i] == "X" and board[i+2] == "X" and board[i+1] == " ":
                        return i+3
                
                if board[5] == " ":
                    return 5

                AI = randint(1,9)
                
                if board[AI] == " ":
                   return int(AI)
                else:
                    return ComputerO()


            def X():

                choice = input("Please choose a square for X: ")
                choice = int(choice)

                if choice > 0 and choice <= 9:
                     if board[choice] == " ":
                        msg = choice
                        msg = str(msg)
                        print(msg)
                        client.send( msg.encode('utf-8') )
                        board[choice] = "X"
                     else:
                        print ("square already taken")
                        time.sleep(1)
                        print ("\n" * 50)
                        print(Board())
                        X()
                else:
                    X()

                if Win(board[choice]) == "You win":
                     return "You win"
                else:
                    return

            def CX():

                AI = int(ComputerO())
                AI = int(AI)

                if AI > 0 and AI <= 9:
                     if board[AI] == " ":
                        board[AI] = "X"
                     else:
                        print ("square already taken")
                        time.sleep(1)
                        print ("\n" * 50)
                        print(Board())
                        X()
                else:
                    X()

                if Win(board[AI]) == "You win":
                     return "You win"
                else:
                    return
                    
                
            def O():
                
                choice = input("Please choose a squar for O: ")
                choice = int(choice)

                if choice > 0 and choice < 10:
                    if board[choice] == " ":
                        msg = choice
                        msg = str(msg)
                        print(msg)
                        client.send( msg.encode('utf-8') )
                        board[choice] = "O"
                    else:
                        print ("square already taken")
                        time.sleep(1)
                        print ("\n" * 50)
                        print(Board())
                        O()
                else:
                    O()

                if Win(board[choice]) == "You win":
                     return "You win"
                else:
                    return
                
            def XS():

                choice = client.recv(1024)
                choice = choice.decode('utf-8').rstrip('\r\n')
                choice = int(choice)

                if choice > 0 and choice <= 9:
                     if board[choice] == " ":
                        board[choice] = "X"
                     else:
                        print ("square already taken")
                        time.sleep(1)
                        print ("\n" * 50)
                        print(Board())
                        X()
                else:
                    X()

                if Win(board[choice]) == "You win":
                     return "You win"
                else:
                    return
                 
                
            def OS():
                
                choice = client.recv(1024)
                choice = choice.decode('utf-8').rstrip('\r\n')
                choice = int(choice)

                if choice > 0 and choice < 10:
                    if board[choice] == " ":
                        board[choice] = "O"
                    else:
                        print ("square already taken")
                        time.sleep(1)
                        print ("\n" * 50)
                        print(Board())
                        O()
                else:
                    O()

                if Win(board[choice]) == "You win":
                     return "You win"
                else:
                    return

            def CO():

                AI = int(ComputerX())
                AI = int(AI)
                
                if AI > 0 and AI < 10:
                    if board[AI] == " ":
                        board[AI] = "O"
                    else:
                        print ("square already taken")
                        time.sleep(1)
                        print ("\n" * 50)
                        print(Board())
                        O()
                else:
                    O()

                if Win(board[AI]) == "You win":
                     return "You win"
                else:
                    return


                   
            def XFirst():

                Round = 1

                while Round <= 5 :
                    print ("\n" * 50)
                    print ("This is Round: " + str(Round))
                    Board()

                    if Round == 5:            
                        if X() == "You win":
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("You Win")
                             Game()
                        else:
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("It's a Tie")
                             Game()
                    

                    if X() == "You win":
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        print ("Player X wins")
                        Game()
                    else:
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        if OS() == "You win":
                            print ("\n" * 50)
                            print ("This is Round: " + str(Round))
                            Board()
                            print ("Player O wins")
                            Game()
                        else:
                            Round = Round + 1
                            

            def OFirst():

                Round = 1
                
                while Round <= 5 :

                    print ("\n" * 50)

                    print ("This is Round: " + str(Round))

                    Board()

                    if Round == 5:
                       if O() == "You win":
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("You Win")
                             Game()
                       else:
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("It's a Tie")
                             Game()       

                    if O() == "You win":
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        print ("Player O wins")
                        Game()
                    
                    else:
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        
                        if XS() == "You win":
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("Player X wins")
                             Game()
                        else:
                            Round = Round + 1

            def XSecond():

                Round = 1

                while Round <= 5 :
                    print ("\n" * 50)
                    print ("This is Round: " + str(Round))
                    Board()
                    
                    if Round == 5:            
                        if XS() == "You win":
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("You Win")
                             Game()
                        else:
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("It's a Tie")
                             Game()
                    

                    if XS() == "You win":
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        print ("Player X wins")
                        Game()
                    else:
                        
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        if O() == "You win":
                            print ("\n" * 50)
                            print ("This is Round: " + str(Round))
                            Board()
                            print ("Player O wins")
                            Game()
                        else:
                            Round = Round + 1
                            

            def OSecond():

                Round = 1
                
                while Round <= 5 :

                    print ("\n" * 50)

                    print ("This is Round: " + str(Round))

                    Board()

                    if Round == 5:
                        if OS() == "You win":
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("You Win")
                             Game()
                        else:
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("It's a Tie")
                             Game()       

                    if OS() == "You win":
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        print ("Player O wins")
                        Game()
                    
                    else:
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        
                        if X() == "You win":
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("Player X wins")
                             Game()
                        else:
                            Round = Round + 1

            def CXFirst():

                Round = 1

                while Round <= 5 :

                    print ("\n" * 50)

                    print ("This is Round: " + str(Round))

                    Board()

                    if Round == 5:            
                         if X() == "You win":
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("You Win")
                             Game()
                             
                         else:
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("It's a Tie")
                             Game()
                    

                    if X() == "You win":
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        print ("Player X wins")
                        Game()
                    else:
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        
                        if CO() == "You win":
                            print ("\n" * 50)
                            print ("This is Round: " + str(Round))
                            Board()
                            print ("Computer wins")
                            Game() 
                        else:
                            Round = Round + 1
                            

            def COFirst():

                Round = 1
                
                while Round <= 5 :

                    print ("\n" * 50)

                    print ("This is Round: " + str(Round))

                    Board()

                    if Round == 5:
                       if O() == "You win":
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("You Win")
                             Game()
                       else:
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("It's a Tie")
                             Game()      

                    if O() == "You win":
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        print ("Player O wins")
                        Game()
                    else:
                        print ("\n" * 50)
                        print ("This is Round: " + str(Round))
                        Board()
                        
                        if CX() == "You win":
                             print ("\n" * 50)
                             print ("This is Round: " + str(Round))
                             Board()
                             print ("Computer wins")
                             Game()
                        else:
                            msg = "4"
                            client.send( msg.encode('utf-8') ) 
                            Round = Round + 1
            Mode()

     else:
        exit()

Game()

