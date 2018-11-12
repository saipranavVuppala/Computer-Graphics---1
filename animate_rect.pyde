c=color(0)
x=0.0
y=200.0
speed=1.0

def setup():
    size(400,400)
    
def draw():
    background(255)
    move()
    display()
        
def move():
    global x
    x=x+speed
    if x>width:
        x=0
        
def display():
    fill(c)
    rect(x,y,40,20)
