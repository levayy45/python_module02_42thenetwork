class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunlightError(GardenError):
    pass


class GardenManager:
    def __init__(self, water_tank: int) -> None:
        self.plants = {}
        self.water_tank = water_tank

    def add_plant(
        self, plant_name: str, water_level: int, sunlight_hours: int
    ) -> None:
        if plant_name is None:
            raise PlantError("Error adding plant: Plant name cannot be None!")
        if plant_name == "":
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        self.plants[plant_name] = {"water": water_level, "sun": sunlight_hours}
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> str:
        plant = self.plants[plant_name]
        water = plant["water"]
        sun = plant["sun"]
        if not (1 <= water <= 10):
            if water > 10:
                raise WaterError(
                    f"Error checking {plant_name}: Water level "
                    f"{water} is too high (max 10)"
                )
            else:
                raise WaterError(
                    f"Error checking {plant_name}: Water level "
                    f"{water} is too low (min 1)"
                )
        if not (2 <= sun <= 12):
            if sun > 12:
                raise SunlightError(
                    f"Error checking {plant_name}: sunlight hours "
                    f"{sun} is too high (max 12)"
                )
            else:
                raise SunlightError(
                    f"Error checking {plant_name}: sunlight hours "
                    f"{sun} is too low (min 2)"
                )
        return f"{plant_name}: healthy (water: {water}" f", sun: {sun})"

    def check_plant_water_tank(self) -> str:
        if self.water_tank < 30:
            raise GardenError("Caught GardenError: Not enough water in tank")
        return f"Water tank '{self.water_tank}' level is sufficient"


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    dict_plant = {
        "plant0": {"name": "tomato", "water": 5, "sun": 8},
        "plant1": {"name": "lettuce", "water": 15, "sun": 8},
        "plant2": {"name": "", "water": 6, "sun": 8},
    }
    water_tank_level = 20
    manager = GardenManager(water_tank_level)

    print("Adding plants to garden...")
    for plant_key in dict_plant:
        try:
            plant_data = dict_plant[plant_key]
            manager.add_plant(
                plant_data["name"], plant_data["water"], plant_data["sun"]
            )
        except PlantError as e:
            print(e)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    for plant_key in dict_plant:
        plant_data = dict_plant[plant_key]
        plant_name = plant_data["name"]
        if plant_name:
            try:
                print(manager.check_plant_health(plant_name))
            except WaterError as e:
                print(e)
            except SunlightError as e:
                print(e)

    print("\nTesting error recovery...")
    try:
        print(manager.check_plant_water_tank())
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
