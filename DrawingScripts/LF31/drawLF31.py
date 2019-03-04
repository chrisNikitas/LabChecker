from PIL import Image, ImageDraw # drawing package
import time # lets us measure time

import MySQLdb # package used to manipulate the database with python
import dbconfig as config # import our database configuration file

#-------------------------------------------------------------------------------

# define it all in a function:
def diffImDrawer():
#-------------------------------------------------------------------------------

  # set start for time measurement:
  start = time.time()

#-------------------------------------------------------------------------------

  # define colours for easy reference:
  background = (4, 20, 45, 0)
  roomLines = (0, 0, 120)
  computerDesks = (100, 50, 0)
    # node colours: 
  nodeRed = (255, 0, 0)
  nodeYellow = (255, 255, 0)
  nodeGreen = (0, 255, 0)

#-------------------------------------------------------------------------------

  # define basic images/backgrounds and set drawing canvases
  cS = 2000 # cS = canvasSize
  staffImg = Image.new('RGBA', (cS,cS), color = background)
  staffDraw = ImageDraw.Draw(staffImg)

  studentImg = Image.new('RGBA', (cS,cS), color = background)
  studentDraw = ImageDraw.Draw(studentImg)

  # define line widths
  wallWidth = int(0.01*cS)
  tableWidth = int(0.005*cS)

#-------------------------------------------------------------------------------

  # define coordinates for easy reference:
    # horizontals:
  a = int(0.2*cS)
  b = int(0.4*cS)
  c = int(0.6*cS)
  d = int(0.8*cS)
    # verticals:
  v = int(0.25*cS)
  w = int(0.45*cS)
  x = int(0.55*cS)
  y = int(0.75*cS)
  z = int(0.65*cS)

#-------------------------------------------------------------------------------

  # draw lines for room outline:
  staffDraw.line((0.1*cS,0.2*cS,0.9*cS,0.2*cS),fill=roomLines, width=wallWidth)
  staffDraw.line((0.1*cS,0.2*cS,0.1*cS,0.8*cS),fill=roomLines, width=wallWidth)
  staffDraw.line((0.1*cS,0.8*cS,0.7*cS,0.8*cS),fill=roomLines, width=wallWidth)
  staffDraw.line((0.7*cS,0.8*cS,0.7*cS,0.5*cS),fill=roomLines, width=wallWidth)
  staffDraw.line((0.7*cS,0.5*cS,0.775*cS,0.5*cS),fill=roomLines, width=wallWidth)
  staffDraw.line((0.825*cS,0.5*cS,0.9*cS,0.5*cS),fill=roomLines, width=wallWidth)
  staffDraw.line((0.9*cS,0.5*cS,0.9*cS,0.2*cS),fill=roomLines, width=wallWidth)

  studentDraw.line((0.1*cS,0.2*cS,0.9*cS,0.2*cS),fill=roomLines, width=wallWidth)
  studentDraw.line((0.1*cS,0.2*cS,0.1*cS,0.8*cS),fill=roomLines, width=wallWidth)
  studentDraw.line((0.1*cS,0.8*cS,0.7*cS,0.8*cS),fill=roomLines, width=wallWidth)
  studentDraw.line((0.7*cS,0.8*cS,0.7*cS,0.5*cS),fill=roomLines, width=wallWidth)
  studentDraw.line((0.7*cS,0.5*cS,0.775*cS,0.5*cS),fill=roomLines, width=wallWidth)
  studentDraw.line((0.825*cS,0.5*cS,0.9*cS,0.5*cS),fill=roomLines, width=wallWidth)
  studentDraw.line((0.9*cS,0.5*cS,0.9*cS,0.2*cS),fill=roomLines, width=wallWidth)

  # draw lines for door:
  staffDraw.line((0.775*cS,0.475*cS,0.825*cS,0.5*cS),fill=roomLines, width=wallWidth)
  studentDraw.line((0.775*cS,0.475*cS,0.825*cS,0.5*cS),fill=roomLines, width=wallWidth)


#-------------------------------------------------------------------------------

  # draw lines for computer tables:
  staffDraw.line((a,v,a,w),fill=computerDesks, width=tableWidth)
  staffDraw.line((b,v,b,w),fill=computerDesks, width=tableWidth)
  staffDraw.line((c,v,c,w),fill=computerDesks, width=tableWidth)
  staffDraw.line((d,v,d,w),fill=computerDesks, width=tableWidth)
  staffDraw.line((a,x,a,y),fill=computerDesks, width=tableWidth)
  staffDraw.line((b,x,b,y),fill=computerDesks, width=tableWidth)
  staffDraw.line((c,x,c,z),fill=computerDesks, width=tableWidth)

  studentDraw.line((a,v,a,w),fill=computerDesks, width=tableWidth)
  studentDraw.line((b,v,b,w),fill=computerDesks, width=tableWidth)
  studentDraw.line((c,v,c,w),fill=computerDesks, width=tableWidth)
  studentDraw.line((d,v,d,w),fill=computerDesks, width=tableWidth)
  studentDraw.line((a,x,a,y),fill=computerDesks, width=tableWidth)
  studentDraw.line((b,x,b,y),fill=computerDesks, width=tableWidth)
  studentDraw.line((c,x,c,z),fill=computerDesks, width=tableWidth)

#-------------------------------------------------------------------------------

  # draw node lines on computer tables:
  # xrange function creates iterable object rather than whole list
  # it is therefore much more efficient and should lead to quicker drawing

  # define int values so we can use xrange rather than using yield to write our 
  # own xrange function:

  numA = int(0.2*cS)
  numB = int(0.801*cS)
  numC = int(0.01*cS)
  numD = int(0.036*cS)
  numE = int(0.025*cS)
  numF = int(0.401*cS)
  numG = int(0.575*cS)
  numH = int(0.625*cS)
  numI = int(0.6*cS)

    # for top row of computer desks:
  for i in xrange(numA, numB, numA):                             # for each column
    for j in xrange(v+numC, w, numD):                               # for each row
      staffDraw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth) 
      studentDraw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth) 


    # for first two columns of bottom row of computer desks:
  for i in xrange(numA, numF, numA):                             # for each column
    for j in xrange(x+numC, y, numD):                               # for each row
      staffDraw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth)
      studentDraw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth)


    # for final column of bottom row of computer desks:
  for j in xrange(x+numC, z, numD):                                 # for each row
    staffDraw.line((numG, j, numI, j),fill=computerDesks, width=tableWidth) # draw a line
    studentDraw.line((numG, j, numI, j),fill=computerDesks, width=tableWidth) # draw a line


#-------------------------------------------------------------------------------

  # create and populate array of tuples representing node coordinates:
  nodeCoords = []                                     # array for node coordinates

  # we will reuse previously defined int values so we can use xrange

    # for top row of computer desks:
  for i in xrange(numA, numB, numA):                             # for each column
    for j in xrange(v+numC, w, numD):                               # for each row
      nodeCoords.append((i-numE, j))                    # add node coords to array
      nodeCoords.append((i+numE, j))                    # add node coords to array

    # for first two columns of bottom row of computer desks:
  for i in xrange(numA, numF, numA):                             # for each column
    for j in xrange(x+numC, y, numD):                               # for each row
      nodeCoords.append((i-numE, j))                    # add node coords to array
      nodeCoords.append((i+numE, j))                    # add node coords to array

    # for final column of bottom row of computer desks:
  for j in xrange(x+numC, z, numD):                                 # for each row
      nodeCoords.append((numG, j))                      # add node coords to array

#-------------------------------------------------------------------------------

  # draw nodes at each coordinate in array. colours depend on database values:
  # ellipse=((topLeftX,topLeftY,bottomRightX,bottomRightY),fill=colour,outline=colour)

  cursor.execute("SELECT status FROM compStatus") # point cursor to status column

  # define empty strings which we will give values to later:
  colour = (255,255,255)
  nextStatus = ""

  noGroups = True
  if len(desiredGroups) != 0: # if there is no lab scheduled at the current time
    noGroups = False

  for node in nodeCoords:
    # calculate node colour based off of status from database:
    nextStatus = cursor.fetchone()  # this returns a tuple in which the first value is the colour of that seat

    if noGroups: # if there is no lab scheduled at the current time
      try:
        if nextStatus[0] == "empty":                   # if the computer is free
          colour = nodeGreen
        else:
          colour = nodeYellow              # if occupied by someone who shouldn't be there
      except:
        print ""

    else: # if there is a lab scheduled right now
      try:
        if nextStatus[0] == "empty":                   # if the computer is free
          colour = nodeGreen
        elif nextStatus in desiredGroups: # if occupied by desired lab group
          colour = nodeYellow
        else:
          colour = nodeRed              # if occupied by someone who shouldn't be there
      except:
        print ""
    # draw the node with the set colour:
    staffDraw.ellipse((node[0]-numC, node[1]-numC, node[0]+numC, node[1]+numC), fill = colour, outline = (0,0,0))



  # draw nodes on student image:
    if nextStatus[0] == "empty":                   # if the computer is free
        studentDraw.ellipse((node[0]-numC, node[1]-numC, node[0]+numC, node[1]+numC), fill = nodeGreen, outline = (0,0,0))

    else:
        studentDraw.ellipse((node[0]-numC, node[1]-numC, node[0]+numC, node[1]+numC), fill = nodeRed, outline = (0,0,0))


#-------------------------------------------------------------------------------

  # save as image in current working directory:
  staffImg.save('staffImage.png')
  studentImg.save('studentImage.png')
#-------------------------------------------------------------------------------
  end = time.time()
  print 'took', end - start, 'seconds to draw and save images'

#-------------------------------------------------------------------------------





















#-------------------------------------------------------------------------------

# define it all in a function:
def sameImDrawer():
#-------------------------------------------------------------------------------

  # set start for time measurement:
  start = time.time()

#-------------------------------------------------------------------------------

  # define colours for easy reference:
  background = (4, 20, 45, 0)
  roomLines = (0, 0, 120)
  computerDesks = (100, 50, 0)
    # node colours: 
  nodeRed = (255, 0, 0)
  nodeYellow = (255, 255, 0)
  nodeGreen = (0, 255, 0)

#-------------------------------------------------------------------------------

  # define basic images/backgrounds and set drawing canvases
  cS = 2000 # cS = canvasSize
  img = Image.new('RGBA', (cS,cS), color = background)

  draw = ImageDraw.Draw(img)

  # define line widths
  wallWidth = int(0.01*cS)
  tableWidth = int(0.005*cS)

#-------------------------------------------------------------------------------

  # define coordinates for easy reference:
    # horizontals:
  a = int(0.2*cS)
  b = int(0.4*cS)
  c = int(0.6*cS)
  d = int(0.8*cS)
    # verticals:
  v = int(0.25*cS)
  w = int(0.45*cS)
  x = int(0.55*cS)
  y = int(0.75*cS)
  z = int(0.65*cS)

#-------------------------------------------------------------------------------

  # draw lines for room outline:
  draw.line((0.1*cS,0.2*cS,0.9*cS,0.2*cS),fill=roomLines, width=wallWidth)
  draw.line((0.1*cS,0.2*cS,0.1*cS,0.8*cS),fill=roomLines, width=wallWidth)
  draw.line((0.1*cS,0.8*cS,0.7*cS,0.8*cS),fill=roomLines, width=wallWidth)
  draw.line((0.7*cS,0.8*cS,0.7*cS,0.5*cS),fill=roomLines, width=wallWidth)
  draw.line((0.7*cS,0.5*cS,0.9*cS,0.5*cS),fill=roomLines, width=wallWidth)
  draw.line((0.9*cS,0.5*cS,0.9*cS,0.2*cS),fill=roomLines, width=wallWidth)


#-------------------------------------------------------------------------------

  # draw lines for computer tables:
  draw.line((a,v,a,w),fill=computerDesks, width=tableWidth)
  draw.line((b,v,b,w),fill=computerDesks, width=tableWidth)
  draw.line((c,v,c,w),fill=computerDesks, width=tableWidth)
  draw.line((d,v,d,w),fill=computerDesks, width=tableWidth)
  draw.line((a,x,a,y),fill=computerDesks, width=tableWidth)
  draw.line((b,x,b,y),fill=computerDesks, width=tableWidth)
  draw.line((c,x,c,z),fill=computerDesks, width=tableWidth)


#-------------------------------------------------------------------------------

  # draw node lines on computer tables:
  # xrange function creates iterable object rather than whole list
  # it is therefore much more efficient and should lead to quicker drawing

  # define int values so we can use xrange rather than using yield to write our 
  # own xrange function:

  numA = int(0.2*cS)
  numB = int(0.801*cS)
  numC = int(0.01*cS)
  numD = int(0.036*cS)
  numE = int(0.025*cS)
  numF = int(0.401*cS)
  numG = int(0.575*cS)
  numH = int(0.625*cS)
  numI = int(0.6*cS)

    # for top row of computer desks:
  for i in xrange(numA, numB, numA):                             # for each column
    for j in xrange(v+numC, w, numD):                               # for each row
      draw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth) 


    # for first two columns of bottom row of computer desks:
  for i in xrange(numA, numF, numA):                             # for each column
    for j in xrange(x+numC, y, numD):                               # for each row
      draw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth)


    # for final column of bottom row of computer desks:
  for j in xrange(x+numC, z, numD):                                 # for each row
    draw.line((numG, j, numI, j),fill=computerDesks, width=tableWidth) # draw a line


#-------------------------------------------------------------------------------

  # create and populate array of tuples representing node coordinates:
  nodeCoords = []                                     # array for node coordinates

  # we will reuse previously defined int values so we can use xrange

    # for top row of computer desks:
  for i in xrange(numA, numB, numA):                             # for each column
    for j in xrange(v+numC, w, numD):                               # for each row
      nodeCoords.append((i-numE, j))                    # add node coords to array
      nodeCoords.append((i+numE, j))                    # add node coords to array

    # for first two columns of bottom row of computer desks:
  for i in xrange(numA, numF, numA):                             # for each column
    for j in xrange(x+numC, y, numD):                               # for each row
      nodeCoords.append((i-numE, j))                    # add node coords to array
      nodeCoords.append((i+numE, j))                    # add node coords to array

    # for final column of bottom row of computer desks:
  for j in xrange(x+numC, z, numD):                                 # for each row
      nodeCoords.append((numG, j))                      # add node coords to array

#-------------------------------------------------------------------------------

  # draw nodes at each coordinate in array. colours depend on database values:
  # ellipse=((topLeftX,topLeftY,bottomRightX,bottomRightY),fill=colour,outline=colour)

  cursor.execute("SELECT status FROM compStatus") # point cursor to status column

  # define empty strings which we will give values to later:
  colour = (255,255,255)
  nextStatus = ""

  noGroups = True
  if len(desiredGroups) != 0: # if there is no lab scheduled at the current time
    noGroups = False

  for node in nodeCoords:
    # calculate node colour based off of status from database:
    nextStatus = cursor.fetchone()  # this returns a tuple in which the first value is the colour of that seat

    if noGroups: # if there is no lab scheduled at the current time
      try:
        if nextStatus[0] == "empty":                   # if the computer is free
          colour = nodeGreen
        else:
          colour = nodeYellow              # if occupied by someone who shouldn't be there
      except:
        print ""

    else: # if there is a lab scheduled right now
      try:
        if nextStatus[0] == "empty":                   # if the computer is free
          colour = nodeGreen
        elif nextStatus in desiredGroups: # if occupied by desired lab group
          colour = nodeYellow
        else:
          colour = nodeRed              # if occupied by someone who shouldn't be there
      except:
        print ""
    # draw the node with the set colour:
    draw.ellipse((node[0]-numC, node[1]-numC, node[0]+numC, node[1]+numC), fill = colour, outline = (0,0,0))


#-------------------------------------------------------------------------------

  # save as image in current working directory:
  img.save('staffImage.png')
  img.save('studentImage.png')
#-------------------------------------------------------------------------------
  end = time.time()
  print 'took', end - start, 'seconds to draw and save images'

#-------------------------------------------------------------------------------

























# connect to the database and make a cursor:
db = MySQLdb.connect(config.host, config.user, config.passwd, config.database) 
cursor = db.cursor()

#-------------------------------------------------------------------------------


# define array holding the groups which should be here currently by reading from database
# this is only for the staff login though. irrelevant to students
desiredGroups = []
numOfRows = cursor.execute("SELECT COUNT(*) FROM desiredGroups")  # returns number of desired groups

cursor.execute("SELECT groupName FROM desiredGroups") # points cursor to correct place

for i in xrange(0, numOfRows + 1):  # for each row in desiredGroups database
  desiredGroups.append(cursor.fetchone()) # adds group name to array of desired groups

#-------------------------------------------------------------------------------

if len(desiredGroups) == 0:
  sameImDrawer()
else:
  diffImDrawer()

# close database and print time taken to draw and save image
db.close()







