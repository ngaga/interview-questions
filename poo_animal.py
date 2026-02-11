
class Necklace():
    def shine(self):
        print('bliiiiink')

class Animal():
    def __init__(self, legs):
        print("init animal")
        self.legs : int = legs
        self.collier = Necklace()
        pass

    def hello(self):
        print('base hello')

    def prout(self):
        print('prout')

    def run(self):
        for i in range(self.legs):
            print('tap')

class Cat(Animal):
    def __init__(self):
        # Note: remember this.
        super().__init__(4)

    
    def hello(self):
        print('Miaou')

a = Cat()
a.hello()
print(f"I have {a.legs} legs.")
a.prout()
a.run()
a.collier.shine()
