class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        in_car = dict()
        for trip in trips:
            if trip[1] in in_car.keys():
                in_car[trip[1]] += trip[0]
            else:
                in_car[trip[1]] = trip[0]
            
            if trip[2] in in_car.keys():
                in_car[trip[2]] += -trip[0]
            else:
                in_car[trip[2]] = -trip[0]
                
        n = 0
        for i in range(1001):
            if i in in_car.keys():
                n += in_car[i]
                del in_car[i]
            else:
                continue
            
            if n > capacity:
                return False
            
            if len(in_car) < 1:
                return True
            
        return True
        