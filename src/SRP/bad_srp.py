from datetime import datetime

from database import cars_db


class CarManager:
    id: int
    make: str
    model: str
    last_service: int

    def __init__(self, id, make, model, last_service):
        self.id = id
        self.make = make
        self.model = model
        self.last_service = last_service

    @classmethod
    def get_by_id(cls, id: int) -> "CarManager":
        data = cars_db[id]
        return cls(
            id=id,
            **data
        )

    @property
    def requires_service(self) -> bool:
        return datetime.today().year - 1 > self.last_service

    def __repr__(self):
        return f"{self.id}: {self.make} {self.model}"


if __name__ == "__main__":
    car = CarManager.get_by_id(1)
    print(f"{car} | requires service: {car.requires_service}")
    car = CarManager.get_by_id(2)
    print(f"{car} | requires service: {car.requires_service}")
