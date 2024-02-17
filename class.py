class Cassa(object):
    current_money = 0
    
    

    def __init__(self, cm):
        self.current_money = cm


    def top_up(self, x):
        self.current_money += x
        


    def count_1000(self):
        result = self.current_money // 1000
        return result


    def take_away(self, X):
            if self.current_money > X:
                self.current_money -= X
            elif X > self.current_money:
                print("в кассе недостаточно денег!")



tmp = Cassa(0)
tmp.top_up(500) #500
tmp.top_up(200) #700
print(f'сейчас в кассе: {tmp.current_money}')



temp = Cassa(5000)
print(temp.count_1000()) #5



tmpp = Cassa(0)    
tmpp.take_away(500)  # 0<500 = error
print(tmpp.current_money) #0