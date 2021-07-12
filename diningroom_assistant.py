import time

# refill aerators and brew next batch of tea
def teaRefill(priorities):
    print("New Task - Are The Tea Aerators Full?")
    startClock = time.time()
    taskVer = True
    while taskVer:
        taskComplete = input("")
        if taskComplete == 'c': taskVer = False
        elif taskComplete == 'p':
            priorities[0]['urgency'] -= 15
            print("task pushed back.")
            return priorities
        elif taskComplete == 'd':
            while True:
                pauseTask = input('press any key to resume: ')
                if pauseTask: return 
        elif taskComplete == 'e': shiftSummary()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs
    logID = 3
    taskTimeLogs(logID, realTaskTime)
    feedback = ""
    
    print("===============================================")
    if int(taskTime) <= 10: feedback = "Good Time, Lets Keep Going!"
    elif int(taskTime) in range(11, 15): feedback = "Thats Decent."
    else: feedback = "Lets Work On Getting Our Time Down!"
    print(f"Task Completed In: {int(taskTime)} Seconds. {feedback}")
    priorities[0]['urgency'] -= 50
    return priorities


# compress and take out trash
def trash(priorities):
    print("New Task - Lets Check On Trash!")
    startClock = time.time()
    taskVer = True
    while taskVer:
        taskComplete = input("")
        if taskComplete == 'c': taskVer = False
        elif taskComplete == 'p':
            priorities[0]['urgency'] -= 15
            print("task pushed back.")
            return priorities
        elif taskComplete == 'd':
            while True:
                pauseTask = input('press any key to resume: ')
                if pauseTask: return 
        elif taskComplete == 'e': shiftSummary()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs
    logID = 0
    taskTimeLogs(logID, realTaskTime)
    feedback = ""
    
    print("===============================================")
    if int(taskTime) <= 10: feedback = "Good Time, Lets Keep Going!"
    elif int(taskTime) in range(11, 15): feedback = "Thats Decent."
    else: feedback = "Lets Work On Getting Our Time Down!"
    print(f"Task Completed In: {int(taskTime)} Seconds. {feedback}")
    priorities[0]['urgency'] -= 35
    return priorities
    
    
# task: wipe down unoccupied tables and chairs
def tableTouch(priorities):
    print("New Task - Get Some Sani-Wipes Because It Is Table Touch Time!")
    startClock = time.time()
    taskVer = True
    while taskVer:
        taskComplete = input("")
        if taskComplete == 'c': taskVer = False
        elif taskComplete == 'p':
            priorities[0]['urgency'] -= 15
            print("task pushed back.")
            return priorities
        elif taskComplete == 'd':
            while True:
                pauseTask = input('press any key to resume: ')
                if pauseTask: return 
        elif taskComplete == 'e': shiftSummary()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs
    logID = 2
    taskTimeLogs(logID, realTaskTime)
    feedback = ""
    
    print("===============================================")
    if int(taskTime) <= 10: feedback = "Good Time, Lets Keep Going!"
    elif int(taskTime) in range(11, 15): feedback = "Thats Decent."
    else: feedback = "Lets Work On Getting Our Time Down!"
    print(f"Task Completed In: {int(taskTime)} Seconds. {feedback}")
    priorities[0]['urgency'] -= 45
    return priorities


# task: restock, clean surface
def selfServe(priorities):
    print("New Task - How Is Self Serve Looking?")
    startClock = time.time()
    taskVer = True
    while taskVer:
        taskComplete = input("")
        if taskComplete == 'c': taskVer = False
        elif taskComplete == 'p':
            priorities[0]['urgency'] -= 15
            print("task pushed back.")
            return priorities
        elif taskComplete == 'd':
            while True:
                pauseTask = input('press any key to resume: ')
                if pauseTask: return 
        elif taskComplete == 'e': shiftSummary()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs
    logID = 1
    taskTimeLogs(logID, realTaskTime)
    feedback = ""
    
    print("===============================================")  
    if int(taskTime) <= 10: feedback = "Good Time, Lets Keep Going!"
    elif int(taskTime) in range(11, 15): feedback = "Thats Decent."
    else: feedback = "Lets Work On Getting Our Time Down!"
    print(f"Task Completed In: {int(taskTime)} Seconds. {feedback}")
    priorities[0]['urgency'] -= 35
    return priorities


# # task: hot water on ice
def iceMelt(priorities):
    print("New Task - Get Some Hot Water To Melt That Ice Build Up. HOT WALKING!!!")
    startClock = time.time()
    taskVer = True
    while taskVer:
        taskComplete = input("")
        if taskComplete == 'c': taskVer = False
        elif taskComplete == 'p':
            priorities[0]['urgency'] -= 15
            print("task pushed back.")
            return priorities
        elif taskComplete == 'd':
            while True:
                pauseTask = input('press any key to resume: ')
                if pauseTask: return 
        elif taskComplete == 'e': shiftSummary()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs
    logID = 4
    taskTimeLogs(logID, realTaskTime)
    feedback = ""

    print("===============================================")
    if int(taskTime) <= 10: feedback = "Good Time, Lets Keep Going!"
    elif int(taskTime) in range(11, 15): feedback = "Thats Decent."
    else: feedback = "Lets Work On Getting Our Time Down!"
    print(f"Task Completed In: {int(taskTime)} Seconds. {feedback}")
    priorities[0]['urgency'] -= 35
    return priorities


# # task: check volpaks, restock if needed
def volpak(priorities):
    print("New Task - Have The Volpaks Been Squeezed Dry Yet?")
    startClock = time.time()
    taskVer = True
    while taskVer:
        taskComplete = input("")
        if taskComplete == 'c': taskVer = False
        elif taskComplete == 'p':
            priorities[0]['urgency'] -= 15
            print("task pushed back.")
            return priorities
        elif taskComplete == 'd':
            while True:
                pauseTask = input('press any key to resume: ')
                if pauseTask: return 
        elif taskComplete == 'e': shiftSummary()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs
    logID = 7
    taskTimeLogs(logID, realTaskTime)
    feedback = ""

    print("===============================================")
    if int(taskTime) <= 10: feedback = "Good Time, Lets Keep Going!"
    elif int(taskTime) in range(11, 15): feedback = "Thats Decent."
    else: feedback = "Lets Work On Getting Our Time Down!"
    print(f"Task Completed In: {int(taskTime)} Seconds. {feedback}")
    priorities[0]['urgency'] -= 85
    return priorities

# task: check/take out self serve trash
def selfServeTrash(priorities):
    print("New Task - Double Check That The Self Serve Trash Isn't Over 3/4 Full.")
    startClock = time.time()
    taskVer = True
    while taskVer:
        taskComplete = input("")
        if taskComplete == 'c': taskVer = False
        elif taskComplete == 'p':
            priorities[0]['urgency'] -= 15
            print("task pushed back.")
            return priorities
        elif taskComplete == 'd':
            while True:
                pauseTask = input('press any key to resume: ')
                if pauseTask: return 
        elif taskComplete == 'e': shiftSummary()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs
    logID = 6
    taskTimeLogs(logID, realTaskTime)
    feedback = ""
    
    print("===============================================")
    if int(taskTime) <= 10: feedback = "Good Time, Lets Keep Going!"
    elif int(taskTime) in range(11, 15): feedback = "Thats Decent."
    else: feedback = "Lets Work On Getting Our Time Down!"
    print(f"Task Completed In: {int(taskTime)} Seconds. {feedback}")
    priorities[0]['urgency'] -= 75
    return priorities


# task: sweep areas in need of attention
def spotSweep(priorities):
    print("New Task - Does The Dining Room Need A Quick Spot Sweep?")
    startClock = time.time()
    taskVer = True
    while taskVer:
        taskComplete = input("")
        if taskComplete == 'c': taskVer = False
        elif taskComplete == 'p':
            priorities[0]['urgency'] -= 15
            print("task pushed back.")
            return priorities
        elif taskComplete == 'd':
            while True:
                pauseTask = input('press any key to resume: ')
                if pauseTask: return 
        elif taskComplete == 'e': shiftSummary()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs
    logID = 5
    taskTimeLogs(logID, realTaskTime)
    feedback = ""

    print("===============================================")
    if int(taskTime) <= 10: feedback = "Good Time, Lets Keep Going!"
    elif int(taskTime) in range(11, 15): feedback = "Thats Decent."
    else: feedback = "Lets Work On Getting Our Time Down!"
    print(f"Task Completed In: {int(taskTime)} Seconds. {feedback}")
    priorities[0]['urgency'] -= 55
    return priorities

# launch task list
# urgency rating 1-100
def startingPriorities():
    priorities = [
    {'task':'iceMelt', 'urgency':50},
    {'task':'trash', 'urgency':75},
    {'task':'selfServe', 'urgency':70},
    {'task':'tableTouch', 'urgency':65},
    {'task':'teaRefill', 'urgency':45},
    {'task':'spotSweep', 'urgency':35},
    {'task':'selfServeTrash', 'urgency':20},
    {'task':'volpak', 'urgency':10}
    ]
    main(priorities)

# takes user input and forwards information to 'display'
# times tasks for delivering feedback
def main(priorityList):
    while True:
        print("===============================================")
        # print(f"For Testing Purposes - Trash Times (Compiled): {trashTime}")
        priorityList[1]['urgency'] += 5
        priorityList[2]['urgency'] += 5
        priorityList[3]['urgency'] += 5
        priorityList[4]['urgency'] += 5
        priorityList[5]['urgency'] += 5
        priorityList[6]['urgency'] += 5
        priorityList[7]['urgency'] += 5
        priorityList = sorted(priorityList, key = lambda i: i['urgency'], reverse=True)
        # print('New Task!')
        # print('For Testing: {priorityList[0]}')
        if priorityList[0]['task'] == 'trash': trash(priorityList)
        if priorityList[0]['task'] == 'selfServe': selfServe(priorityList)
        if priorityList[0]['task'] == 'tableTouch': tableTouch(priorityList)
        if priorityList[0]['task'] == 'teaRefill': teaRefill(priorityList)
        if priorityList[0]['task'] == 'iceMelt': iceMelt(priorityList)
        if priorityList[0]['task'] == 'spotSweep': spotSweep(priorityList)
        if priorityList[0]['task'] == 'selfServeTrash': selfServeTrash(priorityList)
        if priorityList[0]['task'] == 'volpak': volpak(priorityList)

# logs task times for output in shiftSummary
def taskTimeLogs(logid, time):                      
        if logid == 0: trashTime.append(time)
        if logid == 1: selfServeTime.append(time)
        if logid == 2: tableTouchTime.append(time)
        if logid == 3: teaRefillTime.append(time)
        if logid == 4: iceMeltTime.append(time)
        if logid == 5: spotSweepTime.append(time)
        if logid == 6: selfServeTrashTime.append(time)
        if logid == 7: volpakTime.append(time)

# final display, avgs time tables
def shiftSummary():
    if len(trashTime) > 1: avgTrashTime = sum(trashTime) // len(trashTime)
    if len(selfServeTime) > 1: avgSelfServeTime = sum(selfServeTime) // len(selfServeTime)
    if len(tableTouchTime) > 1:avgTableTouchTime = sum(tableTouchTime) // len(tableTouchTime)
    if len(teaRefillTime) > 1: avgTeaRefillTime = sum(teaRefillTime) // len(teaRefillTime)
    if len(iceMeltTime) > 1: avgIceMeltTime = sum(iceMeltTime) // len(iceMeltTime)
    if len(spotSweepTime) > 1: avgSpotSweepTime = sum(spotSweepTime) // len(spotSweepTime)
    if len(selfServeTrashTime) > 1: avgSelfServeTrashTime = sum(selfServeTrashTime) // len(selfServeTrashTime)
    if len(volpakTime) > 1: avgVolpakTime = sum(volpakTime) // len(volpakTime)
    totalSessionTime = sum(trashTime+selfServeTime+tableTouchTime+teaRefillTime+iceMeltTime+spotSweepTime+selfServeTrashTime+volpakTime)
    totalTasksCompleted = len(trashTime+selfServeTime+tableTouchTime+teaRefillTime+iceMeltTime+spotSweepTime+selfServeTrashTime+volpakTime)
    avgTaskTime = totalSessionTime // totalTasksCompleted
    print(f"Here Is Your Report Card {crewName}:")
    time.sleep(2)
    print("This is how your average times break down...")
    time.sleep(2)
    if len(trashTime) > 1:
        print(f"Trash - {avgTrashTime} Seconds")
        time.sleep(2)
    if len(selfServeTime) > 1: 
        print(f"Self Serve - {avgSelfServeTime} Seconds")
        time.sleep(2)
    if len(tableTouchTime) > 1: 
        print(f"Table Touches - {avgTableTouchTime} Seconds")
        time.sleep(2)
    if len(teaRefillTime) > 1: 
        print(f"Tea Refills - {avgTeaRefillTime} Seconds")
        time.sleep(2)
    if len(iceMeltTime) > 1: 
        print(f"Ice Melts - {avgIceMeltTime} Seconds")
        time.sleep(2)
    if len(spotSweepTime) > 1: 
        print(f"Spot Sweeping - {avgSpotSweepTime} Seconds")
        time.sleep(2)
    if len(selfServeTrashTime) > 1:
        print(f"Self Serve Trash - {avgSelfServeTrashTime} Seconds")
        time.sleep(2)
    if len(volpakTime) > 1: 
        print(f"Volpaks - {avgVolpakTime} Seconds")
        time.sleep(2)
    print(f"The Average Time It Took For You To Complete A Task Was - {float(avgTaskTime)} Seconds")
    time.sleep(2)
    print(f"Total Tasks Completed Today - {totalTasksCompleted}")
    time.sleep(2)
    print(f"Total Time For All Tasks - {totalSessionTime} Seconds")
    time.sleep(2)
    print(f"Thank You For Participating! / Program Window Will Close In 20 Seconds")
    time.sleep(20)
    exit()

trashTime = []
selfServeTime = []  
tableTouchTime = []
teaRefillTime = []
iceMeltTime = []
spotSweepTime = []
selfServeTrashTime = []
volpakTime = []

crewName = input('Enter Your Name: ')
print("Press 'c' For Complete, 'p' For Pass, 'd' For Unexpected Delay Or 'e' To Exit When Finished.")
shiftLaunchVer = True
while shiftLaunchVer:  
    shiftLauncher = input("type 'start' to begin your shift: ")
    if shiftLauncher == "start":
        shiftLaunchVer = False
        startingPriorities()