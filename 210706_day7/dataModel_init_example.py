class Point():
    def __new__(cls,*args,**kwargs):
        print("From new")
        print(cls)
        print(args)
        print(kwargs)
        # create our object and return it
        obj = super().__new__(cls)
        return obj

    def __init__(self, x = 0, y = 0):  ## DOES NOT INVOKE ALLOCATIONS
        print("From init")
        self.x = x
        self.y = y

class RectPoint(Point):
    MAX_Inst = 4
    Inst_created = 0
    def __new__(cls,*args,**kwargs):
        if (cls.Inst_created >= cls.MAX_Inst):
            raise ValueError("Cannot create more objects")
        cls.Inst_created += 1
        return super().__new__(cls)


# 1
one1 = Point(3, 4)

#2
p1 = RectPoint(0,0)
p2 = RectPoint(1,0)
p3 = RectPoint(1,1)
p4 = RectPoint(0,1)

p5 = RectPoint(2,2)