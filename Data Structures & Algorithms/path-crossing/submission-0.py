class Solution:
    def isPathCrossing(self, path: str) -> bool:
        self.path = path
        x = y = 0
        visited = set()
        visited.add((x, y))
        for i in self.path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            else:
                x -= 1
            
            coordinates = (x, y)
            if coordinates in visited:
                return True
            else:
                visited.add(coordinates)
        
        return False
        