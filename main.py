import random


class Die:
    def __init__(self):
        self._value= None  #this also same to way passing default value as an argument
    
    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1,6) #genrate a random integer between 1 and 6 
        self._value=new_value
        return new_value
    


class Player:
    def __init__(self,die,is_computer=False):
        self._die= die
        self._is_computer= is_computer
        self._counter =6  #not modify the variable out side the class externally

    @property
    def die(self):
        return self._die  
    @property
    def is_computer(self):
        return self._is_computer
    @property
    def counter(self):
        return self._counter 
    
    def increment_counter(self):
        self._counter +=1
    def decrement_counter(self):
        self._counter -=1

    def roll_die(self):
        return self._die.roll()



class Dicegame:
    def __init__(self, player , computer):
        self._player = player
        self._computer = computer

    
    def play(self):
        print("+++++++++++++++++++++++++++++++++")
        print("🎲  Welcome to Roll the Dice! 🎲")
        print("+++++++++++++++++++++++++++++++++")

        while True:
            self.play_round()
            game_status =self.check_gameover()
            if game_status:  # this check is not true then stop the game some one is won
                break

    def play_round(self):

        self.print_welcome_round()

        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()
          
        #show the points 
        self.show_dice(player_value,computer_value)

        # Deter min the winner and loser
        if player_value> computer_value:
            print("You won the round 🔥!!")
            self.update_counter(winner=self._player, loser=self._computer)
        elif computer_value>player_value:
            print("The computer won the round. Try again 😓 ")
            self.update_counter(winner=self._computer, loser=self._player)
           
        else:
            print("Its a tie 😎!")
    
        self.show_counter()

    def print_welcome_round(self):
        
        print("                                   ")
        print("             NEW ROUND             ")
        input("Press any key to roll the dice. 🎲 ")

    def show_dice(self, player_value,computer_value):

        print(f"Your die :{player_value}")
        print(f"Computer die :{computer_value}")


    def update_counter(self,winner,loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counter(self):
        #show counters
        print(f"\nYour counter : {self._player.counter}")
        print(f"Computer counter :{self._computer.counter}\n")
    
    def check_gameover(self):
        if self._player.counter == 0:
           self.game_over_message(self._player)
           return True
        elif self._computer.counter == 0:
            self.game_over_message(self._computer)
            return True
        else:
            False
    def game_over_message(self,winner):
        if winner.is_computer:
            print("\n     G A M E   O V E R 😎")
            print("====================================")
            print("THE COMPUTER WON THE GAME. SORRY....")
            print("====================================")
            print("                                    ")

        else:
             print("\n  G A M E   O V E R 😎")
             print("====================================")
             print("  YOU WON THE GAME 🔥🔥🎉🎉🎉 ")
             print("====================================")
             print("                                    ")




if __name__ == "__main__":
    die = Die()
    my_player = Player(die, is_computer=False)
    computer_player = Player(die, is_computer=True)
    game = Dicegame(my_player, computer_player)
    game.play()




