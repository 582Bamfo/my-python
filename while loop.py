#while loop
import time

x = 0
while x<10:
    print(f"It is going to be a long looping here as long as x is",x)
    time.sleep(2)
    x+=1
print("while loop terminated")