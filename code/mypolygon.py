import turtle
bob = turtle.Turtle()
print(bob)

# using manual. commenting the next 7 lines
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
#
# # to make square
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

for i in range(4):
    print("Hello!")

# square using for loop
for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()