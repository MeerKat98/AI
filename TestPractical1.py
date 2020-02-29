'''
This File interacts with the agent. 
Includes Test Loop: Runs through all 7 days of the week and prompt the agent 
every hour of the seven days. Outputs the agents responce to terminal
'''
from Agent import Action, Agent
from datetime import datetime
from enum import Enum, IntEnum

testAgent = Agent(Action.Breakfast)
print("Starts on Monday")
for d in range(1,8): #Run through each day
    print("\n########\n#Day: " +  str(d) + "#\n########")

    for h in range(0,24): #Run through every hour
        d1 = datetime(year = 2020, month = 2, day = 16+d, hour = h, minute = 1, second = 59)
        testAgent.sense_world(d1, False)
        print(str(d1.hour) + " : " +  testAgent.perform_action())

'''
Origenal test
-------------
# create the test agent 
testAgent = Agent(Action.Breakfast) 
 
# send the agent the details of the environment 
d1 = datetime(year = 2020, month = 2, day = 23, hour = 10, minute = 1, second = 59) 
testAgent.sense_world(d1, False) 
 
# agent outputs results based on the state it is in 
print(testAgent.perform_action())
'''