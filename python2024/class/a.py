class Rectangle:
    # height = 0
    # width = 0
    # y0 = 0
    # x0 = 0
    # area = 0;
    def property(o_fun):
        def p(*a):
            a[0].area = a[3]*a[4]
            o_fun(*a)
        return p
        

    @property
    def __init__(self , x0 , y0 , width,  height):
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle:('+ str(self.x0) + ',' + str(self.y0) + ')-(' + str((self.x0+self.width)) + ',' + str((self.y0+self.height)) + ')'

    def __or__(self,other):
        lis = [self.x0 , self.x0+self.width , other.x0 , other.x0+other.width]
        lis = sorted(lis)
        ll = [self.y0 , self.y0+self.height , other.y0+other.height , other.y0]
        ll = sorted(ll)
        return Rectangle(lis[0] , ll[0] , lis[3] - lis[0] , ll[3] - ll[0])

    def __and__(self , other):
        x = False
        y = False
        if(self.x0 + self.width < other.x0 + other.width):
            if(self.x0 + self.width > other.x0):
                x = True
        else:
            if(other.x0 + other.width < self.x0):
                x = True
        if x:
            if(self.y0 + self.height < other.y0 + other.height):
                if(self.y0 + self.height > other.y0):
                    y = True
            else:
                if(other.y0 + other.height < self.y0):
                    y = True
        if x and y:
            lis = [self.x0 , self.x0+self.width , other.x0 , other.x0 + other.width]
            ll = [self.y0 , self.y0 + self.height , other.y0 , other.y0+other.height]
            lis = sorted(lis)
            ll = sorted(ll)
            return Rectangle(lis[1] , ll[1] , lis[2] - lis[1] , ll[2] - ll[1])
        else:
            return Rectangle(max(self.x0 , other.x0) , max(self.y0 , other.y0) , 0 , 0)

    def __repr__(self): 
        return f"Rectangle({self.x0},{self.y0},{self.width},{self.height})"
    def __eq__(self , other):
        return self.x0 == other.x0 and self.y0 == other.y0 and self.width == other.width and self.height == other.height
# rr = Rectangle(3 , 3, 3, 3)\

# rect1 = Rectangle(0,0,10,10)
# rect2 = Rectangle(10,10,10,10)
# # 2
# print(rect1.area)

# rect3 = rect1 | rect2
# # 3
# print(rect3)


# # 4
# rect4 = rect1 & rect2
# print(rect4)


# #5
# print(rect1)
# # 6
# print(rect1==eval(repr(rect1)))
