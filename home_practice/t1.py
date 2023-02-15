from turtle import * 
speed('slowest')
pencolor('orange')
fillcolor('green')
begin_fill()

for i in range (12,2,-2):
    fd(100)
    lt(72)
    write(i)
end_fill()
hideturtle()
mainloop()