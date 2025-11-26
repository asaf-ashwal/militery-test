from classes.house.house import House
from classes.soldier.soldier import Soldier


class Houses:
    def __init__(self):
        self.class_houses: list[House] = [House(0)]
        # self.add_basic_houses()

    def add_house(self, house: House):
        self.class_houses.append(house)
    
    def add_to_house(self, soldier: Soldier):
        result = self.class_houses[-1].add_to_room(soldier,self.class_houses[-1].house_id)
        if result == False and len(self.class_houses) < 2:
            new_house = House(len(self.class_houses)+1)
            new_house.add_to_room(soldier,new_house.house_id)
            self.class_houses.append(new_house)
        elif result == False and len(self.class_houses) >= 2 : return False


    def add_full_soldier_to_houses(self,soldiers):
        """added soldiers to houses and return num of the solsers thet aedded"""
        for i in range(len(soldiers)):
            result = self.add_to_house(soldiers[i])
            if result == False:
                return i
        
    def get_houses_space(self):
        
        if len(self.class_houses)>1:
            result = self.class_houses[1].is_full()
            return {
                "full rooms":result['full']+10,#של החדרים המלאים מהבית הראשון
                "not empty rooms":result['not_full'],
                "empty rooms":result['empty']
            }
        else:
            result = self.class_houses[0].is_full()
            return {
                "full rooms":result['full'],
                "not empty rooms":result['not_full'],
                "empty rooms":result['empty']
            }
        
