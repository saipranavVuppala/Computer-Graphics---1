t1=3
t2=4
colorT=10
x=noise(t1)
y=noise(t2)
def setup():
    size(640,640)
    background(0,255,0)
    
def draw():
    global x,t1,t2,colorT
    background((noise(colorT)*100))
    colorT=colorT+0.01
    x=noise(t1)
    y=noise(t2)
    x=x*1000
    y=y*1000
    t1=t1+0.01
    t2=t2+0.01
    ellipse(x,y,30,30)
