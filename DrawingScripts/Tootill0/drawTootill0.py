from PIL import Image, ImageDraw # drawing package
import time # lets us measure time

from random import randint

import MySQLdb # package used to manipulate the database with python
import dbconfig as config # import our database configuration file

import base64 # allows us to save image as base64 string file
import cStringIO # lets us save image as string variable to save time
#-------------------------------------------------------------------------------

# define it all in a function:
def imDrawer():
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
  b = int(0.6*cWidth) # 450/1000
  b2 = b - int(0.005*cS) # 450/1000
  c = int(0.995*cWidth) # 800/1000

  d = int(0.05*cWidth) # 250/1000
  e = int(0.25*cWidth) # 400/1000
  f = int(0.35*cWidth) # 550/1000
  g = int(0.55*cWidth) # 700/1000
  h = int(0.75*cWidth) # 700/1000

    # verticals:
  t = int(0.2*cHeight) # 490/1000
  u = int(0.45*cHeight) # 560/1000
  v = int(0.7*cHeight) # 815/1000
  w = int(0.95*cHeight) # 890/1000

  x = int(0.005*cHeight) # 100/1000
  y = int(0.55*cHeight) # 550/1000
  z = int(0.995*cHeight) # 900/1000

    # numbers for drawing node lines:
  numA = int(0.075*cWidth) # 575/1000
  numB = int(0.4*cWidth) # 125/1000
 
    # numbers for drawing node lines:
  nodeStep = int(0.06*cWidth) # 75/1000, vertical distance between node lines
  nodeStep2 = int(0.075*cWidth) # 75/1000, vertical distance between node lines

  nodeHeight = int(0.025*cHeight) # 25/1000, height of a node line on each side of table
  tableGap = int(0.25*cHeight) # height between desks
  nodeRadius = int(0.01*cHeight)

    # numbers for drawing doors:
  doorStart = int(0.25*cWidth) # 350/1000
  doorEnd = int(0.32*cWidth) # 400/1000
  doorHeight = int(0.95*cHeight) # 850/1000
#-------------------------------------------------------------------------------

  # draw lines for room outline:
  staffDraw.line((a,0,a,cHeight),fill=roomLines, width=wallWidth)
  staffDraw.line((b,y,b,0),fill=roomLines, width=wallWidth)
  staffDraw.line((0,x,b,x),fill=roomLines, width=wallWidth)
  staffDraw.line((b2,y,cWidth,y),fill=roomLines, width=wallWidth)
  staffDraw.line((c,y,c,cHeight),fill=roomLines, width=wallWidth)
  staffDraw.line((c,z,doorEnd,z),fill=roomLines, width=wallWidth)
  staffDraw.line((doorStart,z,0,z),fill=roomLines, width=wallWidth)

  # draw lines for room outline:
  studentDraw.line((a,0,a,cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((b,y,b,0),fill=roomLines, width=wallWidth)
  studentDraw.line((0,x,b,x),fill=roomLines, width=wallWidth)
  studentDraw.line((b2,y,cWidth,y),fill=roomLines, width=wallWidth)
  studentDraw.line((c,y,c,cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((c,z,doorEnd,z),fill=roomLines, width=wallWidth)
  studentDraw.line((doorStart,z,0,z),fill=roomLines, width=wallWidth)

  # draw lines for door:
  staffDraw.line((doorStart,z,doorEnd,doorHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((doorStart,z,doorEnd,doorHeight),fill=roomLines, width=wallWidth)

#-------------------------------------------------------------------------------
  # draw lines for computer tables:

  # left column:
  staffDraw.line((d,t,e,t),fill=computerDesks, width=tableWidth)
  staffDraw.line((d,u,e,u),fill=computerDesks, width=tableWidth)
  staffDraw.line((d,v,e,v),fill=computerDesks, width=tableWidth)
  staffDraw.line((d,w,e,w),fill=computerDesks, width=tableWidth)

  studentDraw.line((d,t,e,t),fill=computerDesks, width=tableWidth)
  studentDraw.line((d,u,e,u),fill=computerDesks, width=tableWidth)
  studentDraw.line((d,v,e,v),fill=computerDesks, width=tableWidth)
  studentDraw.line((d,w,e,w),fill=computerDesks, width=tableWidth)

  # right column, top two rows:
  staffDraw.line((f,t,g,t),fill=computerDesks, width=tableWidth)
  staffDraw.line((f,u,g,u),fill=computerDesks, width=tableWidth)

  studentDraw.line((f,t,g,t),fill=computerDesks, width=tableWidth)
  studentDraw.line((f,u,g,u),fill=computerDesks, width=tableWidth)
  
  # right column, botttom two rows:
  staffDraw.line((f,v,h,v),fill=computerDesks, width=tableWidth)
  staffDraw.line((f,w,h,w),fill=computerDesks, width=tableWidth)

  studentDraw.line((f,v,h,v),fill=computerDesks, width=tableWidth)
  studentDraw.line((f,w,h,w),fill=computerDesks, width=tableWidth)
  
#-------------------------------------------------------------------------------

  # draw node lines on computer tables and add coordinates of nodes to array:
  # xrange function creates iterable object rather than whole list
  # it is therefore much more efficient and should lead to quicker drawing

  # define int values so we can use xrange rather than using yield to write our 
  # own xrange function:



  nodeCoords = []                                     # array for node coordinates


  # for left column except bottom desk
  for i in xrange(numA,e,nodeStep):
    for j in xrange(t,v+1,tableGap):
      staffDraw.line((i, j-nodeHeight, i, j+nodeHeight),fill=computerDesks, width=tableWidth) 
      studentDraw.line((i, j-nodeHeight, i, j+nodeHeight),fill=computerDesks, width=tableWidth) 
      nodeCoords.append((i, j-nodeHeight))
      nodeCoords.append((i, j+nodeHeight))

  # for bottom desk in left column
  for i in xrange(numA,e,nodeStep):
    staffDraw.line((i, w, i, w-nodeHeight),fill=computerDesks, width=tableWidth)
    studentDraw.line((i, w, i, w-nodeHeight),fill=computerDesks, width=tableWidth)
    nodeCoords.append((i,w-nodeHeight))

  # for right column, top two desks
  for i in xrange(numB,g,nodeStep):
    for j in xrange(t,u+1,tableGap):
      staffDraw.line((i, j-nodeHeight, i, j+nodeHeight),fill=computerDesks, width=tableWidth) 
      studentDraw.line((i, j-nodeHeight, i, j+nodeHeight),fill=computerDesks, width=tableWidth) 
      nodeCoords.append((i, j-nodeHeight))
      nodeCoords.append((i, j+nodeHeight))

  # for right column, third desk from the top, top half
  for i in xrange(numB,h,nodeStep):
    staffDraw.line((i, v, i, v-nodeHeight),fill=computerDesks, width=tableWidth) 
    studentDraw.line((i, v, i, v-nodeHeight),fill=computerDesks, width=tableWidth) 
    nodeCoords.append((i, v-nodeHeight))

  # for right column, third desk from the top, bottom half
  for i in xrange(numB,h,nodeStep2):
    staffDraw.line((i, v, i, v+nodeHeight),fill=computerDesks, width=tableWidth) 
    studentDraw.line((i, v, i, v+nodeHeight),fill=computerDesks, width=tableWidth) 
    nodeCoords.append((i, v+nodeHeight))


  # for right column, bottom desk
  for i in xrange(numB,h,nodeStep):
    staffDraw.line((i, w, i, w-nodeHeight),fill=computerDesks, width=tableWidth) 
    studentDraw.line((i, w, i, w-nodeHeight),fill=computerDesks, width=tableWidth) 
    nodeCoords.append((i,w-nodeHeight))


#-------------------------------------------------------------------------------

  # draw nodes at each coordinate in array. colours depend on database values:
  # ellipse=((topLeftX,topLeftY,bottomRightX,bottomRightY),fill=colour,outline=colour)

  cursor.execute("SELECT labs FROM compStatus") # point cursor to status column

  # define empty strings which we will give values to later:
  colour = (255,255,255)
  nextStatus = ""



  for node in nodeCoords:
    # calculate node colour based off of status from database:
    nextStatus = cursor.fetchone()  # this returns a tuple in which the first value is the colour of that seat
    nextStatus = nextStatus[0].split(",")

    if nextStatus[2] == "empty":                   # if the computer is free
      colour = nodeGreen
    elif nextStatus[2] == desiredGroup: # if occupied by desired lab group
      colour = nodeYellow
    else:
      colour = nodeRed              # if occupied by someone who shouldn't be there
  # draw the node with the set colour:
    staffDraw.ellipse((node[0]-nodeRadius, node[1]-nodeRadius, node[0]+nodeRadius, node[1]+nodeRadius), fill = colour, outline = (0,0,0))


  # draw nodes on student image:
    if nextStatus[2] == "empty":                   # if the computer is free
      studentDraw.ellipse((node[0]-nodeRadius, node[1]-nodeRadius, node[0]+nodeRadius, node[1]+nodeRadius), fill = nodeGreen, outline = (0,0,0))

    else:
      studentDraw.ellipse((node[0]-nodeRadius, node[1]-nodeRadius, node[0]+nodeRadius, node[1]+nodeRadius), fill = nodeRed, outline = (0,0,0))


#-------------------------------------------------------------------------------

###########
  staffImg.save("test.png")
###########
  # push staff image to db
  buffer = cStringIO.StringIO()
  staffImg.save(buffer, format="PNG")
  staff_encoded = base64.b64encode(buffer.getvalue())

  command = "UPDATE base64Images SET `Tootill 0`='" + staff_encoded + "' WHERE Type='Staff'"
  cursor.execute(command)


  # push staff image to db
  buffer = cStringIO.StringIO()
  studentImg.save(buffer, format="PNG")
  student_encoded = base64.b64encode(buffer.getvalue())

  command = "UPDATE base64Images SET `Tootill 0`='" + student_encoded + "' WHERE Type='Student'"
  cursor.execute(command)


  db.commit()

#-------------------------------------------------------------------------------






















#-------------------------------------------------------------------------------

# set start for time measurement:
start = time.time()


# connect to the database and make a cursor:
db = MySQLdb.connect(config.host, config.user, config.passwd, config.database) 
cursor = db.cursor()

#-------------------------------------------------------------------------------


# define array holding the groups which should be here currently by reading from database
# this is only for the staff login though. irrelevant to students
numOfRows = cursor.execute("SELECT COUNT(*) FROM desiredGroups")  # returns number of desired groups

cursor.execute("SELECT `Tootill 0` FROM desiredGroups") # points cursor to correct place

desiredGroup = (cursor.fetchone())[0] # adds group name to array of desired groups

#-------------------------------------------------------------------------------
imDrawer()

# close database and print time taken to draw and save image
db.close()

#-------------------------------------------------------------------------------
end = time.time()
print 'took', end - start, 'seconds to draw and save images'



