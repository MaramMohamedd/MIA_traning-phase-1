defensive = {
    'Brake Late': [25, 30],
    'ERS Deployment': [40, 50],
    'Slipstream Cut': [20, 40],
    'Aggressive Block': [35, 100]
}

offensive = {
    'RDS Boost': [45, 12],
    'Red Bull Surge': [80, 20],
    'Precision Turn': [30, 8],
    'Turbo Start': [50, 10],
    'Mercedes Charge': [90, 22],
    'Corner Mastery': [25, 7]
}

class Racer:
    def __init__(self):
        self.tire_health = 100
        self.fuel = 500
        self.used_aggressive_blocks = 0
        self.used_ers_deployments = 0
   
 #both racers will use the next two methods but each one with diff behavior -> polymorphism
    def Call_move(self):
        pass  #to be implemented in child classes

    def Call_tactic(self):
        pass  #to be implemented in child classes
    #both racers will use it 
    def do_offensive_move(self, move):
        if move in offensive:
            fuel_cost, tire_impact = offensive[move]
            if self.fuel >= fuel_cost:
                self.fuel -= fuel_cost
                return tire_impact
            print("Not enough fuel for this move!")
        else:
            print("Move not found!")
        return 0

    def do_defensive_tacticks(self, tactic):
        if tactic in defensive:
            fuel_cost, damage_reduction = defensive[tactic]
            if self.fuel >= fuel_cost:
                self.fuel -= fuel_cost
                return damage_reduction
            print("Not enough fuel for this tactic!")
        else:
            print("Tactic not found!")
        return 0

class Mostafa(Racer):
    def Call_move(self):
        print("1- Turbo Start\n2- Mercedes Charge\n3- Corner Mastery")
        choice = 5
        while choice > 3 or choice < 1:
          choice = int(input("Choose move (1-3): "))
        return ['Turbo Start', 'Mercedes Charge', 'Corner Mastery'][choice-1]

    def Call_tactic(self):
        print("1- Slipstream Cut\n2- Aggressive Block")
        choice = 3 
        while choice > 2 or choice <1 :
          choice = int(input("Choose tactic (1-2): "))
        tactic = ['Slipstream Cut', 'Aggressive Block'][choice-1]
        
        if tactic == 'Aggressive Block' and self.used_aggressive_blocks >= 2:
            print("Can't use Aggressive Block more than twice!")
            return self.Call_tactic()  
            
        if tactic == 'Aggressive Block':
            self.used_aggressive_blocks += 1
        return tactic

class Vers(Racer):
    def Call_move(self):
        print("1- RDS Boost\n2- Red Bull Surge\n3- Precision Turn")
        choice = 5
        while choice > 3 or choice < 1 :
          choice = int(input("Choose move (1-3): "))
        return ['RDS Boost', 'Red Bull Surge', 'Precision Turn'][choice-1]

    def Call_tactic(self):
        print("1- Brake Late\n2- ERS Deployment")
        choice = 5
        while choice > 2 or choice < 1 :
           choice = int(input("Choose tactic (1-2): "))
        tactic = ['Brake Late', 'ERS Deployment'][choice-1]
        
        if tactic == 'ERS Deployment' and self.used_ers_deployments >= 3:
            print("Can't use ERS Deployment more than three times!")
            return self.Call_tactic()  # using recursion instead of a loop for chekcing the validation
            
        if tactic == 'ERS Deployment':
            self.used_ers_deployments += 1
        return tactic

class Race:
    def __init__(self, racer1, racer2):
        self.racer1 = racer1
        self.racer2 = racer2
        self.current_turn = 1  # 0 for racer1 and 1 for racer2(verstappens will beggin so i will start with one )

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def check_winner(self):
        if self.racer1.tire_health <= 0:
            return self.racer2
        if self.racer2.tire_health <= 0:
            return self.racer1
        return None

    def start_race(self):
        print('_'*50)
        print("RACE START!")
        print('_'*50)
        while True:
            attacker = self.racer1 if self.current_turn == 0 else self.racer2
            defender = self.racer2 if self.current_turn == 0 else self.racer1

            print(f"\n--- {attacker.__class__.__name__}'s turn ---")
            print(f"{attacker.__class__.__name__}: Fuel={attacker.fuel}, Tires={attacker.tire_health}")
            print(f"{defender.__class__.__name__}: Fuel={defender.fuel}, Tires={defender.tire_health}")

            # attacker's move
            move = attacker.Call_move()
            damage = attacker.do_offensive_move(move)
            print(f"{attacker.__class__.__name__} uses {move}!")

            # defender's response
            defend = input(f"{defender.__class__.__name__}, defend? (y/n): ").lower()
            if defend == 'y':
                tactic = defender.Call_tactic()
                reduction = defender.do_defensive_tacticks(tactic)
                damage = max(0, damage - reduction)
                print(f"{defender.__class__.__name__} defends with {tactic}!")
            
            defender.tire_health -= damage
            print(f"{defender.__class__.__name__} takes {damage} damage!")

            winner = self.check_winner()
            if winner:
                print(f"\n {winner.__class__.__name__} WINS THE RACE! ")
                break

            self.switch_turn()

# starting  the race
racer1  = Mostafa()
racer2  = Vers()
race = Race(racer1, racer2)
race.start_race()


#about my trials actually i started watching el zero web school for oop concepts
#then started to implement the class but before that i start to draw like a digram in papaers shows 
#what is the usage of each attribute and class then tried to implement class racer and its functions 
#applying THE INHERITANCE concept by making the class racer (parent) ans class mostafe (child)
#class vers(child2) then modifying the methods that tailors each racer moves and tactics (POLYMORPHISM)
#  the actual problem was in class race the simulation process 
#i tried in this class but each time i discover a new condition must be handeled 
#like the number of trials for a specific tactic or move and is it  amust for the user to defend or make an offensive move ?
#so after searching the debugs were solved and the class finished 
#then in the main class i started to intialize the racers using an objs and called the function race start 
# actually i have a passion to do more in this proj but due to time this is what i could do 
# also from c++ i used maps many times so i thought that making the moves in a dict will help so i made this  