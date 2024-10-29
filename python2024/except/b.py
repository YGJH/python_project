class Rectangle:
    height = 0
    width = 0
    y0 = 0
    x0 = 0
    area = 0;
    def property(o_fun):
        def p(*a , **b):
            a[0].area = a[3]*a[4]
            # print(a[3])
            # print(a[4])
            # print(f'area = {a[0].area}')
            # o_fun()
        return p
        

    @property
    def __init__(self , x0 , y0 , width,  height):
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height
        return

    def __or__(self,other):
        x_x = max(self.x0+self.width/2 , other.x0+other.width/2 )
        print(x_x)
        x_X = min(self.x0-self.width/2 , other.x0-other.width/2 )
        print(x_X)
        y_y = max(self.y0+self.height/2 , other.y0+other.height/2)
        y_Y = min(self.y0-self.height/2 , other.y0-other.height/2)
        return Rectangle((self.x0+other.x0)/2 , (self.y0+other.y0)/2 , (x_x - x_X) , (y_y - y_Y))
    
    def __str__(self):
        # return str(f'Rectangle:'+{self.x0}+{self.y0}+'-'+{self.x0+self.width}+','+{self.y0+self.height})
        return 'Rectangle:('+str(self.x0)+','+str(self.y0)+')-('+str(self.x0+self.width)+','+str(self.y0+self.height)+')'

    def __and__(self , other):
        x = False
        y = False
        # 檢查有無重疊
        if(self.x0 + self.width/2 > other.x0 + other.width/2):
            if(self.x0 - self.width/2 < other.x0 + other.width/2):
                x = True
        else:
            if(self.x0 + self.width/2 > other.x0 - other.width/2):
                x = True
        if x:
            if(self.y0 + self.height > other.y0 + other.height):
                if(self.y0 - self.height < other.y0 + other.height):
                    y = True
            else:
                if(self.y0 + self.height > other.y0 + other.height):
                    y = True
        
        if y and x:
            lis = [self.x0 + self.width/2 , self.x0 - self.width/2 , other.x0 + other.width/2 , other.x0 - other.width/2 ]
            lis = sorted(lis)
            li = [self.y0 + self.height/2 , self.y0 - self.height/2 , other.y0 + other.height/2 , other.y0 - other.height/2 ]
            li = sorted(li)
            return Rectangle((lis[2] + lis[1])/2 , (li[2] - li[1])/2 , lis[2] - lis[1] , li[2] - li[1])
        else:
            return Rectangle(max(self.x0,other.x0),max(self.y0,other.y0) , 0 , 0)
    def __repr__(self): 
        return "Rectangle({},{},{},{})".format(self.x0,self.y0,self.width ,self.height)
# rr = Rectangle(3 , 3, 3, 3)\

rect1 = Rectangle(0,0,10,10)
rect2 = Rectangle(10,10,10,10)
print(rect1.area)


rect3 = rect1 | rect2
print(rect3)
