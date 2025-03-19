class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x = []
        y = []
        for coordinate in coordinates:
            xc = coordinate[0]
            yc = coordinate[1]
            x.append(xc)
            y.append(yc)
            
        last = len(x) - 1
        
        try:   
            if len(coordinates) == 2:
                return True
            elif (y[1] - y[0]) * (x[last] - x[last - 1]) == (y[last] - y[last - 1]) * (x[1] - x[0]) and (y[2] - y[1]) * (x[last] - x[last - 1]) == (y[last] - y[last - 1]) * (x[2] - x[1]):
                return True
            else:
                return False
        except ZeroDivisionError:
            if 0.5 * (x[0] * (y[1] - y[last]) + x[1] * (y[last] - y[0]) + x[last] * (y[0] - y[1])) == 0:
                return True
            else:
                return False

#Area = 0.5 * (x[0](y[1] - y[last]) + x[1](y[last] - y[0]) + x[last](y[0] - y[1])) = 0
#y3 =ylat,y2 = y[1] and y1 = y[0]

    
                    