from datetime import datetime
from enum import Enum, IntEnum

class Action(IntEnum):
    Breakfast = 1
    Lunch = 2
    Dinner = 3
    Sleep = 4
    Gym = 5
    Class = 6
    Church = 7
    Television = 8
    River = 9

class Agent:

    def __init__(self, initialstate):
        self.state = initialstate
        pass

    def sense_world(self, dt, sick):
        weekend = False
        gym_day = False
        
        if(dt.weekday() == 0 or dt.weekday() == 2 or dt.weekday() == 4):
            gym_day = True
        


        if (dt.weekday() >= 5):
            weekend = True

        #Statements to determine: SLEEP
        if (dt.hour >= 22 or dt.hour < 6 or (dt.hour < 9 and weekend)):
            self.state = Action.Sleep

        
        #Statements to determine: GYM
        if (gym_day == True and (dt.hour == 7)):
            self.state = Action.Gym
        
        #Statements to determine: CHURCH
        if (dt.weekday() == 6 and dt.hour == 10):
            self.state = Action.Church

        #Statements to determine: CLASS
        if (((dt.hour > 7 and gym_day == True) or (dt.hour > 6 and gym_day == False and weekend == False)) and dt.hour < 17):
            self.state = Action.Class

        #Statements to determine: RIVER
        if (((dt.weekday() == 5 and dt.hour >= 10) or (dt.weekday() == 6 and dt.hour >= 11)) and dt.hour < 19):
            self.state = Action.River
        
        #Statements to determine: TV
        if ((dt.hour >= 17 and weekend == False and dt.hour < 22) or (dt.hour > 19 and dt.hour < 22 and weekend == True)):
            self.state = Action.Television

        #Statements to determine: BREAKFAST
        if ((dt.hour == 6 and weekend == False) or (dt.hour == 9 and weekend == True)):
            self.state = Action.Breakfast
        
        #Statements to determine: LUNCH
        if(((weekend == False) and (dt.hour == 13)) or ((weekend == True) and (dt.hour == 14)) ):
            self.state = Action.Lunch
            
        #Statements to determine: DINNER
        if(dt.hour >= 19):
            self.state = Action.Dinner

        return self.state

    def perform_action(self):
        if self.state == Action.Breakfast:
            return "I am eating breakfast"
        if self.state == Action.Sleep:
            return "ZzZzZzZzZzZ"
        if self.state == Action.Gym:
            return "1..2..3..4..5..6 Next Set"
        if self.state == Action.Church:
            return "Shhhh.... Be quite. We're praying!"
        if self.state == Action.Class:
            return "Can't reply right now, in class"
        if self.state == Action.River:
            return "Weeee... Im swimming in the River"
    
        if self.state == Action.Dinner:
            return "Foooooooood!!!:Dinner"
        if self.state == Action.Lunch:
            return "Time for lunch :D "
        if self.state == Action.Television:
            return "I am watching TV. You can join me if you have popcorn."

        # add in the checks for all the other states
        # return "I am eating lunch"
        # return "I am eating dinner"
        # return "I am sleeping"
        # return "I am at the gym"
        # return "I am in class"
        # return "I am at church"
        # return "I am watching television"
        # return "I am next to the river"
