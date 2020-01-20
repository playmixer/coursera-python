

class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        arr_lights = []
        arr_obstacles = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] < 0:
                    arr_obstacles.append((x, y))
                if grid[y][x] > 0:
                    arr_lights.append((x, y))
                    
        self.adaptee.set_dim((len(grid[0]), len(grid)))
        self.adaptee.set_lights(arr_lights)
        self.adaptee.set_obstacles(arr_obstacles)
        
        return self.adaptee.generate_lights()