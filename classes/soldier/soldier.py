class Soldier:
    def __init__(
        self,
        soldier_number: int,
        first_name: str,
        last_name: str,
        gender: str,
        city: str,
        distance: int,
        inlay_status: str = 'on the waiting list',
        house_id: int | None = None,
    ):
        self.soldier_number = soldier_number
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.distance = distance
        self.inlay_status = inlay_status
        self.house_androom_id = house_id

    def __str__(self):
        return f"""
        soldier number: {self.soldier_number},
        fill name: {self.first_name} {self.last_name},
        distance: {self.distance},
        inlay_status: {self.inlay_status},
"""
    def in_house(self,house_androom_id: dict):
        self.house_androom_id = house_androom_id
        self.inlay_status = 'Residentially embedded'

