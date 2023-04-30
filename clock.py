import turtle
import time

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("Digital Clock")

# Create the clock face
clock_face = turtle.Turtle()
clock_face.shape("circle")
clock_face.shapesize(4)
clock_face.pensize(4)

# Create the hour hand
hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.shapesize(2)
hour_hand.pensize(3)

# Create the minute hand
minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.shapesize(2)
minute_hand.pensize(2)

# Create the second hand
second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.shapesize(1)
second_hand.pensize(1)

# Hide the turtle pen
turtle.hideturtle()

def draw_clock():
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    # Calculate the angles of the hands
    hour_angle = (hour % 12) * 30 + (minute / 60) * 30
    minute_angle = minute * 6
    second_angle = second * 6
    
    # Draw the hour hand
    hour_hand.setheading(hour_angle)
    hour_hand.pendown()
    hour_hand.forward(80)
    hour_hand.penup()
    hour_hand.goto(0, 0)
    
    # Draw the minute hand
    minute_hand.setheading(minute_angle)
    minute_hand.pendown()
    minute_hand.forward(120)
    minute_hand.penup()
    minute_hand.goto(0, 0)
    
    # Draw the second hand
    second_hand.setheading(second_angle)
    second_hand.pendown()
    second_hand.forward(140)
    second_hand.penup()
    second_hand.goto(0, 0)
    
    # Update the screen
    screen.update()
    
    # Reset the hands
    hour_hand.clear()
    minute_hand.clear()
    second_hand.clear()
    
# Set the update interval
turtle.tracer(0)
screen.ontimer(draw_clock, 1000)

# Start the turtle main loop
turtle.mainloop()
