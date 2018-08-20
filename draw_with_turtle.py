import turtle

def draw_square(turtle_name):  
  #drawing square
  for i in range(4):
    brad.forward(100)
    brad.right(90)
    
    
draw_with_turtle():
  window = turtle.Screen()
  window.bgcolor("red")
  
  # create brad for drawing square
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("yellow")
  brad.speed(2)
  draw_square(brad)
  
  # create angie for drawing cicle
  angie = turtle.Turtle()
  angie.shape("arrow")
  angie.color("blue")
  angie.circle(100)
  
  window.exitonclick()
  
draw_with_turtle()
