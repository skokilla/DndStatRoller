#Stat roller
import random
import numpy as np

def roll():
    #print("Made it to roll ") #Debug line
    try:
        stats = []
        
        for t in range(6):
            dice = ([random.randint(1,6), random.randint(1,6),random.randint(1,6),random.randint(1,6)]) # generates rolls
         #   print(f"Rolled: {dice}")
            lowest = min(dice)
        #    print(f"The lowest dice is {lowest} and will be dropped")
            dice.remove(lowest)
            stat = sum(dice)
            stats.append(stat)
       # print(f"Final stats: {stats}")
        return stats
    except Exception as e:
        print(f"Error occurred: {e}")
       
        
def main():
    
    sets = int(input("How many sets of stats would you like to roll? "))
    allStats = []
   # print(sets) #Debug line
    for x in range(sets):
       statSet = roll()
       if statSet:
           allStats.append(statSet)
    print(f"\nAll {sets} generated stat sets to pick from")
    for i, statSet in enumerate(allStats,1):
        print(f"Set{i}: {statSet}")
    
if __name__ == '__main__':
    main()
input("\nPress Enter to exit...")