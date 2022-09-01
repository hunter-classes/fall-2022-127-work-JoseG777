current_time = input("Current time? In hours (0-23)")
timer = input("How many hours until the alarm goes off?")

cti = int(current_time)
ti = int(timer)

print((cti + ti)%24)