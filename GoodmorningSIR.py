import time
timmeclock = time.strftime('%H:%M:%S')
print(f" Hii the time is {timmeclock}")
timmeclock = time.strftime('%H:%M:%S')
Curtime = int(time.strftime('%H'))

if Curtime < 12:
    print(f"Good Morning Sir")
elif Curtime >= 12 and Curtime <= 16:
    print(f"Good Afternoon Sir")
elif Curtime >= 16 and Curtime <= 20:
    print(f"Good Evening Sir")
else:
    print(f"Good Night Sir")
