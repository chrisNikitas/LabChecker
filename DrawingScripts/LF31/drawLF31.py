from PIL import Image, ImageDraw # drawing package
import time # lets us measure time

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
  cS = 2000 # cS = canvasScale
  cHeight = int(0.610*cS) # height of image
  cWidth = int(0.810*cS) # width of image
  staffImg = Image.new('RGBA', (cWidth,cHeight), color = background)
  staffDraw = ImageDraw.Draw(staffImg)

  studentImg = Image.new('RGBA', (cWidth,cHeight), color = background)
  studentDraw = ImageDraw.Draw(studentImg)

  # define line widths
  wallWidth = int(0.01*cS)
  tableWidth = int(0.005*cS)

#-------------------------------------------------------------------------------

  # define coordinates for easy reference:
    # horizontals:
  a = int(0.2*cWidth)
  b = int(0.4*cWidth)
  c = int(0.6*cWidth)
  d = int(0.8*cWidth)
    # verticals:
  v = int(0.1*cHeight)
  w = int(0.4*cHeight)
  x = int(0.6*cHeight)
  y = int(0.9*cHeight)
  z = int(0.75*cHeight)

#-------------------------------------------------------------------------------

  # draw lines for room outline:
  staffDraw.line((0,0.005*cHeight,cWidth,0.005*cHeight),fill=roomLines, width=wallWidth)
  staffDraw.line((0.005*cWidth,0,0.005*cWidth,cHeight),fill=roomLines, width=wallWidth)
  staffDraw.line((0,0.995*cHeight,0.75*cWidth,0.995*cHeight),fill=roomLines, width=wallWidth)
  staffDraw.line((0.75*cWidth,cHeight,0.75*cWidth,0.5*cHeight),fill=roomLines, width=wallWidth)
  staffDraw.line((0.745*cWidth,0.5*cHeight,0.825*cWidth,0.5*cHeight),fill=roomLines, width=wallWidth)
  staffDraw.line((0.925*cWidth,0.5*cHeight,cWidth,0.5*cHeight),fill=roomLines, width=wallWidth)
  staffDraw.line((0.995*cWidth,0.5*cHeight,0.995*cWidth,0),fill=roomLines, width=wallWidth)

  studentDraw.line((0,0.005*cHeight,cWidth,0.005*cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((0.005*cWidth,0,0.005*cWidth,cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((0,0.995*cHeight,0.75*cWidth,0.995*cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((0.75*cWidth,cHeight,0.75*cWidth,0.5*cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((0.745*cWidth,0.5*cHeight,0.825*cWidth,0.5*cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((0.925*cWidth,0.5*cHeight,cWidth,0.5*cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((0.995*cWidth,0.5*cHeight,0.995*cWidth,0),fill=roomLines, width=wallWidth)

  # draw lines for door:
  staffDraw.line((0.83*cWidth,0.45*cHeight,0.925*cWidth,0.5*cHeight),fill=roomLines, width=wallWidth)
  studentDraw.line((0.83*cWidth,0.45*cHeight,0.925*cWidth,0.5*cHeight),fill=roomLines, width=wallWidth)


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

  # draw node lines on computer tables and node coordinates to array:
  # xrange function creates iterable object rather than whole list
  # it is therefore much more efficient and should lead to quicker drawing

  # define int values so we can use xrange rather than using yield to write our 
  # own xrange function:

  numA = int(0.2*cWidth)  # first column
  numB = int(0.801*cWidth)  # last column (limit)
  numC = int(0.025*cHeight)   # width of one node line
  numE = int(0.025*cWidth)
  numF = int(0.401*cWidth)
  numG = int(0.575*cWidth)  # third column
  numI = int(0.6*cWidth)

  nodeStep = int(0.05*cHeight) # vertical distance between node lines

  # create and populate array of tuples representing node coordinates:
  nodeCoords = []                                     # array for node coordinates


    # for top row of computer desks:
  for i in xrange(numA, numB, numA):                             # for each column
    for j in xrange(v+numC, w, nodeStep):                               # for each row
      staffDraw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth) 
      studentDraw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth) 
      nodeCoords.append((i-numE, j))                    # add node coords to array
      nodeCoords.append((i+numE, j))                    # add node coords to array


    # for first two columns of bottom row of computer desks:
  for i in xrange(numA, numF, numA):                             # for each column
    for j in xrange(x+numC, y, nodeStep):                               # for each row
      staffDraw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth)
      studentDraw.line((i-numE, j, i+numE, j),fill=computerDesks, width=tableWidth)
      nodeCoords.append((i-numE, j))                    # add node coords to array
      nodeCoords.append((i+numE, j))                    # add node coords to array


    # for final column of bottom row of computer desks:
  for j in xrange(x+numC, z, nodeStep):                                 # for each row
    staffDraw.line((numG, j, numI, j),fill=computerDesks, width=tableWidth) # draw a line
    studentDraw.line((numG, j, numI, j),fill=computerDesks, width=tableWidth) # draw a line
    nodeCoords.append((numG, j))                      # add node coords to array


#-------------------------------------------------------------------------------

  # draw nodes at each coordinate in array. colours depend on database values:
  # ellipse=((topLeftX,topLeftY,bottomRightX,bottomRightY),fill=colour,outline=colour)

  nodeDiameter = int(0.013*cHeight)

  cursor.execute("SELECT labs FROM compStatus") # point cursor to status column

  # define empty strings which we will give values to later:
  colour = (255,255,255)
  nextStatus = ""

  for node in nodeCoords:
    # calculate node colour based off of status from database:
    nextStatus = cursor.fetchone()  # this returns a tuple in which the first value is the colour of that seat
    nextStatus = nextStatus[0].split(",")

    if nextStatus[0] == "empty":                   # if the computer is free
      colour = nodeGreen
    elif nextStatus in desiredGroups: # if occupied by desired lab group
      colour = nodeYellow
    else:
      colour = nodeRed              # if occupied by someone who shouldn't be there
  # draw the node with the set colour:
    staffDraw.ellipse((node[0]-nodeDiameter, node[1]-nodeDiameter, node[0]+nodeDiameter, node[1]+nodeDiameter), fill = colour, outline = (0,0,0))


  # draw nodes on student image:
    if nextStatus[0] == "empty":                   # if the computer is free
      studentDraw.ellipse((node[0]-nodeDiameter, node[1]-nodeDiameter, node[0]+nodeDiameter, node[1]+nodeDiameter), fill = nodeGreen, outline = (0,0,0))

    else:
      studentDraw.ellipse((node[0]-nodeDiameter, node[1]-nodeDiameter, node[0]+nodeDiameter, node[1]+nodeDiameter), fill = nodeRed, outline = (0,0,0))


#-------------------------------------------------------------------------------

  # push staff image to db
  buffer = cStringIO.StringIO()
  staffImg.save(buffer, format="PNG")
  staff_encoded = base64.b64encode(buffer.getvalue())

  command = "UPDATE base64Images SET LF31='" + staff_encoded + "' WHERE Type='Staff'"
  cursor.execute(command)


  # push staff image to db
  buffer = cStringIO.StringIO()
  studentImg.save(buffer, format="PNG")
  student_encoded = base64.b64encode(buffer.getvalue())

  command = "UPDATE base64Images SET LF31='" + student_encoded + "' WHERE Type='Student'"
  cursor.execute(command)


  db.commit()


#-------------------------------------------------------------------------------


# set start for time measurement:
start = time.time()

#-------------------------------------------------------------------------------


# connect to the database and make a cursor:
db = MySQLdb.connect(config.host, config.user, config.passwd, config.database) 
cursor = db.cursor()

#-------------------------------------------------------------------------------


# define array holding the groups which should be here currently by reading from database
# this is only for the staff login though. irrelevant to students
desiredGroups = []
numOfRows = cursor.execute("SELECT COUNT(*) FROM desiredGroups")  # returns number of desired groups

cursor.execute("SELECT LF31 FROM desiredGroups") # points cursor to correct place

desiredGroups.append(cursor.fetchone()) # adds group name to array of desired groups

#-------------------------------------------------------------------------------
imDrawer()
# close database and print time taken to draw and save image
db.close()



end = time.time()
print 'took', end - start, 'seconds to draw and save images'

#-------------------------------------------------------------------------------




















