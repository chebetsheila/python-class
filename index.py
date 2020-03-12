# age=10
# if age<18:
#     print("child")
# else:
#     print("adult")
time=int(input("enter the right salute time!:"))
if time>=6 and time<12:
    print("good morning")
elif time>= 12 and time <16:
    print("good afternoon")
elif time>=16 and time<20:
    print("good evening")
elif time>20 and time <24 or time>=0 and time<6:
    print("good night")
else:
    print("invalid time")
