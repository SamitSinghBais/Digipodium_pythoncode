from turtle import *
speed('slowest')
pencolor('green')
fillcolor('blue')

for i in range(3):
   fd(200)
   for i in range(3):
      fd(100)
      begin_fill()
      for i in range(3):
        fd(1)
        rt(60)
      end_fill()
      lt(60)
   rt(60)

   write(i)
hideturtle()
mainloop()
