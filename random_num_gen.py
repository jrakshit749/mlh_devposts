from datetime import date, datetime
import random

today = date.today()
now = datetime.now()
timer = now.strftime("%H:%M:%S")
r_key = random.randint(0,2359)
h = timer[:2]
m = timer[3:5]
s = timer[6:8]
x_key = float(str(h)+str(m)+str(s))
x = str(today).split("-")
y_key = float("".join(x))

z_key = (x_key/y_key)*r_key

print("Random Number: ",z_key)