from PIL import Image, ImageDraw # drawing package
import time # lets us measure time

from random import randint

import MySQLdb # package used to manipulate the database with python
import dbconfig as config # import our database configuration file

#-------------------------------------------------------------------------------

# define it all in a function:
def imDrawer():
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
  cWidth = int(0.6*cS)
  cHeight = int(0.8*cS)
  staffImg = Image.new('RGBA', (cWidth,cHeight), color = background)
  staffDraw = ImageDraw.Draw(staffImg)

  studentImg = Image.new('RGBA', (cWidth,cHeight), color = background)
  studentDraw = ImageDraw.Draw(studentImg)

  # define line widths
  wallWidth = int(0.01*cS)
  tableWidth = int(0.005*cS)

#-------------------------------------------------------------------------------

  # define values for easy reference:
    # horizontals:
  a = int(0.005*cWidth) # 200/1000
  b = int(0.45*cWidth) # 450/1000
  b2 = int(0.455*cWidth) # 450/1000
  c = int(0.995*cWidth) # 800/1000
  d = int(0.05*cWidth) # 250/1000
  e = int(0.32*cWidth) # 400/1000
  f = int(0.59*cWidth) # 550/1000
  g = int(0.86*cWidth) # 700/1000

    # verticals:
  r = int(0.025*cHeight) # 110/1000
  s = int(0.425*cHeight) # 440/1000
  t = int(0.49*cHeight) # 490/1000
  u = int(0.575*cHeight) # 560/1000
  v = int(0.89*cHeight) # 815/1000
  w = int(0.975*cHeight) # 890/1000
  x = int(0.005*cHeight) # 100/1000
  y = int(0.55*cHeight) # 550/1000
  z = int(0.995*cHeight) # 900/1000

    # numbers for drawing node lines:
  numA = int(0.585*cHeight) # 575/1000
  numB = int(0.035*cHeight) # 125/1000
  numC = int(0.50*cHeight) # 500/1000
  
    # numbers for drawing node lines:
  nodeStep = int(0.095*cHeight) # 75/1000, vertical distance between node lines
  nodeWidth = int(0.035*cWidth) # 25/1000, width of a node line on each side of table
  tableGap = int(0.27*cWidth) # 150/1000
  nodeRadius = int(0.01*cHeight)

    # numbers for drawing doors:
  doorStart = int(0.2*cWidth) # 350/1000
  doorEnd = int(0.3*cWidth) # 400/1000
  doorHeight = int(0.95*cHeight) # 850/1000
#-------------------------------------------------------------------------------

  # draw lines for room outline:
  staffDraw.line((0,y,b2,y),fill=roomLines, width=wallWidth)
  staffDraw.line((b,y,b,0),fill=roomLines, width=wallWidth)
  staffDraw.line((b,x,cWidth,x),fill=roomLines, width=wallWidth)
  staffDraw.line((c,x,c,cHeight),fill=roomLines, width=wallWidth)
  staffDraw.line((c,z,doorEnd,z),fill=roomLines, width=wallWidth)
  staffDraw.line((doorStart,z,0,z),fill=roomLines, width=wallWidth)
  staffDraw.line((a,z,a,y),fill=roomLines, width=wallWidth)

  studentDraw.line((0,y,b2,y),fill=roomLines, width=wallWidth)
  studentDraw.line((b,y,b,0),fill=roomLines, width=wallWidth)
  studentDraw.line((b,x,cWidth,x),fill=roomLines, width=wallWidth)
  studentDraw.line((c,x,c,cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((c,z,doorEnd,z),fill=roomLines, width=wallWidth)
  studentDraw.line((doorStart,z,0,z),fill=roomLines, width=wallWidth)
  studentDraw.line((a,z,a,y),fill=roomLines, width=wallWidth)

  # draw lines for door:
  staffDraw.line((doorStart,z,doorEnd,doorHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((doorStart,z,doorEnd,doorHeight),fill=roomLines, width=wallWidth)

#-------------------------------------------------------------------------------

  # draw lines for computer tables:
  staffDraw.line((d,u,d,w),fill=computerDesks, width=tableWidth)
  staffDraw.line((e,u,e,v),fill=computerDesks, width=tableWidth)
  staffDraw.line((f,r,f,s),fill=computerDesks, width=tableWidth)
  staffDraw.line((f,t,f,v),fill=computerDesks, width=tableWidth)
  staffDraw.line((g,r,g,s),fill=computerDesks, width=tableWidth)
  staffDraw.line((g,t,g,v),fill=computerDesks, width=tableWidth)

  studentDraw.line((d,u,d,w),fill=computerDesks, width=tableWidth)
  studentDraw.line((e,u,e,v),fill=computerDesks, width=tableWidth)
  studentDraw.line((f,r,f,s),fill=computerDesks, width=tableWidth)
  studentDraw.line((f,t,f,v),fill=computerDesks, width=tableWidth)
  studentDraw.line((g,r,g,s),fill=computerDesks, width=tableWidth)
  studentDraw.line((g,t,g,v),fill=computerDesks, width=tableWidth)

#-------------------------------------------------------------------------------

  # draw node lines on computer tables and add coordinates of nodes to array:
  # xrange function creates iterable object rather than whole list
  # it is therefore much more efficient and should lead to quicker drawing

  # define int values so we can use xrange rather than using yield to write our 
  # own xrange function:



  nodeCoords = []                                     # array for node coordinates




    # for bottom row, first column of computer desks:
  for j in xrange(numA, w, nodeStep):                             # for each row
    staffDraw.line((d, j, d+nodeWidth, j),fill=computerDesks, width=tableWidth) 
    studentDraw.line((d, j, d+nodeWidth, j),fill=computerDesks, width=tableWidth) 
    nodeCoords.append((d+nodeWidth, j))


    # for bottom row, second column of computer desks:
  for j in xrange(numA, v, nodeStep):                               # for each row
    staffDraw.line((e-nodeWidth,j,e+nodeWidth,j),fill=computerDesks, width=tableWidth)
    studentDraw.line((e-nodeWidth,j,e+nodeWidth,j),fill=computerDesks, width=tableWidth)
    nodeCoords.append((e-nodeWidth, j))
    nodeCoords.append((e+nodeWidth, j))


    # for two bottom right rows of computer desks:
  for i in xrange(f,c,tableGap): # for each column
    for j in xrange(numC, v, nodeStep):                                 # for each row
      staffDraw.line((i-nodeWidth, j, i+nodeWidth, j),fill=computerDesks, width=tableWidth) # draw a line
      studentDraw.line((i-nodeWidth, j, i+nodeWidth, j),fill=computerDesks, width=tableWidth) # draw a line
      nodeCoords.append((i-nodeWidth, j))
      nodeCoords.append((i+nodeWidth, j))


    # for top row of computer desks:
  for i in xrange(f,c,tableGap): # for each column
    for j in xrange(numB, s, nodeStep):                                 # for each row
      staffDraw.line((i-nodeWidth, j, i+nodeWidth, j),fill=computerDesks, width=tableWidth) # draw a line
      studentDraw.line((i-nodeWidth, j, i+nodeWidth, j),fill=computerDesks, width=tableWidth) # draw a line
      nodeCoords.append((i-nodeWidth, j))                    # add node coords to array
      nodeCoords.append((i+nodeWidth, j))                    # add node coords to array



#-------------------------------------------------------------------------------

  # draw nodes at each coordinate in array. colours depend on database values:
  # ellipse=((topLeftX,topLeftY,bottomRightX,bottomRightY),fill=colour,outline=colour)

  cursor.execute("SELECT `Tootill 1` FROM compStatus") # point cursor to status column

  # define empty strings which we will give values to later:
  colour = (255,255,255)
  nextStatus = ""

  noGroups = True
  if len(desiredGroups) != 0: # if there is no lab scheduled at the current time
    noGroups = False


  for node in nodeCoords:
    # calculate node colour based off of status from database:
    nextStatus = cursor.fetchone()  # this returns a tuple in which the first value is the colour of that seat

    if nextStatus[0] == "empty":                   # if the computer is free
      colour = nodeGreen
    elif nextStatus in desiredGroups: # if occupied by desired lab group
      colour = nodeYellow
    else:
      colour = nodeRed              # if occupied by someone who shouldn't be there
  # draw the node with the set colour:
    staffDraw.ellipse((node[0]-nodeRadius, node[1]-nodeRadius, node[0]+nodeRadius, node[1]+nodeRadius), fill = colour, outline = (0,0,0))


  # draw nodes on student image:
    if nextStatus[0] == "empty":                   # if the computer is free
      studentDraw.ellipse((node[0]-nodeRadius, node[1]-nodeRadius, node[0]+nodeRadius, node[1]+nodeRadius), fill = nodeGreen, outline = (0,0,0))

    else:
      studentDraw.ellipse((node[0]-nodeRadius, node[1]-nodeRadius, node[0]+nodeRadius, node[1]+nodeRadius), fill = nodeRed, outline = (0,0,0))


#-------------------------------------------------------------------------------

  # save as image in current working directory:
  staffImg.save('staffImage.png')
  studentImg.save('studentImage.png')
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

cursor.execute("SELECT `Tootill 1` FROM desiredGroups") # points cursor to correct place

desiredGroups.append(cursor.fetchone()) # adds group name to array of desired groups

print desiredGroups
#-------------------------------------------------------------------------------
imDrawer()

# close database and print time taken to draw and save image
db.close()




