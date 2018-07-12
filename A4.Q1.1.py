#Parent Class Triangle
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
#Sub class Area
class Area(Triangle):
    def __init__(self,*args,**kwargs):
        super(Area, self).__init__(*args,**kwargs)
        s = (self.a+self.b+self.c)/2
        a = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        print("The area of the triangle is %f" %a)

Tri = Area(7,8,9)
