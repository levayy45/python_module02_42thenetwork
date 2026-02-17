class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunlightError(GardenError):
    pass


class GardenManager:
    def __init__(
        self, plant_name: str, water_level: int, sunlight_hours: int,
            water_tank: int) -> None:
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.water_tank = water_tank
        self.is_planted = False

    def add_plant(self) -> str:
        if self.plant_name is None:
            raise PlantError("Error adding plant: Plant name cannot be None!")
        if self.plant_name == "":
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        self.is_planted = True
        return f"Added {self.plant_name} successfully"

    def water_plant(self) -> str:
        if not self.is_planted:
            return None
        return f"Watering {self.plant_name} - success"

    def check_plant_health(self) -> str:
        if not self.is_planted:
            return None
        if not (1 <= self.water_level <= 10):
            if self.water_level > 10:
                raise WaterError(
                    f"Error checking {self.plant_name}: Water level "
                    f"{self.water_level} is too high (max 10)"
                    )
            else:
                raise WaterError(
                    f"Error checking {self.plant_name}: Water level "
                    f"{self.water_level} is too low (min 1)"
                    )
        if not (2 <= self.sunlight_hours <= 12):
            if self.sunlight_hours > 12:
                raise SunlightError(
                    f"Error checking {self.plant_name}: sunlight hours "
                    f"{self.sunlight_hours} is too high (max 12)"
                    )
            else:
                raise SunlightError(
                    f"Error checking {self.plant_name}: sunlight hours "
                    f"{self.sunlight_hours} is too low (min 2)"
                    )
        return (
            f"{self.plant_name}: healthy (water: {self.water_level}"
            f", sun: {self.sunlight_hours})"
        )

    def check_plant_water_tank(self) -> str:
        if self.water_tank < 30:
            raise GardenError("Caught GardenError: Not enough water in tank")
        return f"Water tank '{self.water_tank}' level is sufficient"


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    dict_plant = {
        "plant0": {"name": "tomato", "water": 5, "sun": 8},
        "plant1": {"name": "lettuce", "water": 15, "sun": 8},
        "plant2": {"name": "", "water": 6, "sun": 8}
    }
    water_tank_level = 20

    plants = {}
    for plant_key in dict_plant:
        plant_data = dict_plant[plant_key]
        plants[plant_key] = GardenManager(
            plant_data["name"], plant_data["water"],
            plant_data["sun"], water_tank_level
        )
    print("Adding plants to garden...")
    for plant_key in plants:
        try:
            print(plants[plant_key].add_plant())
        except PlantError as e:
            print(e)

    print("\nWatering plants...\nOpening watering system")
    try:
        for plant_key in plants:
            result = plants[plant_key].water_plant()
            if result:
                print(result)
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    for plant_key in plants:
        try:
            result = plants[plant_key].check_plant_health()
            if result:
                print(result)
        except WaterError as e:
            print(e)
        except SunlightError as e:
            print(e)

    print("\nTesting error recovery...")
    try:
        plant = GardenManager("test", 5, 8, water_tank_level)
        print(plant.check_plant_water_tank())
    except GardenError as e:
        print(e)
        print("System recovered and continuing...")

    finally:
        print("\nGarden management system test complete!")


if __name__ == "__main__":
    try:
        test_garden_management()
    except Exception as e:
        print("Error: ", e)
