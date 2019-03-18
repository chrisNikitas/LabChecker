# program performs simulation of lab LF31 in kilburn buinding

# Wojciech Czosnyka January - March 2019

from datetime import datetime, timedelta, date
from scipy.integrate import quad
from time import sleep
import numpy
import math
import random
import MySQLdb
import config

# function computing probability that everone from a group entered lab
def enterence (x, peak):
    return (1/(numpy.sqrt(2*numpy.pi*4)))*numpy.e**((-(x-peak)**2)/8)

# function computing probability that everone from a group exited lab
def exit (x, peak):
    if x > peak:
        return (1/(numpy.sqrt(2*numpy.pi*4)))*numpy.e**((-(x-peak)**2)/8)
    else:
        return (1/(numpy.sqrt(2*numpy.pi*400)))*numpy.e**((-(x-peak)**2)/800)

# set up string to text file
def printGroupsToTxt(groups):
    result = ""
    for group in groups:
        result += "\t{}".format(group[1])
    return result

# function places new students on random free space of the lab or removes
# student from the lab if student was more than 30 minutes if not looks for the
# next one or takes the one with the greatest time spent in lab
def placeStudent(difference, group, labIndex):
    # place different number of students (if negative romeve absolute)
    if difference > 0:
        for x in range(0, abs(difference)):
            # find a place if free place a student
            foundSpace = False
            while foundSpace == False:
                seat = random.randint(0,labCapacity[labIndex] - 1)

                if lab[labIndex][seat] == "empty":
                    lab[labIndex][seat] = group[0]
                    # store entry time
                    labEntryTime[labIndex][seat] = math.floor(simulationTime)

                    if group[3] == -1:
                        group[3] = labEntryTime[labIndex][seat]
                    foundSpace = True

    else:
        for x in range(0, abs(difference)):
            # find a place if not empty and student from gib=ven group remove
            # student
            foundSpace = False
            while foundSpace == False:
                seat = random.randint(0,labCapacity[labIndex] - 1)
                if lab[labIndex][seat] == group[0] and \
                     (simulationTime - labEntryTime[labIndex][seat] > 30 or \
                     labEntryTime[labIndex][seat] == group[3]):

                    lab[labIndex][seat] = "empty"
                    labEntryTime[labIndex][seat] = 0
                    findLongest(group, labIndex)
                    foundSpace = True


def findLongest(group,labIndex):
    global labCapacity
    global lab
    global labEntryTime

    group[3] = -1

    for seat in range(labCapacity[labIndex]):
        if lab[labIndex][seat] == group[0] and \
           (labEntryTime[labIndex][seat] < group[3] or group[3] == -1):
            group[3] = labEntryTime[labIndex][seat]

def insertToDB():
    global lab
    global simulationDay
    global simulationTime
    global timetable

    cur.execute("DELETE FROM compStatus")

    for slot in range(0, numpy.amax(labCapacity)):
        reachableSlots = [" ", " ", " "];

        for x in range(0,3):
            if slot < labCapacity[x]:
                reachableSlots[x] = lab[x][slot]

        result = reachableSlots[0] + "," + reachableSlots[1] + "," + reachableSlots[2]
        # add changes to database
        cur.execute(f"INSERT INTO compStatus VALUES (\"{slot + 1}\", \"{result}\")")

    currentGroups = ["-", "-", "-"]

    for x in range(0, 3):
        for slot in timetable[x][simulationDay]:
            if slot[1] > simulationTime and slot[0] < simulationTime:
                currentGroups[x] = slot[2]

    # update the current group in the database
    cur.execute("DELETE FROM desiredGroups")
    cur.execute(f"INSERT INTO desiredGroups VALUES (\"{currentGroups[0]}\"," +
                f"\"{currentGroups[1]}\", \"{currentGroups[2]}\")")

    db.commit()

# connect to group database
db = MySQLdb.connect(config.host,  # your host
                     config.user,       # username
                     config.passwd,     # password
                     config.db)   # name of the database

# create coursor for our database
cur = db.cursor()

# timetable in form the time of start time, finish time, group symbol
# all times are differences from start time to current time
timetable = [[[[120, 240, "K"],    [480, 600, "Y"]                                        ],
              [[840, 960, "X"],    [1020, 1080, "Y"], [1140, 1260, "MW"]                  ],
              [[1380, 1500, "Z"]                                                          ],
              [[2040, 2160, "Y"],  [2160, 2280, "X"]                                      ],
              [[2820, 2940, "MW"], [3120, 3240, "Z"]                                      ],
              [[3780, 3900, "Y"]                                                          ],
              [[4100, 4260, "X"],  [4320, 4380, "Y"], [4440, 4560, "MW"]                  ],
              [[4680, 4800, "Z"]                                                          ],
              [[5340, 5460, "Y"],  [5460, 5580, "X"], [5760, 5880, "G"]                   ],
              [[6120, 6240, "MW"], [6420, 6540, "Z"]                                      ]],


             [[[60, 180, "F"],     [420, 480,"MW"],   [480, 600, "H"]                     ],
              [[720, 840, "F"],    [840, 900, "L"],   [1020, 1140, "F"], [1140, 1260, "G"]],
              [[1380, 1440, "X"],  [1440, 1560, "H"]                                      ],
              [[2040, 2160, "H"],  [2160, 2280, "F"], [2460, 2580, "H"]                   ],
              [[2760, 2820, "L"],  [3060, 3180, "G"]                                      ],
              [[3720, 3780, "MW"], [3780,3900, "H"]                                       ],
              [[4020, 4140, "F"],  [4140, 4200, "L"], [4320, 4440, "F"],                  ],
              [[4680, 4740, "X"],  [4740, 4860, "H"]                                      ],
              [[5340, 5460, "H"],  [5460, 5580, "F"],                                     ],
              [[6060, 6120, "L"],  [6360, 6480, "G"]                                      ]],


             [[[60, 180, "F"]                                                             ],
              [[840,900, "L"],     [1140, 1260, "G"]                                      ],
              [                                                                           ],
              [[2460, 2580, "H"]                                                          ],
              [[2760, 2820, "L"]                                                          ],
              [                                                                           ],
              [[4140, 4200, "L"]                                                          ],
              [                                                                           ],
              [                                                                           ],
              [[6060, 6120, "L"]                                                          ]]]

# groups with number of people currently in the lab from such group in form
# group symbol, currently in lab, in lab in previous step
groups = [[["K", 0, 0, -1], ["Y", 0, 0, -1], ["X", 0, 0, -1], ["MW", 0, 0, -1],
           ["Z", 0, 0, -1], ["G", 0, 0, -1], ["F", 0, 0, -1], ["H", 0, 0, -1],
           ["L", 0, 0, -1]],

          [["K", 0, 0, -1], ["Y", 0, 0, -1], ["X", 0, 0, -1], ["MW", 0, 0, -1],
           ["Z", 0, 0, -1], ["G", 0, 0, -1], ["F", 0, 0, -1], ["H", 0, 0, -1],
           ["L", 0, 0, -1]],

          [["K", 0, 0, -1], ["Y", 0, 0, -1], ["X", 0, 0, -1], ["MW", 0, 0, -1],
           ["Z", 0, 0, -1], ["G", 0, 0, -1], ["F", 0, 0, -1], ["H", 0, 0, -1],
           ["L", 0, 0, -1]]]

# array representng the computers in a lab and the time they got into
lab = ["empty"] * 75, ["empty"] * 53, ["empty"] * 50
labEntryTime = [0] * 75, [0] * 53, [0] * 50

# initilize start time of the simulation
startTime = datetime.now()

# day in simulation in range 0 to 10 (2 weeks without weekends)
simulationDay = 0

# current time to compare with start time and compute simulation time
currentTime = datetime.now()

# initialize simulation time as difference between start and current time
simulationTime = (currentTime - startTime).total_seconds()

# capacity of the lab
labCapacity = [75, 53, 50]

# number of people currently in lab and in previous step
currentlyInLab = [0, 0, 0]
previouslyInLab = [0, 0, 0]

# initialization of connection and start of check file (to check statistics
# of a simultion)
file = open('dataToAnalyse.txt', 'w')
file.write("# of people \tK \tY \tX \tMW \tZ \tG \t\ttime")
file.close()

# main program creating simulation
def computeLab(labIndex):
    global currentTime
    global startTime
    global simulationTime
    global db
    global cur
    global simulationDay
    global currentlyInLab
    global previouslyInLab
    global groups
    global timetable
    global lab
    global labEntryTime
    global labCapacity

    # set up values for previous variables to start simulation step
    for group in groups[labIndex]:
        group[2] = group[1]

    previouslyInLab[labIndex] = currentlyInLab[labIndex]

    # initialize new number of people in lab
    currentlyInLab[labIndex] = 0

    # compute the simulation time
    currentTime = datetime.now()
    simulationTime = (currentTime - startTime).total_seconds()

    # compute the numbers for groups that has lab in less then 40 minutes or
    # had lab in such time
    for slot in timetable[labIndex][simulationDay]:
        if slot[1] > simulationTime - 40 and slot[0] <= simulationTime + 40:
            # compute the probabilities
            enterenceProbability, err = quad(enterence, slot[0] - 40, simulationTime, args = (slot[0]))
            exitProbability, err = quad(exit, slot[1] - 40, simulationTime, args = (slot[1]))

            # dealing with errors that could occur
            if enterenceProbability > 1:
                enterenceProbability = 1
            if exitProbability > 1:
                exitProbability = 1
            if enterenceProbability < 0:
                enterenceProbability = 0
            if exitProbability < 0:
                exitProbability = 0

            # comuting number of people from each group
            numberOfPeople = round(labCapacity[labIndex] * (enterenceProbability - exitProbability))

            # assigning computed umber of people to proper group
            for group in groups[labIndex]:
                if group[0] == slot[2]:
                    group[1] = numberOfPeople

    # initializing the current group so the group that has currenty lab
    currentGroup = ""

    # computing current group and assigning new places for current group
    for group in groups[labIndex]:
        for slot in timetable[labIndex][simulationDay]:
            # if group has currently labs assign it to the current group
            if group[0] == slot[2] and slot[0] < simulationTime  and slot[1] > simulationTime:
                currentGroup = group[0]
                currentlyInLab[labIndex] += group[1];

                # compute how many new people get to lab in this step
                difference = group[1] - group[2]

                # place that many people in a lab from current group (if
                # negative remove the absolute)
                if difference > 0:
                    for x in range(0, abs(difference)):
                        # if lab was not full place students there if was remove
                        # people from different group and place from current
                        foundSpace = False
                        if previouslyInLab[labIndex] < labCapacity[labIndex]:
                            while foundSpace == False:
                                # place the student and update the counter
                                seat = random.randint(0, labCapacity[labIndex] - 1)
                                if lab[labIndex][seat] == "empty":
                                    lab[labIndex][seat] = group[0]
                                    labEntryTime[labIndex][seat] = math.floor(simulationTime)

                                    if group[3] == -1:
                                        group[3] = labEntryTime[labIndex][seat]

                                    foundSpace = True
                                    previouslyInLab[labIndex] += 1
                        else:
                            while foundSpace == False:
                                # take random studnet check group and place
                                # from curremt group instead
                                seat = random.randint(0, labCapacity[labIndex] - 1)
                                if lab[labIndex][seat] != group[0]:
                                    for groupProposition in groups[labIndex]:
                                        if groupProposition[0] == lab[labIndex][seat] \
                                             and (simulationTime - labEntryTime[labIndex][seat] > 30 \
                                             or labEntryTime[labIndex][seat] == groupProposition[3]):
                                            groupProposition[2] -= 1
                                            labEntryTime[labIndex][seat] = math.floor(simulationTime)
                                            lab[labIndex][seat] = group[0]
                                            findLongest(groupProposition, labIndex)
                                            foundSpace = True
                # remove students from current group
                else:
                    for x in range(0, abs(difference)):
                        foundSpace = False
                        while foundSpace == False:
                            seat = random.randint(0,labCapacity[labIndex] - 1)
                            if lab[labIndex][seat] == group[0] and  \
                                 (simulationTime - labEntryTime[labIndex][seat] > 30 or \
                                 labEntryTime[labIndex][seat] == group[3]):
                                lab[labIndex][seat] = "empty"
                                labEntryTime[labIndex][seat] = 0
                                group[2] -= 1
                                findLongest(group, labIndex)
                                foundSpace = True


    # add students from previous step to lab currently
    for group in groups[labIndex]:
        if currentGroup != group[0]:
            currentlyInLab[labIndex] += group[2]

    #print ("-----------------------------------------------------------")
    #print (currentGroup)
    #print (groups)
    #print (lab)
    #print ("-----------------------------------------------------------")
    # add to people currently in lab people the get here via function in the
    # begiinning
    for group in groups[labIndex]:
        if currentGroup != group[0]:
            # if there is space add them to number in lab if not resize the set
            # to maximum available resize
            if (group[1] - group[2]) + currentlyInLab[labIndex] > labCapacity[labIndex]:
                if  group[2] + (labCapacity[labIndex] - currentlyInLab[labIndex]) < 0:
                    currentlyInLab[labIndex] -= group[2]
                    group[1] = 0
                else:
                    group[1] = group[2] + (labCapacity[labIndex] - currentlyInLab[labIndex])
                    currentlyInLab[labIndex] = labCapacity[labIndex]
            else:
                currentlyInLab[labIndex] += (group[1] - group[2])
        if group[0] != currentGroup:
            if group[1] != group[2]:
                placeStudent(group[1] - group[2], group, labIndex)


    # make some random changes in lab the number of changes is half of all
    # empty seats
    emptyLabSeats = int(math.ceil(0.2*(labCapacity[labIndex] - currentlyInLab[labIndex])))

    # make these changes
    for x in range(emptyLabSeats):
        # take a random group
        randomGroup = random.randint(0,8)

        # comupte the change the more people in lab the more likely decrease is
        change = 0
        if groups[labIndex][randomGroup][1] > 0 and groups[labIndex][randomGroup][0] != currentGroup:
            if random.randint(0,labCapacity[labIndex]) > currentlyInLab[labIndex]: change = 1
            else: change = -1
        elif groups[labIndex][randomGroup][0] != currentGroup:
            change = 1

        # execute the change
        #print (lab)
        placeStudent(change, groups[labIndex][randomGroup], labIndex)
        #print (lab)
        currentlyInLab[labIndex] += change
        groups[labIndex][randomGroup][1] += change

    # output the state to the sreen
    print (f"{currentlyInLab[labIndex]}\t{groups[labIndex]}\t\t{simulationTime}\t{simulationDay}")

    # output changes to file
    file = open('dataToAnalyse.txt', 'a')
    file.write('\n{}\t{}\t\t{}'.format(currentlyInLab[labIndex], printGroupsToTxt(groups[labIndex]),simulationTime))
    file.close()

while True:
    computeLab(0)
    computeLab(1)
    computeLab(2)
    insertToDB()

    # wait till next xecond to perform next step
    previousSimulationTime = math.ceil(simulationTime)
    while math.floor(simulationTime) < previousSimulationTime:
        sleep(0.001)
        currentTime = datetime.now()
        simulationTime = (currentTime - startTime).total_seconds()

    # check if day ended (each day is from 8am to 7pm so 660 minutes)
    if math.floor(simulationTime / 660) != simulationDay:
        # if whole 2 weeks finished restart simulation
        if math.floor(simulationTime) >= 6600:
            simulationDay = 0
            startTime = datetime.now()
        else:
            simulationDay += 1

        # remove everybody from lab
        for x in range(3):
            for group in groups[x]:
                group[1] = 0
                group[2] = 0
                group[3] = -1

        # restart all the labs
        lab = ["empty"] * 75, ["empty"] * 53, ["empty"] * 50
        labEntryTime = [0] * 75, [0] * 53, [0] * 50

        currentlyInLab = [0, 0, 0]
