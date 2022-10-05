#importing
import random
import time

#start main loop
while True:
    #asking for parameters and setting variables
    SampleSize = int(input("Sample Size: "))
    BDayMatch = 0
    BDayNoMatch = 0
    NumberOfPeople = int(input("People: "))
    NumberOfPossibilities = 365
    #starts timer
    timestampone = time.perf_counter()
    #starts brute force calculation
    for SampleNumber in range(SampleSize):
        dates = []
        Duplicates = 0
        
        for i in range(NumberOfPeople):
            date = random.randint(1,NumberOfPossibilities)
            dates.append(date)
        for i in dates:
            counter = -1
            for x in dates:
                if i == x:
                    counter += 1
            if counter >= 1:
                Duplicates += counter
        if Duplicates >= 1:
            BDayMatch += 1
        else:
            BDayNoMatch += 1
        #prints percentage completed
        print("Completed: "+str((SampleNumber/SampleSize)*100)[:5]+"%")
    
    #calculates final chance of matching birthday and stops timer
    TotalBDays = BDayMatch + BDayNoMatch
    FinalAverage = BDayMatch/TotalBDays*100
    timestamptwo = time.perf_counter()
    #prints results
    print(f"Result: {FinalAverage}% chance of a matching birthday")
    print("Ran in "+str(timestamptwo-timestampone)+" seconds\n\n")
    #repeats
