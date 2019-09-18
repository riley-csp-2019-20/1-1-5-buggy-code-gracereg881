print("hello world")

#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 6
length_of_legs = 70
z = 380 / legs
print("z=",z)
spider.pensize(5)
n = 0
while (n < legs):
  print("z*n=",z*n)
  spider.goto(0,0)
  spider.setheading(z*n)
  spider.forward(length_of_legs)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()