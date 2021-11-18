#importations
from art import airtitle as ART
from credits import credits
from runconfig import runLetter as rl, runNumber as rn
from airlines import airlines
import random

airline = airlines[random.randint(0, 21)]
AirNumber = random.randint(134, 234579)

print(f"Flight {airline} {AirNumber} cleared for takeoff on runway {rn} {rl}\n\n")
print(credits)
