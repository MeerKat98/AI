from Agent import Action, Agent
from datetime import datetime
from enum import Enum, IntEnum

# create the test agent
testAgent = Agent(Action.Breakfast)

# send the agent the details of the environment
d1 = datetime(year = 2020, month = 2, day = 23, hour = 10, minute = 1, second = 59)
testAgent.sense_world(d1, False)

# agent outputs results based on the state it is in
print(testAgent.perform_action())