import sys
width,height,bottom,right = int(input()),int(input()),int(input()),int(input())
slope = (right)/(width-bottom)
b = right - slope*width
path = 1
visited,visited2 = ['Right'],set()
x,y = width,right
while True:
    slope = -slope
    b = y-slope*x
    if 'Top' not in visited and 0 <= ((height - b)/(slope)) <= width:  #top
        if 0 <= ((height - b)/(slope)) < 5 or width-5 < ((height - b)/(slope)) <= width:
            break
        visited[0] = 'Top'
        path += 1
        x,y = round((height - b)/(slope),10),height
        if (x,y) in visited2:
            print(0)
            sys.exit()
        else:
            visited2.add((x,y))

    elif 'Left' not in visited and 0 <= (slope*0 + b) <= height: #left
        if 0 <= (slope*0 + b) < 5 or height-5 < (slope*0 + b) <= height:
            break
        visited[0] = 'Left'
        path += 1
        x,y = 0,round((slope*0 + b),10)
        if (x,y) in visited2:
            print(0)
            sys.exit()
        else:
            visited2.add((x,y))
            
    elif 'Bottom' not in visited and 0 <= ((0 - b)/(slope)) <= width: #bottom
        if 0 <= ((0 - b)/(slope)) < 5 or width-5 < ((0 - b)/(slope)) <= width:
            if ((0 - b)/(slope)) < 5:
                break
            else:
                break
        visited[0] = 'Bottom'
        path += 1
        x,y =  round((0 - b)/(slope),10),0
        if (x,y) in visited2:
            print(0)
            sys.exit()
        else:
            visited2.add((x,y))
    elif 'Right' not in visited and 0 <= (slope*width + b) <= height: #right
        if 0 <= (slope*width + b) < 5 or height-5 < (slope*width + b) <= height:
            break
        visited[0] = 'Right'
        path += 1
        x,y = width,round((slope*width + b),10)
        if (x,y) in visited2:
            print(0)
            sys.exit()
        else:
            visited2.add((x,y))
print(path)







