class Graph:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        return

    def __add__(self,other):
        total_x = self.x + other.x
        total_y = self.y + other.y
        return Graph(total_x,total_y)

    def __str__(self):
        return "Total: "+str(self.x)+", "+str(self.y)

p1 = Graph(10,20)
p2 = Graph(25,50)
#print(p1+p2)
p3 = p1+p2
print(p3)
