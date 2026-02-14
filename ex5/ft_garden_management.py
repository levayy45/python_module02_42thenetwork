class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(
        self, plant_name: str, water_level: int, sunlight_hours: int,
            water_tank: int) -> None:
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.water_tank = water_tank

    def add_plant(self) -> str:
        if self.plant_name == "":
            raise ValueError("Error adding plant: Plant name cannot be empty!")
        return f"Added {self.plant_name} successfully"

    def water_plant(self) -> str:
        if self.plant_name == "":
            raise PlantError("Error: Cannot water None - invalid plant!")
        return f"Watering {self.plant_name} - success"

    def check_plant_health(self) -> str:
        if not (1 <= self.water_level <= 10):
            if self.water_level > 10:
                raise ValueError(
                    f"Error checking {self.plant_name}: Water level "
                    f"{self.water_level} is too high (max 10)"
                    )
            else:
                raise ValueError(
                    f"Error checking {self.plant_name}: Water level "
                    f"{self.water_level} is too low (min 1)"
                    )
        if not (2 <= self.sunlight_hours <= 12):
            if self.sunlight_hours > 12:
                raise ValueError(
                    f"Error checking {self.plant_name}: sunlight hours "
                    f"{self.sunlight_hours} is too high (max 12)"
                    )
            else:
                raise ValueError(
                    f"Error checking {self.plant_name}: sunlight hours "
                    f"{self.sunlight_hours} is too low (min 2)"
                    )
        return (
            f"{self.plant_name}: healthy (water: {self.water_level})"
            f", sun: {self.sunlight_hours}"
        )

    def check_plant_water_tank(self) -> None:
        if self.water_tank < 30:
            raise WaterError("Caught GardenError: Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    dict_plant = {
        "plant0": {
            "name": "tomato",
            "water": 5,
            "sun": 8
        },
        "plant1": {
            "name": "lettuce",
            "water": 15,
            "sun": 8
        },
        "plant2": {
            "name": "",
            "water": 6,
            "sun": 8
        }
    }
    water_tank_level = 20

    print("Adding plants to garden...")
    try:
        for plant_key in dict_plant:
            plant_data = dict_plant[plant_key]
            plant = GardenManager(
                plant_data["name"], plant_data["water"], plant_data["sun"],
                water_tank_level)
            res = plant.add_plant()
            print(res)
    except ValueError as e:
        print(e)

    print("\nWatering plants...\nOpening watering system")
    try:
        for plant_key in dict_plant:
            plant_data = dict_plant[plant_key]
            if plant_data["name"] != "":
                plant = GardenManager(
                    plant_data["name"], plant_data["water"], plant_data["sun"],
                    water_tank_level)
                res = plant.water_plant()
                print(res)
    except PlantError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        for plant_key in dict_plant:
            plant_data = dict_plant[plant_key]
            if plant_data["name"] != "":
                plant = GardenManager(
                    plant_data["name"], plant_data["water"], plant_data["sun"],
                    water_tank_level)
                res = plant.check_plant_health()
                print(res)
    except ValueError as e:
        print(e)

    print("\nTesting error recovery...")
    try:
        plant = GardenManager("test", 5, 8, water_tank_level)
        plant.check_plant_water_tank()
    except WaterError as e:
        print(e)
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
