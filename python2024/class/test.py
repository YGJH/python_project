class Cat:
    # """定义一个猫类"""
 
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age  # 它是一个对象中的属性,在对象中存储,即只要这个对象还存在,那么这个变量就可以使用
 
    def __str__(self):
        return '名字是:'+str(self.name)+' , 年龄是:'+str(self.age)
 
    def eat(self):
        print("%s在吃鱼...." % self.name)
 
    def drink(self):
        print("%s在喝可乐..." % self.name)
 
    def introduce(self):
        # print("名字是:%s, 年龄是:%d" % (汤姆的名字, 汤姆的年龄))
        # print("名字是:%s, 年龄是:%d" % (tom.name, tom.age))
        print("名字是:%s, 年龄是:%d" % (self.name, self.age))
 
# 创建了一个对象
tom = Cat("汤姆", 30)
print(tom)
