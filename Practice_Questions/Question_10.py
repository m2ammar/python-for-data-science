checkin_times = [540, 542, 561, 561, 598, 599, 640, 700, 701, 703]

# Your loop here

for i in range (0, len(checkin_times) - 1, 1):
    a = checkin_times[i]
    b = checkin_times[i + 1]
    gap = b - a
    if gap < 5 :
        print(f"Gap of {gap} min between check-in at {a} and check-in at {b}")
        
    
    
    
     