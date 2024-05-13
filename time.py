import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))
print(hour)

if 5<=hour<=12:
    print('Good morning') 
elif 13<=hour<=18:
    print('Good afternoon') 
else:
    print('Good night')