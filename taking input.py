#interactive script
Devops = ["jenkins","ansible", "docker","terraform"]
Development = ("nodjs","java",".net", "python")
empl = {"name":"bamf","skill":"linux"}

usr_skill = input("enter your skill:")

#conditions
if usr_skill in Devops:
    print(f"we have {usr_skill} in devops")
elif usr_skill in Development:
    print(f"we have {usr_skill} in development")


