# [도전] 저글링 클래스 만들기

class Zergling :
    
    def __init__(self) :
        self.hp = 20
        self.mana = 50
        
    def run(self) :
        print('뛴다')
        self.hp -= 1
        self.mana += 1
        
    def show_status(self) :
        print(self.hp,self.mana)
        
z1 = Zergling()
z2 = Zergling()

z1.run()
z1.show_status()

for _ in range(5) :
    z2.run()
    
z2.show_status()

