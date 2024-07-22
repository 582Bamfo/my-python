# continue statement
import random
import time

for i in ["devop","aws","ansible","terraform","python","linux"]:
    print(i)
    if i =="ansible":
        print("my data found")
        continue
    time.sleep(1)
print("out of the continue statement loop")
