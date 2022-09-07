import matplotlib.pyplot as plt


def showWay(startPoint, finishPoint):
    if finishPoint.x == startPoint.x and finishPoint.y == startPoint.y:
        print(finishPoint.x, finishPoint.y)
        return
    else:
        maze[finishPoint.y][finishPoint.x] = 9
        print(finishPoint.x, finishPoint.y)
        showWay(startPoint, finishPoint.comeFrom)


def get_green_range(startX, startY, finishX, finishY):
    return round(((abs(startX - finishX) * 10) ** 2 + (abs(startY - finishY) * 10) ** 2) ** 0.5)


def get_blue_range(startX, startY, finishX, finishY):
    return abs(startX - finishX) * 10 + abs(startY - finishY) * 10


class Point:
    def __init__(self, x, y, status, greenRange=None, blueRange=None, sumRange=None, comeFrom=[]):
        self.comeFrom = comeFrom
        self.greenRange = greenRange
        self.blueRange = blueRange
        self.sumRange = sumRange
        self.x = x
        self.y = y
        self.status = status
        self.visited = False


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 3, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

road = 0
wall = 1
startPointName = 2
finishPointName = 3
alreadyVisited = 4

for i in range(len(maze)):
    for k in range(len(maze[i])):
        if maze[i][k] == startPointName:
            startPoint = Point(x=k, y=i, status=2, greenRange=0)

        if maze[i][k] == finishPointName:
            finishPoint = Point(x=k, y=i, status=3)

openList = []
closeList = []
currentPoint = startPoint
print('i start in', currentPoint.x, currentPoint.y)

print(currentPoint.y != finishPoint.y)
while currentPoint.x != finishPoint.x or currentPoint.y != finishPoint.y:
    search = \
        [
            Point(x=currentPoint.x - 1,
                  y=currentPoint.y - 1,
                  status=maze[currentPoint.y - 1][currentPoint.x - 1],
                  ),

            Point(x=currentPoint.x - 1,
                  y=currentPoint.y,
                  status=maze[currentPoint.y][currentPoint.x - 1],
                  ),

            Point(x=currentPoint.x - 1,
                  y=currentPoint.y + 1,
                  status=maze[currentPoint.y + 1][currentPoint.x - 1],
                  ),

            Point(x=currentPoint.x,
                  y=currentPoint.y - 1,
                  status=maze[currentPoint.y - 1][currentPoint.x],
                  ),

            Point(x=currentPoint.x,
                  y=currentPoint.y + 1,
                  status=maze[currentPoint.y + 1][currentPoint.x],
                  ),

            Point(x=currentPoint.x + 1,
                  y=currentPoint.y - 1,
                  status=maze[currentPoint.y - 1][currentPoint.x + 1],
                  ),

            Point(x=currentPoint.x + 1,
                  y=currentPoint.y,
                  status=maze[currentPoint.y][currentPoint.x + 1],
                  ),

            Point(x=currentPoint.x + 1,
                  y=currentPoint.y + 1,
                  status=maze[currentPoint.y + 1][currentPoint.x + 1],
                  )
        ]

    for i in search:
        if i.status != 1:
            if [i.x, i.y] not in [[j.x, j.y] for j in closeList]:
                if [i.x, i.y] not in [[j.x, j.y] for j in openList]:
                    i.comeFrom = currentPoint
                    i.greenRange = i.comeFrom.greenRange + get_green_range(i.comeFrom.x, i.comeFrom.y, i.x, i.y)
                    i.blueRange = get_blue_range(i.x, i.y, finishPoint.x, finishPoint.y)
                    i.sumRange = i.blueRange + i.greenRange
                    openList.append(i)
                elif i in openList and \
                        currentPoint.greenRange + get_green_range(currentPoint.x, currentPoint.y, i.x,i.y) < i.greenRange:
                    i.comeFrom = currentPoint
                    i.greenRange = get_green_range(currentPoint.x, currentPoint.y, i.x, i.y)
                    i.blueRange = get_blue_range(i.x, i.y, finishPoint.x, finishPoint.y)
                    i.sumRange = i.blueRange + i.greenRange

    closeList.append(currentPoint)
    if currentPoint in openList:
        openList.remove(currentPoint)
   
    for i in openList:
        print('x =', i.x)
        print('y =', i.y)
        print('greenRange =', i.greenRange)
        print('blueRange =', i.blueRange)
        print('sumRange =', i.sumRange)

    currentPoint = openList[[i.sumRange for i in openList].index(min(i.sumRange for i in openList))]
    print('finish step, next point is', currentPoint.x, currentPoint.y)

showWay(startPoint, currentPoint.comeFrom)

fig, ax = plt.subplots()

ax.imshow(maze)

fig.set_figwidth(6)
fig.set_figheight(6)

plt.show()
