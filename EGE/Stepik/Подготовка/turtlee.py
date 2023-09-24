import turtle as t

# t.pensize(5)
# t.resizemode("auto")
k = 10
t.speed(100)
t.left(90)

t.forward(100)
t.right(90)
t.forward(100)
t.right(45)

for i in range(15):
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)

t.up()
t.speed(1000)
for x in range(13, 6, -1):
    for y in range(15, 5, -1):
        t.goto(x * k, y * k)
        t.dot(3)
t.done()