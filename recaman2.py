#Using the recaman Sequence
# start at zero
# every step is 1 bigger than the last step
# if it's possible to step backward, do it
# you can only go backward if it results in positive number
# and it hasn't been 'seen' before
import turtle 

window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
stan = turtle.Turtle()
stan.shape("turtle")
scale = 5 #this scale isn't turtle, just for us
stan.speed(900)
stan.color('red', 'green')






# move to left for more room
stan.penup()
stan.setpos(-390, 0)
stan.pendown()

current = 0 # Here's how we know where we are
seen = set() # how we keep track

# step increases by one
for step_size in range(1, 100):

    backwards = current - step_size

    # go backwords if possible
    if backwards > 0 and backwards not in seen:
        stan.setheading(90) # straight up
        #makes half circle
        stan.circle(scale * step_size/2, 180)
        current = backwards
        seen.add(current)
    # else go forwards
    else:
        stan.setheading(270) # down
        stan.circle(scale * step_size/2, 180)
        current += step_size
        seen.add(current)

turtle.done()