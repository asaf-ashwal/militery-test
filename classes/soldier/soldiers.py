from classes.soldier.soldier import Soldier


class Soldiers:
    def __init__(self):
        self.class_soldiers = []
        # coloms

    def add_soldier(self, soldier: Soldier):
        """adding a new soldier"""
        self.class_soldiers.append(soldier)
        # print(soldier)

    def add_csv_soldiers(self, soldiers):
        # print(soldiers)
        try:
            for soldier in soldiers:
                new_soldiers = Soldier(
                    soldier_number=soldier[0],
                    first_name=soldier[1],
                    last_name=soldier[2],
                    gender=soldier[3],
                    city=soldier[4],
                    distance=soldier[5],
                )
                self.add_soldier(new_soldiers)
            self.class_soldiers.sort(key=myFunc)
            return self.class_soldiers

        except:
            print("Error")
    def get_thet_wait():
        pass

def myFunc(e):
    return e.distance
