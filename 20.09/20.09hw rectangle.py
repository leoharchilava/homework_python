class Rectangle():
    def init(self,w,h):
        self.w = w
        self.h = h
    
    def get_p(self):
        return (self.w + self.h) * 2

    def get_s(self):
        return (self.w * self.h)

r = Rectangle(4, 5)

print(r.get_s())
print(r.get_p())
