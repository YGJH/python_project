class myChain:
    def __init__(self,*num):
        self.head = None
        b = list()
        for i in num:
            for c in i:
                b.append(c)

        b = reversed(b)
        # self.Data = b;
        for i in b:
            self.insert_head(i)
            # self.insert_head(i)

    def insert_head(self,data):
        self.head = (data,self.head)

    def __del__(self):
        p = self.head
        while p is not None:
            q = p
            p = p[1]
            del q

    def __iter__(self):
        self.iter_p = self.head
        return self

    def __next__(self):
        if self.iter_p is None:
            raise StopIteration
        p = self.iter_p
        self.iter_p = p[1]
        return p[0]
    

a = myChain([1,2,3],[4,5,6],[6,7,8])
for i in a:
    print(i,end=',')
