def HighestAltitude(li):
    current_altitude = 0
    max_altitude = 0
    for i in li:
        current_altitude += i #updating current altitude by adding the gain
        max_altitude = max(max_altitude,current_altitude)
    return max_altitude

# classic prefix sum problem
print(HighestAltitude([-5,1,5,0,-1]))
