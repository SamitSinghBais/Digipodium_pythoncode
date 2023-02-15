from turtle import *
speed('fastest')
pencolor('yellow')
fillcolor('green')
begin_fill()
for i in range(5):
    
    fd(100)
    for i in range(5) :
        fd(50)
        for i in range(5):
            fd(25)
            rt(72)
        lt(72)
    rt(72)

    end_fill()
write(i)
hideturtle()
mainloop()  