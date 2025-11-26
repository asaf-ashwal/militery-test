from classes.soldier.soldier import Soldier


class Soldiers:
    def __init__(self):
        self.class_soldiers = []

    def add_soldier(self, soldier: Soldier):
        """adding a new soldier"""
        self.class_soldiers.append(soldier)

    def add_csv_soldiers(self, soldiers):
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

    # הם כבר מסודרים אז הוא יחזיר אןתם לפי סדר עדיפויות
    def get_thet_wait(self):
        wait_soldiers = []
        for s in self.class_soldiers:
            if s.inlay_status == "on the waiting list":
                wait_soldiers.append(s)
        return {
            "waiting list number": len(wait_soldiers),
            "the soldiers": wait_soldiers,
        }

    def get_soldier_by_id(self, soldier_id):
        print(len(self.class_soldiers))
        for s in self.class_soldiers:
            if s.soldier_number == str(soldier_id):
                return s
        return {"no soldier maching"}


def myFunc(e):
    return e.distance
