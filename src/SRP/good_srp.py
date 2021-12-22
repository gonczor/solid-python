from datetime import datetime

from database import cars_db


class CarModel:
    id: int
    make: str
    model: str
    last_service: int

    def __init__(self, id, make, model, last_service):
        self.id = id
        self.make = make
        self.model = model
        self.last_service = last_service

    def __repr__(self):
        return f"{self.id}: {self.make} {self.model}"


class CarRepository:
    @staticmethod
    def get_by_id(id: int) -> CarModel:
        data = cars_db[id]
        return CarModel(
            id=id,
            **data
        )


class CarManager:
    def __init__(self, car: CarModel):
        self.__car = car

    @property
    def requires_service(self) -> bool:
        return datetime.today().year - 1 > self.__car.last_service


if __name__ == "__main__":
    car = CarRepository.get_by_id(1)
    manager = CarManager(car)
    print(f"{car} | requires service: {manager.requires_service}")
    car = CarRepository.get_by_id(2)
    manager = CarManager(car)
    print(f"{car} | requires service: {manager.requires_service}")
