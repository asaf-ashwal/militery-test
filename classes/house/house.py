from classes.house.room import Room
from classes.soldier.soldier import Soldier


class House:
    def __init__(self, house_id: int):
        self.house_id = house_id
        self.rooms: list[Room] = [Room(0)]

    def add_room(self, room: Room):
        if len(self.rooms) < 10:
            self.rooms.append(room)

    def add_to_room(self, soldier: Soldier, house_id):
        if len(self.rooms[-1].soldiers) < 8:
            self.rooms[-1].soldiers.append(soldier)
            soldier.in_house({'house_id':house_id,'room_id':self.rooms[-1].room_id})

        elif len(self.rooms)< 10:
            new_room = Room(len(self.rooms)+1)
            new_room.add_soldier(soldier)
            self.add_room(new_room)
            soldier.in_house({'house_id':house_id,'room_id':new_room.room_id})
        else: return False
    def is_full(self):
        if len(self.rooms[-1].soldiers)<8 and len(self.rooms[-1].soldiers)>0:
            return {'full':len(self.rooms)-1,'not_full':1,'empty':10 - len(self.rooms)}
        elif len(self.rooms[-1].soldiers)<8 and len(self.rooms[-1].soldiers)<0:
            return {'full':len(self.rooms),'not_full':0,'empty':10 - len(self.rooms)}
        else:
            return {'full':len(self.rooms)-1,'not_full':0,'empty':10}


        
        

    # לבדוק שאין 10 חדרים מלאים ולא להכניס ואם כן להחזיר FALSE
    # def add_soldier_to_room(self, soldiers: Soldier):
    #     for soldier in soldiers:
    #         result = self.add_to_room(soldier)
    #         if result == False:
    #             return False