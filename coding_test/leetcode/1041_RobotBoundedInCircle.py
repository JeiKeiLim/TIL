class Solution:
    def __init__(self):
        self.rx, self.ry = 0, 0
        self.r_face = 0
        
    def turnRobot(self, dir):
        self.r_face += dir
        if self.r_face < 0:
            self.r_face = 3
        elif self.r_face > 3:
            self.r_face = 0
        
    def forwardRobot(self):
        if self.r_face == 0:
            self.ry -= 1
        elif self.r_face == 1:
            self.rx += 1
        elif self.r_face == 2:
            self.ry += 1
        else:
            self.rx -= 1
        
    def isRobotBounded(self, instructions: str) -> bool:
        
        for i in range(10):
            for cmd in instructions:
                if cmd == 'G':
                    self.forwardRobot()
                elif cmd == 'R':
                    self.turnRobot(1)
                else:
                    self.turnRobot(-1)

            if (self.rx, self.ry) == (0, 0):
                return True
            
        return False
                
        