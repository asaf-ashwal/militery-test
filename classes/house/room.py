from classes.soldier.soldier import Soldier


class Room:
    def __init__(self, room_id: int):
        self.room_id = room_id
        self.soldiers: list = []

    def add_soldier(self, soldier: Soldier):
        if len(self.soldiers) < 8:
            self.soldiers.append(soldier)
    def is_full(self):
        return self.soldiers < 8

