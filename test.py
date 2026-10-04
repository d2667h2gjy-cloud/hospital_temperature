count=0
total=0
highest=30
lowest=45
normal=0
above_normal=0
high_fever=False

while True:
    temp= float(input('Enter temperature (0 to finish): '))
    if temp==0:
        break
    if temp<30 or temp>45:
        print('Temperature is out of range')
        continue
    count=count+1
    total=total+temp
    if temp>highest:
        highest=temp
    if temp<lowest:
        lowest=temp
    if temp<36.0:
        print('Low')
    elif temp<37.5:
        print('Normal')
        normal=normal+1
    elif temp<39.0:
        print('Above normal')
        above_normal=above_normal+1
    else:
        print('High fever')
        above_normal=above_normal+1
        high_fever=True
print('Temperature Summary')
print('Number of valid readings', count)
if count>0:
    average=total/count
    print('Average temperature:', average)
    print('Highest temperature:', highest)
    print('Lowest temperature:', lowest)
    print('Normal temperature:', normal)
    print('Above normal readings:', above_normal)
    if high_fever:
        print('patient has high fever, warn the doctor')
    else:
        print('no high fever was recorded')
else:
    print('No valid readings')