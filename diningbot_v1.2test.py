from hashlib import new
from math import exp
import datetime
import time
import random

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
        elif taskComplete == 'e': gradeEvaluator()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs / setTaskTime Range
    logID = 3
    taskTimeLogs(logID, realTaskTime)
    setTaskTimeRange(logID, realTaskTime)
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
        elif taskComplete == 'e': gradeEvaluator()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs / setTaskTimeRange
    logID = 0
    taskTimeLogs(logID, realTaskTime)
    setTaskTimeRange(logID, realTaskTime)
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
        elif taskComplete == 'e': gradeEvaluator()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs / setTaskTimeRange
    logID = 2
    taskTimeLogs(logID, realTaskTime)
    setTaskTimeRange(logID, realTaskTime)
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
        elif taskComplete == 'e': gradeEvaluator()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs / setTaskTimeRange
    logID = 1
    taskTimeLogs(logID, realTaskTime)
    setTaskTimeRange(logID, realTaskTime)
    priorities[0]['urgency'] -= 35
    return priorities


# task: hot water on ice
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
        elif taskComplete == 'e': gradeEvaluator()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs / setTaskTimeRange
    logID = 4
    taskTimeLogs(logID, realTaskTime)
    setTaskTimeRange(logID, realTaskTime)
    priorities[0]['urgency'] -= 35
    return priorities


# task: check volpaks, restock if needed
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
        elif taskComplete == 'e': gradeEvaluator()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs / setTaskTimeRange
    logID = 7
    taskTimeLogs(logID, realTaskTime)
    setTaskTimeRange(logID, realTaskTime)
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
        elif taskComplete == 'e': gradeEvaluator()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs
    logID = 6
    taskTimeLogs(logID, realTaskTime)
    setTaskTimeRange(logID, realTaskTime)
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
        elif taskComplete == 'e': gradeEvaluator()
    endClock = time.time()
    taskTime = endClock - startClock
    realTaskTime = int(taskTime)
    # log id: used as key for sorting data / taskTimeLogs / setTaskTimeRange
    logID = 5
    taskTimeLogs(logID, realTaskTime)
    setTaskTimeRange(logID, realTaskTime)
    priorities[0]['urgency'] -= 55
    return priorities

# launch task list
# urgency rating 1-100
def startingPriorities():
    priorities = [
    {'task':'trash', 'urgency':75},
    {'task':'selfServe', 'urgency':70},
    {'task':'tableTouch', 'urgency':65},
    {'task':'iceMelt', 'urgency':50},
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
        print("==========================")
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
        if logid not in range(8): print("ERROR 102: Invalid logid, Contact Developer.")


# final display, avgs time tables
def shiftSummary(sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade, iceMeltGrade, spotSweepGrade, selfServeTrashGrade, volpakGrade):
    if len(trashTime) >= 1: avgTrashTime = sum(trashTime) // len(trashTime)
    if len(selfServeTime) >= 1: avgSelfServeTime = sum(selfServeTime) // len(selfServeTime)
    if len(tableTouchTime) >= 1:avgTableTouchTime = sum(tableTouchTime) // len(tableTouchTime)
    if len(teaRefillTime) >= 1: avgTeaRefillTime = sum(teaRefillTime) // len(teaRefillTime)
    if len(iceMeltTime) >= 1: avgIceMeltTime = sum(iceMeltTime) // len(iceMeltTime)
    if len(spotSweepTime) >= 1: avgSpotSweepTime = sum(spotSweepTime) // len(spotSweepTime)
    if len(selfServeTrashTime) >= 1: avgSelfServeTrashTime = sum(selfServeTrashTime) // len(selfServeTrashTime)
    if len(volpakTime) >= 1: avgVolpakTime = sum(volpakTime) // len(volpakTime)
    totalSessionTime = sum(trashTime+selfServeTime+tableTouchTime+teaRefillTime+iceMeltTime+spotSweepTime+selfServeTrashTime+volpakTime)
    minuteDisplay = totalSessionTime // 60
    secondDisplay = totalSessionTime % 60
    if secondDisplay < 10: finalTimeDisplay = f"{minuteDisplay}:0{secondDisplay}"
    elif secondDisplay >= 10: finalTimeDisplay = f"{minuteDisplay}:{secondDisplay}"
    totalTasksCompleted = len(trashTime+selfServeTime+tableTouchTime+teaRefillTime+iceMeltTime+spotSweepTime+selfServeTrashTime+volpakTime)
    avgTaskTime = totalSessionTime // totalTasksCompleted
    print(f"Here Is Your Report Card {crewName}:")
    time.sleep(2)
    print("This is how your average times break down...")
    time.sleep(2)
    if len(trashTime) >= 1:
        print(f"Trash - {avgTrashTime} Seconds. Grade {trashGrade}")
        time.sleep(2)
    if len(selfServeTime) >= 1: 
        print(f"Self Serve - {avgSelfServeTime} Seconds. Grade {selfServeGrade}")
        time.sleep(2)
    if len(tableTouchTime) >= 1: 
        print(f"Table Touches - {avgTableTouchTime} Seconds. Grade {tableTouchGrade}")
        time.sleep(2)
    if len(teaRefillTime) >= 1: 
        print(f"Tea Refills - {avgTeaRefillTime} Seconds. Grade {teaRefillGrade}")
        time.sleep(2)
    if len(iceMeltTime) >= 1: 
        print(f"Ice Melts - {avgIceMeltTime} Seconds. Grade {iceMeltGrade}")
        time.sleep(2)
    if len(spotSweepTime) >= 1: 
        print(f"Spot Sweeping - {avgSpotSweepTime} Seconds. Grade {spotSweepGrade}")
        time.sleep(2)
    if len(selfServeTrashTime) >= 1:
        print(f"Self Serve Trash - {avgSelfServeTrashTime} Seconds. Grade {selfServeTrashGrade}")
        time.sleep(2)
    if len(volpakTime) >= 1: 
        print(f"Volpaks - {avgVolpakTime} Seconds. Grade {volpakGrade}")
        time.sleep(2)
    if len(trashTime) >= 1: 
        print(f"Total Tasks Completed Today - {totalTasksCompleted}")
        time.sleep(2)
    if len(trashTime) >= 1: 
        print(f"Total Time For All Tasks - {finalTimeDisplay}")
        time.sleep(2)
    if len(trashTime) >= 1: 
        print(f"The Average Time It Took For You To Complete A Task Was - {avgTaskTime} Seconds. Grade {sessionGrade}")
        time.sleep(2)
    print(f"Thank You For Participating! Program Window Will Close In 30 Seconds.")
    time.sleep(30)
    exit()

# calculates approximate time task should be completed in. Times outputted determine feedback user recieves
def setTaskTimeRange(logid, time):
    # avgExpectedTime used for scoring shift in shiftScore function
    # Adjust Trash Time Expectations
    if logid == 0:
        positive = 1
        lowRange = 2
        highRange = 3
        avgExpectedTime = 4
    # Adjust selfServe Time Expectations
    if logid == 1:
        positive = 1
        lowRange = 2
        highRange = 3
        avgExpectedTime = 4
    # Adjust tableTouch Time Expectations
    if logid == 2:
        positive = 1
        lowRange = 2
        highRange = 3
        avgExpectedTime = 4
    # Adjust teaRefill Time Expectations
    if logid == 3:
        positive = 1
        lowRange = 2
        highRange = 3
        avgExpectedTime = 4
    # Adjust iceMelt Time Expectations
    if logid == 4:
        positive = 1
        lowRange = 2
        highRange = 3
        avgExpectedTime = 4
    # Adjust spotSweep Time Expectations
    if logid == 5:
        positive = 1
        lowRange = 2
        highRange = 3
        avgExpectedTime = 4
    # Adjust selfServeTrash Time Expectations
    if logid == 6:
        positive = 1
        lowRange = 2
        highRange = 3
        avgExpectedTime = 4
    # Adjust volpak Time Expectations
    if logid == 7:
        positive = 1
        lowRange = 2
        highRange = 3
        avgExpectedTime = 4
    if logid not in range(8): print("ERROR 101: Invalid logid, Contact Developer.")

    passTime = time
    # TODO: fix... fix... fix... 
    # adjust times for expected foot traffic
    today = datetime.datetime.today()
    now = datetime.datetime.now()
    currentHour = int(now.hour)
    # if today.weekday() == 4:
        # friday night 12.5% higher expected times 
        # reassign range when hours of operation change
        # if currentHour() in range(17,21):
        #     positive * 1.125
        #     lowRange * 1.125
        #     highRange * 1.125
    # saturday 10% higher expected times
    # if today.weekday() == 5:
    #     positive * 1.1
    #     lowRange * 1.1
    #     highRange * 1.1
        # saturday night 15% higher expected times
        # if currentHour() in range(17,21):
        #     positive * 1.05
        #     lowRange * 1.05
        #     highRange * 1.05
    # sunday 7.5% higher expected times
    # if today.weekday() == 6:
    #     positive * 1.075
    #     lowRange * 1.075
    #     highRange * 1.075
    if logid in range(8):
        expectedTime = [positive, lowRange, highRange]
    
    scoreTracker(logid, passTime, avgExpectedTime)
    displayFeedback(expectedTime, passTime)

# sorts and stores data for gradeEvaluator
def scoreTracker(logid, newTime, avgTime):
    # percentage variation calculator
    if newTime == avgTime: pctChg=0
    elif newTime < avgTime: pctChg=(newTime-avgTime)//avgTime*100
    elif avgTime < newTime: pctChg=(avgTime-newTime)//avgTime*100
    # sorts percentage variations based on task completed (logid)
    if logid == 0: trashAvg.append(pctChg)
    if logid == 1: selfServeAvg.append(pctChg)
    if logid == 2: tableTouchAvg.append(pctChg)
    if logid == 3: teaRefillAvg.append(pctChg)
    if logid == 4: iceMeltAvg.append(pctChg)
    if logid == 5: spotSweepAvg.append(pctChg)
    if logid == 6: selfServeTrashAvg.append(pctChg)
    if logid == 7: volpakAvg.append(pctChg)


# calculates shift grade
def gradeEvaluator():
    
    if len(trashAvg) >= 1: trashScore = sum(trashAvg) // len(trashAvg)
    if len(selfServeAvg) >= 1: selfServeScore = sum(selfServeAvg) // len(selfServeAvg)
    if len(tableTouchAvg) >= 1: tableTouchScore = sum(tableTouchAvg) // len(tableTouchAvg)
    if len(teaRefillAvg) >= 1: teaRefillScore = sum(teaRefillAvg) // len(teaRefillAvg)
    if len(iceMeltAvg) >= 1: iceMeltScore = sum(iceMeltAvg) // len(iceMeltAvg)
    if len(spotSweepAvg) >= 1: spotSweepScore = sum(spotSweepAvg) // len(spotSweepAvg)
    if len(selfServeTrashAvg) >= 1: selfServeTrashScore = sum(selfServeTrashAvg) // len(selfServeTrashAvg)
    if len(volpakAvg) >= 1: volpakScore = sum(volpakAvg) // len(volpakAvg)

    if len(trashAvg) >= 1: totalSessionCombinedAvgs = sum(trashAvg+selfServeAvg+tableTouchAvg+teaRefillAvg+iceMeltAvg+spotSweepAvg+selfServeTrashAvg+volpakAvg)
    if len(trashAvg) >= 1: 
        totalTasks = len(trashAvg+selfServeAvg+tableTouchAvg+teaRefillAvg+iceMeltAvg+spotSweepAvg+selfServeTrashAvg+volpakAvg)
        sessionScore = totalSessionCombinedAvgs // totalTasks
    # overall grade
    if len(trashAvg) >= 1:
        if sessionScore >= 20: sessionGrade="A+"
        elif sessionScore in range(15,20): sessionGrade="A"
        elif sessionScore in range(10,15): sessionGrade="A-"
        elif sessionScore in range(7,10): sessionGrade="B+"
        elif sessionScore in range(5,7): sessionGrade="B"
        elif sessionScore in range(3,5): sessionGrade="B-"
        elif sessionScore in range(2,3): sessionGrade="C+"
        elif sessionScore in range(-1,2): sessionGrade="C"
        elif sessionScore in range(-4,-1): sessionGrade="C-"
        elif sessionScore in range(-7,-4): sessionGrade="D+"
        elif sessionScore in range(-12,-7): sessionGrade="D"
        elif sessionScore in range(-19,-12): sessionGrade="D-"
        elif sessionScore <= -20: sessionGrade="F"
    # trash grade
    if len(trashAvg) >= 1:
        if trashScore >= 20: trashGrade="A+"
        elif trashScore in range(15,20): trashGrade="A"
        elif trashScore in range(10,15): trashGrade="A-"
        elif trashScore in range(7,10): trashGrade="B+"
        elif trashScore in range(5,7): trashGrade="B"
        elif trashScore in range(3,5): trashGrade="B-"
        elif trashScore in range(2,3): trashGrade="C+"
        elif trashScore in range(-1,2): trashGrade="C"
        elif trashScore in range(-4,-1): trashGrade="C-"
        elif trashScore in range(-7,-4): trashGrade="D+"
        elif trashScore in range(-12,-7): trashGrade="D"
        elif trashScore in range(-19,-12): trashGrade="D-"
        elif trashScore <= -20: trashGrade="F"
    # selfServe grade
    if len(selfServeTrashAvg) >= 1:
        if selfServeScore >= 20: selfServeGrade="A+"
        elif selfServeScore in range(15,20): selfServeGrade="A"
        elif selfServeScore in range(10,15): selfServeGrade="A-"
        elif selfServeScore in range(7,10): selfServeGrade="B+"
        elif selfServeScore in range(5,7): selfServeGrade="B"
        elif selfServeScore in range(3,5): selfServeGrade="B-"
        elif selfServeScore in range(2,3): selfServeGrade="C+"
        elif selfServeScore in range(-1,2): selfServeGrade="C"
        elif selfServeScore in range(-4,-1): selfServeGrade="C-"
        elif selfServeScore in range(-7,-4): selfServeGrade="D+"
        elif selfServeScore in range(-12,-7): selfServeGrade="D"
        elif selfServeScore in range(-19,-12): selfServeGrade="D-"
        elif selfServeScore <= -20: selfServeGrade="F"
    # tableTouch grade
    if len(tableTouchAvg) >= 1:
        if tableTouchScore >= 20: tableTouchGrade="A+"
        elif tableTouchScore in range(15,20): tableTouchGrade="A"
        elif tableTouchScore in range(10,15): tableTouchGrade="A-"
        elif tableTouchScore in range(7,10): tableTouchGrade="B+"
        elif tableTouchScore in range(5,7): tableTouchGrade="B"
        elif tableTouchScore in range(3,5): tableTouchGrade="B-"
        elif tableTouchScore in range(2,3): tableTouchGrade="C+"
        elif tableTouchScore in range(-1,2): tableTouchGrade="C"
        elif tableTouchScore in range(-4,-1): tableTouchGrade="C-"
        elif tableTouchScore in range(-7,-4): tableTouchGrade="D+"
        elif tableTouchScore in range(-12,-7): tableTouchGrade="D"
        elif tableTouchScore in range(-19,-12): tableTouchGrade="D-"
        elif tableTouchScore <= -20: tableTouchGrade="F"
    # teaRefill grade
    if len(teaRefillAvg) >= 1:
        if teaRefillScore >= 20: teaRefillGrade="A+"
        elif teaRefillScore in range(15,20): teaRefillGrade="A"
        elif teaRefillScore in range(10,15): teaRefillGrade="A-"
        elif teaRefillScore in range(7,10): teaRefillGrade="B+"
        elif teaRefillScore in range(5,7): teaRefillGrade="B"
        elif teaRefillScore in range(3,5): teaRefillGrade="B-"
        elif teaRefillScore in range(2,3): teaRefillGrade="C+"
        elif teaRefillScore in range(-1,2): teaRefillGrade="C"
        elif teaRefillScore in range(-4,-1): teaRefillGrade="C-"
        elif teaRefillScore in range(-7,-4): teaRefillGrade="D+"
        elif teaRefillScore in range(-12,-7): teaRefillGrade="D"
        elif teaRefillScore in range(-19,-12): teaRefillGrade="D-"
        elif teaRefillScore <= -20: teaRefillGrade="F"
    # iceMelt grade
    if len(iceMeltAvg) >= 1:
        if iceMeltScore >= 20: iceMeltGrade="A+"
        elif iceMeltScore in range(15,20): iceMeltGrade="A"
        elif iceMeltScore in range(10,15): iceMeltGrade="A-"
        elif iceMeltScore in range(7,10): iceMeltGrade="B+"
        elif iceMeltScore in range(5,7): iceMeltGrade="B"
        elif iceMeltScore in range(3,5): iceMeltGrade="B-"
        elif iceMeltScore in range(2,3): iceMeltGrade="C+"
        elif iceMeltScore in range(-1,2): iceMeltGrade="C"
        elif iceMeltScore in range(-4,-1): iceMeltGrade="C-"
        elif iceMeltScore in range(-7,-4): iceMeltGrade="D+"
        elif iceMeltScore in range(-12,-7): iceMeltGrade="D"
        elif iceMeltScore in range(-19,-12): iceMeltGrade="D-"
        elif iceMeltScore <= -20: iceMeltGrade="F"
    # spotSweep grade
    if len(spotSweepAvg) >= 1:
        if spotSweepScore >= 20: spotSweepGrade="A+"
        elif spotSweepScore in range(15,20): spotSweepGrade="A"
        elif spotSweepScore in range(10,15): spotSweepGrade="A-"
        elif spotSweepScore in range(7,10): spotSweepGrade="B+"
        elif spotSweepScore in range(5,7): spotSweepGrade="B"
        elif spotSweepScore in range(3,5): spotSweepGrade="B-"
        elif spotSweepScore in range(2,3): spotSweepGrade="C+"
        elif spotSweepScore in range(-1,2): spotSweepGrade="C"
        elif spotSweepScore in range(-4,-1): spotSweepGrade="C-"
        elif spotSweepScore in range(-7,-4): spotSweepGrade="D+"
        elif spotSweepScore in range(-12,-7): spotSweepGrade="D"
        elif spotSweepScore in range(-19,-12): spotSweepGrade="D-"
        elif spotSweepScore <= -20: spotSweepGrade="F"
    # selfServeTrash grade
    if len(selfServeTrashAvg) >= 1: 
        if selfServeTrashScore >= 20: selfServeTrashGrade="A+"
        elif selfServeTrashScore in range(15,20): selfServeTrashGrade="A"
        elif selfServeTrashScore in range(10,15): selfServeTrashGrade="A-"
        elif selfServeTrashScore in range(7,10): selfServeTrashGrade="B+"
        elif selfServeTrashScore in range(5,7): selfServeTrashGrade="B"
        elif selfServeTrashScore in range(3,5): selfServeTrashGrade="B-"
        elif selfServeTrashScore in range(2,3): selfServeTrashGrade="C+"
        elif selfServeTrashScore in range(-1,2): selfServeTrashGrade="C"
        elif selfServeTrashScore in range(-4,-1): selfServeTrashGrade="C-"
        elif selfServeTrashScore in range(-7,-4): selfServeTrashGrade="D+"
        elif selfServeTrashScore in range(-12,-7): selfServeTrashGrade="D"
        elif selfServeTrashScore in range(-19,-12): selfServeTrashGrade="D-"
        elif selfServeTrashScore <= -20: selfServeTrashGrade="F"
    # volpak grade
    # TODO: Solve Error Before Update
    # File "c:\Dev\diningbot_v1.2test.py", line 596, in gradeEvaluator
    # shiftSummary(sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade, iceMeltGrade, spotSweepGrade, selfServeTrashGrade, volpakGrade)
    # UnboundLocalError: local variable 'volpakGrade' referenced before assignment
    if len(volpakAvg) >= 1:
        if volpakScore >= 20: volpakGrade="A+"
        elif volpakScore in range(15,20): volpakGrade="A"
        elif volpakScore in range(10,15): volpakGrade="A-"
        elif volpakScore in range(7,10): volpakGrade="B+"
        elif volpakScore in range(5,7): volpakGrade="B"
        elif volpakScore in range(3,5): volpakGrade="B-"
        elif volpakScore in range(2,3): volpakGrade="C+"
        elif volpakScore in range(-1,2): volpakGrade="C"
        elif volpakScore in range(-4,-1): volpakGrade="C-"
        elif volpakScore in range(-7,-4): volpakGrade="D+"
        elif volpakScore in range(-12,-7): volpakGrade="D"
        elif volpakScore in range(-19,-12): volpakGrade="D-"
        elif volpakScore <= -20: volpakGrade="F"

    shiftSummary(sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade, iceMeltGrade, spotSweepGrade, selfServeTrashGrade, volpakGrade)

# delivers timely and relevant feedback to end user (trainee)
def displayFeedback(expected, timeTook):
    # feedback classes based on time took to complete each task
    positiveFeedback = [
    f"Great Job {crewName}!",
    "Excellent Time, Woohoo!", 
    "Strong Preformance!", 
    "SOU FTW!", 
    "This Dining Room Is Looking Very One Love Quality!"
    ]
    neutralFeedback = [
    "Just A Little Faster And We Are Rocking It",
    "Decent Time...",
    "Our Task Time Is Ok. Not To Be Confused With Good Though.",
    "Think About Ways To Shave Off Time. Right Now You Are Doing Fine But There Is Room For Improvement.",
    f"Not Bad {crewName}, Not Good Either."
    ]
    constructiveFeedback = [
    "Hurry Up or Aidee Will Yell At You!",
    "We Got to Go A Bit Quicker...",
    f"Todd Would Be Disappointed, {crewName}. Put Some Pep In Your Step!",
    "This Dining Room Doesnt Clean Itself, Pick Up The Pace.",
    "FASTER!!!",
    f"Here At Raising Canes We Have Standards. You Dont Meet Them {crewName}, But You Can If You Knock These Tasks Out Quicker!",
    f"I Know You Can Go Faster {crewName}",
    "Go Quicker, You're Stressing Joyce Out."
    ]
 
    minuteDisplay = timeTook // 60
    secondDisplay = timeTook % 60
    if secondDisplay < 10: finalTimeDisplay = f"Time {minuteDisplay}:0{secondDisplay}"
    elif secondDisplay >= 10: finalTimeDisplay = f"Time {minuteDisplay}:{secondDisplay}"
    if timeTook <= expected[0]: print(f"{finalTimeDisplay} Feedback: {random.choice(positiveFeedback)}")
    elif timeTook in range(expected[1], expected[2]): print(f"{finalTimeDisplay} Feedback: {random.choice(neutralFeedback)}")
    else: print(f"{finalTimeDisplay} Feedback: {random.choice(constructiveFeedback)}")
        
trashTime = []
selfServeTime = []  
tableTouchTime = []
teaRefillTime = []
iceMeltTime = []
spotSweepTime = []
selfServeTrashTime = []
volpakTime = []
trashAvg = []
selfServeAvg = []  
tableTouchAvg = []
teaRefillAvg = []
iceMeltAvg = []
spotSweepAvg = []
selfServeTrashAvg = []
volpakAvg = []

crewName = input('Enter Your Name: ')

print("Press 'c' For Complete, 'p' For Pass, 'd' For Unexpected Delay Or 'e' To Exit When Finished.")
shiftLaunchVer = True
while shiftLaunchVer:  
    shiftLauncher = input("type 'start' to begin your shift, or type 'freshstart' for instructions on effective use: ")
    if shiftLauncher == "start":
        shiftLaunchVer = False
        startingPriorities()
    # TODO: add 'help' feature / instuctions
    elif shiftLauncher == "freshstart": print("Help is on the way: feature scheduled to be added in v1.3")