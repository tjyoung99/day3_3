ellipsesize= 50
lefttopboundary=ellipsesize/2
rightbottomboundary= 400-ellipsesize/2
xcoordinate= random(lefttopboundary,rightbottomboundary)
speed=2
yspeed=2
ycoordinate=random(lefttopboundary,rightbottomboundary)
def setup():
    size(400,400)
def draw():
    background(0)
    global xcoordinate, ycoordinate, speed,ellipsesize, yspeed
    if xcoordinate >= rightbottomboundary or xcoordinate <=lefttopboundary:
        speed = -speed
    if ycoordinate >= rightbottomboundary or ycoordinate <= lefttopboundary:
        yspeed=-yspeed
    fill(0,0,0)
    ellipse(xcoordinate,ycoordinate,ellipsesize,ellipsesize)
    fill(255,255,255)
    ellipse(xcoordinate,ycoordinate,ellipsesize,ellipsesize)
    xcoordinate +=speed
    ycoordinate +=yspeed
