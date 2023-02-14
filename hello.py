from turtle import*
speed('fastest')
pencolor('orange')
fillcolor('blue')

for i in range(6):
   fd(100)
   for i in range(6):
      fd(50)
      begin_fill()
      for i in range(6):
        fd(50)
        rt(60)
      end_fill()
      lt(60)
   rt(60)

   write(i)
hideturtle()
mainloop()
