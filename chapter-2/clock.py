current_time = input("Current time? In hours (1-24)")
timer = input("How many hours until the alarm goes off?")

cti = int(current_time)
ti = int(timer)

print((cti + ti)%24)