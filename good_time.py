import time

a= time.strftime("%H:%M:%S")
print("CURRENT TIME: ", a)
b= time.strftime("%H")
#print(int(b))
if (int(b)<12):   #12= 12 PM
	print("\n🌷🌄GOOD MORNING SIR!🌷🌄")
elif (12 <= int(b) < 16):
	print("\n🌷☀️GOOD AFTERNOON SIR!🌷☀️")
elif (16 <= int(b) < 22):   #16 = 4PM
	print("\n🌷🌇GOOD EVENING SIR!🌷🌇")
elif (22 <= int(b)):   #22= 10PM
	print("\n🌷🌙🌆GOOD NIGHT SIR!🀼����🌆")