from hashlib import new
from math import exp
import datetime
import time
import random
import statistics

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
        print(f'For Testing: {priorityList[0]}')
        print(trashTime)
        print(selfServeTime)  
        print(tableTouchTime)
        print(teaRefillTime)
        print(iceMeltTime)
        print(spotSweepTime)
        print(selfServeTrashTime)
        print(volpakTime)
        print(trashAvg)
        print(selfServeAvg)  
        print(tableTouchAvg)
        print(teaRefillAvg)
        print(iceMeltAvg)
        print(spotSweepAvg)
        print(selfServeTrashAvg)
        print(volpakAvg)
        print(totalAvg)

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
def shiftSummary(overallScore, sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade, iceMeltGrade, spotSweepGrade, selfServeTrashGrade, volpakGrade):
    if len(trashTime) >= 1: avgTrashTime = sum(trashTime) / len(trashTime)
    if len(selfServeTime) >= 1: avgSelfServeTime = sum(selfServeTime) / len(selfServeTime)
    if len(tableTouchTime) >= 1:avgTableTouchTime = sum(tableTouchTime) / len(tableTouchTime)
    if len(teaRefillTime) >= 1: avgTeaRefillTime = sum(teaRefillTime) / len(teaRefillTime)
    if len(iceMeltTime) >= 1: avgIceMeltTime = sum(iceMeltTime) / len(iceMeltTime)
    if len(spotSweepTime) >= 1: avgSpotSweepTime = sum(spotSweepTime) / len(spotSweepTime)
    if len(selfServeTrashTime) >= 1: avgSelfServeTrashTime = sum(selfServeTrashTime) / len(selfServeTrashTime)
    if len(volpakTime) >= 1: avgVolpakTime = sum(volpakTime) / len(volpakTime)
    
    totalSessionTime = sum(trashTime+selfServeTime+tableTouchTime+teaRefillTime+iceMeltTime+spotSweepTime+selfServeTrashTime+volpakTime)
    minuteDisplay = totalSessionTime // 60
    secondDisplay = totalSessionTime % 60
    if secondDisplay < 10: finalTimeDisplay = f"{minuteDisplay}:0{secondDisplay}"
    elif secondDisplay >= 10: finalTimeDisplay = f"{minuteDisplay}:{secondDisplay}"
    totalTasksCompleted = len(trashTime+selfServeTime+tableTouchTime+teaRefillTime+iceMeltTime+spotSweepTime+selfServeTrashTime+volpakTime)
    avgTaskTime = totalSessionTime / totalTasksCompleted
    
    print(f"Here Is Your Report Card {crewName}:")
    time.sleep(2)
    print("This is how your average times break down...")
    time.sleep(2)
    if len(trashTime) >= 1:
        print(f"Trash - {avgTrashTime:.2f} Seconds. Grade {trashGrade}")
        time.sleep(2)
    if len(selfServeTime) >= 1: 
        print(f"Self Serve - {avgSelfServeTime:.2f} Seconds. Grade {selfServeGrade}")
        time.sleep(2)
    if len(tableTouchTime) >= 1: 
        print(f"Table Touches - {avgTableTouchTime:.2f} Seconds. Grade {tableTouchGrade}")
        time.sleep(2)
    if len(teaRefillTime) >= 1: 
        print(f"Tea Refills - {avgTeaRefillTime:.2f} Seconds. Grade {teaRefillGrade}")
        time.sleep(2)
    if len(iceMeltTime) >= 1: 
        print(f"Ice Melts - {avgIceMeltTime:.2f} Seconds. Grade {iceMeltGrade}")
        time.sleep(2)
    if len(spotSweepTime) >= 1: 
        print(f"Spot Sweeping - {avgSpotSweepTime:.2f} Seconds. Grade {spotSweepGrade}")
        time.sleep(2)
    if len(selfServeTrashTime) >= 1:
        print(f"Self Serve Trash - {avgSelfServeTrashTime:.2f} Seconds. Grade {selfServeTrashGrade}")
        time.sleep(2)
    if len(volpakTime) >= 1: 
        print(f"Volpaks - {avgVolpakTime:.2f} Seconds. Grade {volpakGrade}")
        time.sleep(2)
    if len(trashTime) >= 1: 
        print(f"Total Tasks Completed Today - {totalTasksCompleted}")
        time.sleep(2)
    if len(trashTime) >= 1: 
        print(f"Total Time For All Tasks - {finalTimeDisplay}")
        time.sleep(2)
    if len(trashTime) >= 1: 
        print(f"The Average Time It Took For You To Complete A Task Was - {avgTaskTime:.2f} Seconds. Grade {sessionGrade}")
        time.sleep(2)
    print(f"Thank You For Participating! Program Window Will Close In 30 Seconds.")
    time.sleep(30)
    exit()
    # print(f"trash{trashTime}")
    # print(f"selfserve{selfServeTime}")  
    # print(f"tabletouch{tableTouchTime}")
    # print(f"tearefill{teaRefillTime}")
    # print(f"icemelt{iceMeltTime}")
    # print(f"spotsweep{spotSweepTime}")
    # print(f"selftrash{selfServeTrashTime}")
    # print(f"volpak{volpakTime}")
    # print(f"Shift Score: {overallScore}")
# calculates approximate time task should be completed in. Times outputted determine feedback user recieves
def setTaskTimeRange(logid, time):
    # avgExpectedTime used for scoring shift in shiftScore function
    # Adjust Trash Time Expectations
    if logid == 0:
        lowRange = 3
        highRange = 7
    # Adjust selfServe Time Expectations
    if logid == 1:
        lowRange = 3
        highRange = 7
    # Adjust tableTouch Time Expectations
    if logid == 2:
        lowRange = 3
        highRange = 7 
    # Adjust teaRefill Time Expectations
    if logid == 3:
        lowRange = 3
        highRange = 7
    # Adjust iceMelt Time Expectations
    if logid == 4:
        lowRange = 3
        highRange = 7
    # Adjust spotSweep Time Expectations
    if logid == 5:
        lowRange = 3
        highRange = 7
    # Adjust selfServeTrash Time Expectations
    if logid == 6:
        lowRange = 3
        highRange = 7
    # Adjust volpak Time Expectations
    if logid == 7:
        lowRange = 3
        highRange = 7
    if logid not in range(8): print("ERROR 101: Invalid logid, Contact Developer.")
    medianlist = [lowRange, highRange]
    positive = lowRange - 1
    passTime = time
    avgExpectedTime = statistics.median(medianlist)
    # TODO: fix... fix... fix... 
    # adjust times for expected foot traffic
    today = datetime.datetime.today()
    now = datetime.datetime.now()
    currentHour = int(now.hour)
    if today.weekday() == 4:
        # friday night 12.5% higher expected times 
        # reassign range when hours of operation change
        if currentHour() in range(17,21):
            positive * 1.125
            lowRange * 1.125
            highRange * 1.125
    # saturday 10% higher expected times
    if today.weekday() == 5:
        positive * 1.1
        lowRange * 1.1
        highRange * 1.1
        # saturday night 15% higher expected times
        if currentHour() in range(17,21):
            positive * 1.05
            lowRange * 1.05
            highRange * 1.05
    # sunday 7.5% higher expected times
    if today.weekday() == 6:
        positive * 1.075
        lowRange * 1.075
        highRange * 1.075
    if logid in range(8):
        expectedTime = [positive, lowRange, highRange]
    
    scoreTracker(logid, passTime, avgExpectedTime)
    displayFeedback(expectedTime, passTime)

# sorts and stores data for gradeEvaluator
def scoreTracker(logid, newTime, avgTime):
    # percentage variation calculator
    if newTime == avgTime: pctChg=0.0
    elif newTime < avgTime: 
        pctChg=(newTime-avgTime)/avgTime*100
        pctChg *= -1
    elif avgTime < newTime: pctChg=(avgTime-newTime)/avgTime*100
    # sorts percentage variations based on task completed (logid)
    if logid == 0: trashAvg.append(pctChg)
    if logid == 1: selfServeAvg.append(pctChg)
    if logid == 2: tableTouchAvg.append(pctChg)
    if logid == 3: teaRefillAvg.append(pctChg)
    if logid == 4: iceMeltAvg.append(pctChg)
    if logid == 5: spotSweepAvg.append(pctChg)
    if logid == 6: selfServeTrashAvg.append(pctChg)
    if logid == 7: volpakAvg.append(pctChg)
    totalAvg.append(pctChg)
    # TODO: for testing only
    # print(f"{totalAvg}: PctChng")


# calculates shift grade
def gradeEvaluator():
    
    if len(trashAvg) >= 1:
        trashScore = sum(trashAvg) / len(trashAvg)
        print(trashScore)
    if len(selfServeAvg) >= 1: selfServeScore = (sum(selfServeAvg) / len(selfServeAvg))*-1
    if len(tableTouchAvg) >= 1: tableTouchScore = (sum(tableTouchAvg) / len(tableTouchAvg))*-1
    if len(teaRefillAvg) >= 1: teaRefillScore = (sum(teaRefillAvg) / len(teaRefillAvg))*-1
    if len(iceMeltAvg) >= 1: iceMeltScore = (sum(iceMeltAvg) / len(iceMeltAvg))*-1
    if len(spotSweepAvg) >= 1: spotSweepScore = (sum(spotSweepAvg) / len(spotSweepAvg))*-1
    if len(selfServeTrashAvg) >= 1: selfServeTrashScore = (sum(selfServeTrashAvg) / len(selfServeTrashAvg))*-1
    if len(volpakAvg) >= 1: volpakScore = (sum(volpakAvg) / len(volpakAvg))*-1

    if len(trashAvg) >= 1: totalSessionCombinedAvgs = sum(trashAvg+selfServeAvg+tableTouchAvg+teaRefillAvg+iceMeltAvg+spotSweepAvg+selfServeTrashAvg+volpakAvg)
    if len(trashAvg) >= 1: 
        totalTasks = len(trashAvg+selfServeAvg+tableTouchAvg+teaRefillAvg+iceMeltAvg+spotSweepAvg+selfServeTrashAvg+volpakAvg)
        sessionScore = totalSessionCombinedAvgs / totalTasks
    print
    # overall grade
    if len(trashAvg) >= 1:
        sessionScore *= -1
        if sessionScore >= 20: sessionGrade="F"
        elif sessionScore in range(15,20): sessionGrade="D-"
        elif sessionScore in range(10,15): sessionGrade="D"
        elif sessionScore in range(7,10): sessionGrade="D+"
        elif sessionScore in range(5,7): sessionGrade="C-"
        elif sessionScore in range(3,5): sessionGrade="C"
        elif sessionScore in range(2,3): sessionGrade="C+"
        elif sessionScore in range(-1,2): sessionGrade="B-"
        elif sessionScore in range(-4,-1): sessionGrade="B"
        elif sessionScore in range(-7,-4): sessionGrade="B+"
        elif sessionScore in range(-12,-7): sessionGrade="A-"
        elif sessionScore in range(-19,-12): sessionGrade="A"
        elif sessionScore <= -20: sessionGrade="A+"
    # trash grade
    if len(trashAvg) >= 1:
        if trashScore >= 20: trashGrade="F"
        elif trashScore in range(15,20): trashGrade="D-"
        elif trashScore in range(10,15): trashGrade="D"
        elif trashScore in range(7,10): trashGrade="D+"
        elif trashScore in range(5,7): trashGrade="C-"
        elif trashScore in range(3,5): trashGrade="C"
        elif trashScore in range(2,3): trashGrade="C+"
        elif trashScore in range(-1,2): trashGrade="B-"
        elif trashScore in range(-4,-1): trashGrade="B"
        elif trashScore in range(-7,-4): trashGrade="B+"
        elif trashScore in range(-12,-7): trashGrade="A-"
        elif trashScore in range(-19,-12): trashGrade="A"
        elif trashScore <= -20: trashGrade="A+"
    # selfServe grade
    if len(selfServeAvg) >= 1:
        if selfServeScore >= 20: selfServeGrade="F"
        elif selfServeScore in range(15,20): selfServeGrade="D-"
        elif selfServeScore in range(10,15): selfServeGrade="D"
        elif selfServeScore in range(7,10): selfServeGrade="D+"
        elif selfServeScore in range(5,7): selfServeGrade="C-"
        elif selfServeScore in range(3,5): selfServeGrade="C"
        elif selfServeScore in range(2,3): selfServeGrade="C+"
        elif selfServeScore in range(-1,2): selfServeGrade="B-"
        elif selfServeScore in range(-4,-1): selfServeGrade="B"
        elif selfServeScore in range(-7,-4): selfServeGrade="B+"
        elif selfServeScore in range(-12,-7): selfServeGrade="A-"
        elif selfServeScore in range(-19,-12): selfServeGrade="A"
        elif selfServeScore <= -20: selfServeGrade="A+"
    # tableTouch grade
    if len(tableTouchAvg) >= 1:
        if tableTouchScore >= 20: tableTouchGrade="F"
        elif tableTouchScore in range(15,20): tableTouchGrade="D-"
        elif tableTouchScore in range(10,15): tableTouchGrade="D"
        elif tableTouchScore in range(7,10): tableTouchGrade="D+"
        elif tableTouchScore in range(5,7): tableTouchGrade="C-"
        elif tableTouchScore in range(3,5): tableTouchGrade="C"
        elif tableTouchScore in range(2,3): tableTouchGrade="C+"
        elif tableTouchScore in range(-1,2): tableTouchGrade="B-"
        elif tableTouchScore in range(-4,-1): tableTouchGrade="B"
        elif tableTouchScore in range(-7,-4): tableTouchGrade="B+"
        elif tableTouchScore in range(-12,-7): tableTouchGrade="A-"
        elif tableTouchScore in range(-19,-12): tableTouchGrade="A"
        elif tableTouchScore <= -20: tableTouchGrade="A+"
    # teaRefill grade
    if len(teaRefillAvg) >= 1:
        if teaRefillScore >= 20: teaRefillGrade="F"
        elif teaRefillScore in range(15,20): teaRefillGrade="D-"
        elif teaRefillScore in range(10,15): teaRefillGrade="D"
        elif teaRefillScore in range(7,10): teaRefillGrade="D+"
        elif teaRefillScore in range(5,7): teaRefillGrade="C-"
        elif teaRefillScore in range(3,5): teaRefillGrade="C"
        elif teaRefillScore in range(2,3): teaRefillGrade="C+"
        elif teaRefillScore in range(-1,2): teaRefillGrade="B-"
        elif teaRefillScore in range(-4,-1): teaRefillGrade="B"
        elif teaRefillScore in range(-7,-4): teaRefillGrade="B+"
        elif teaRefillScore in range(-12,-7): teaRefillGrade="A-"
        elif teaRefillScore in range(-19,-12): teaRefillGrade="A"
        elif teaRefillScore <= -20: teaRefillGrade="A+"
    # iceMelt grade
    if len(iceMeltAvg) >= 1:
        if iceMeltScore >= 20: iceMeltGrade="F"
        elif iceMeltScore in range(15,20): iceMeltGrade="D-"
        elif iceMeltScore in range(10,15): iceMeltGrade="D"
        elif iceMeltScore in range(7,10): iceMeltGrade="D+"
        elif iceMeltScore in range(5,7): iceMeltGrade="C-"
        elif iceMeltScore in range(3,5): iceMeltGrade="C"
        elif iceMeltScore in range(2,3): iceMeltGrade="C+"
        elif iceMeltScore in range(-1,2): iceMeltGrade="B-"
        elif iceMeltScore in range(-4,-1): iceMeltGrade="B"
        elif iceMeltScore in range(-7,-4): iceMeltGrade="B+"
        elif iceMeltScore in range(-12,-7): iceMeltGrade="A-"
        elif iceMeltScore in range(-19,-12): iceMeltGrade="A"
        elif iceMeltScore <= -20: iceMeltGrade="A+"
    # spotSweep grade
    if len(spotSweepAvg) >= 1:
        if spotSweepScore >= 20: spotSweepGrade="F"
        elif spotSweepScore in range(15,20): spotSweepGrade="D-"
        elif spotSweepScore in range(10,15): spotSweepGrade="D"
        elif spotSweepScore in range(7,10): spotSweepGrade="D+"
        elif spotSweepScore in range(5,7): spotSweepGrade="C-"
        elif spotSweepScore in range(3,5): spotSweepGrade="C"
        elif spotSweepScore in range(2,3): spotSweepGrade="C+"
        elif spotSweepScore in range(-1,2): spotSweepGrade="B-"
        elif spotSweepScore in range(-4,-1): spotSweepGrade="B"
        elif spotSweepScore in range(-7,-4): spotSweepGrade="B+"
        elif spotSweepScore in range(-12,-7): spotSweepGrade="A-"
        elif spotSweepScore in range(-19,-12): spotSweepGrade="A"
        elif spotSweepScore <= -20: spotSweepGrade="A+"
    # selfServeTrash grade
    if len(selfServeTrashAvg) >= 1: 
        if selfServeTrashScore >= 20: selfServeTrashGrade="F"
        elif selfServeTrashScore in range(15,20): selfServeTrashGrade="D-"
        elif selfServeTrashScore in range(10,15): selfServeTrashGrade="D"
        elif selfServeTrashScore in range(7,10): selfServeTrashGrade="D+"
        elif selfServeTrashScore in range(5,7): selfServeTrashGrade="C-"
        elif selfServeTrashScore in range(3,5): selfServeTrashGrade="C"
        elif selfServeTrashScore in range(2,3): selfServeTrashGrade="C+"
        elif selfServeTrashScore in range(-1,2): selfServeTrashGrade="B-"
        elif selfServeTrashScore in range(-4,-1): selfServeTrashGrade="B"
        elif selfServeTrashScore in range(-7,-4): selfServeTrashGrade="B+"
        elif selfServeTrashScore in range(-12,-7): selfServeTrashGrade="A-"
        elif selfServeTrashScore in range(-19,-12): selfServeTrashGrade="A"
        elif selfServeTrashScore <= -20: selfServeTrashGrade="A+"
    # volpak grade
    # TODO: Solve Error Before Update
    # File "c:\Dev\diningbot_v1.2test.py", line 596, in gradeEvaluator
    # shiftSummary(sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade, iceMeltGrade, spotSweepGrade, selfServeTrashGrade, volpakGrade)
    # UnboundLocalError: local variable 'volpakGrade' referenced before assignment
    if len(volpakAvg) >= 1:
        if volpakScore >= 20: volpakGrade="F"
        elif volpakScore in range(15,20): volpakGrade="D-"
        elif volpakScore in range(10,15): volpakGrade="D"
        elif volpakScore in range(7,10): volpakGrade="D+"
        elif volpakScore in range(5,7): volpakGrade="C-"
        elif volpakScore in range(3,5): volpakGrade="C"
        elif volpakScore in range(2,3): volpakGrade="C+"
        elif volpakScore in range(-1,2): volpakGrade="B-"
        elif volpakScore in range(-4,-1): volpakGrade="B"
        elif volpakScore in range(-7,-4): volpakGrade="B+"
        elif volpakScore in range(-12,-7): volpakGrade="A-"
        elif volpakScore in range(-19,-12): volpakGrade="A"
        elif volpakScore <= -20: volpakGrade="A+"

    # TODO: Finish Crash Proofing
    
    if len(selfServeAvg) < 1: shiftSummary(totalSessionCombinedAvgs, sessionGrade, trashGrade)
    elif len(tableTouchAvg) < 1: shiftSummary(totalSessionCombinedAvgs, sessionGrade, trashGrade, selfServeGrade)
    elif len(teaRefillAvg) < 1: shiftSummary(totalSessionCombinedAvgs, sessionGrade, trashGrade, selfServeGrade, tableTouchGrade)
    elif len(iceMeltAvg) < 1: shiftSummary(totalSessionCombinedAvgs, sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade)
    elif len(spotSweepAvg) < 1: shiftSummary(totalSessionCombinedAvgs, sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade, iceMeltGrade)
    elif len(selfServeTrashAvg) < 1: shiftSummary(totalSessionCombinedAvgs, sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade, iceMeltGrade, spotSweepGrade)
    elif len(volpakAvg) < 1: shiftSummary(totalSessionCombinedAvgs, sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade, iceMeltGrade, spotSweepGrade, selfServeTrashGrade)
    else: shiftSummary(totalSessionCombinedAvgs, sessionGrade, trashGrade, selfServeGrade, tableTouchGrade, teaRefillGrade, iceMeltGrade, spotSweepGrade, selfServeTrashGrade, volpakGrade)

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
totalAvg = []

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