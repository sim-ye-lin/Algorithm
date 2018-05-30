import turtle as t
default_shape = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
user_shape = ["7s0.gif", "7s1.gif", "7s2.gif"]

for i in range(1, len(default_shape)):
    t.delay(1000)
    t.shape(default_shape[i])

for i in range(0, len(user_shape)):
    t.delay(1000)
    t.addshape(user_shape[i])
    t.shape(user_shape[i])
    
