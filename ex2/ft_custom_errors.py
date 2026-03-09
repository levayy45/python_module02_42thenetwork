class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def raise_plant_error(plant_name: str) -> None:
    raise PlantError(f"The {plant_name} plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise_plant_error("tomato")
    except PlantError as e:
        print(f"Caught {PlantError.__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print(f"Caught {WaterError.__name__}: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise_plant_error("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    try:
        test_custom_errors()
    except Exception as e:
        print("Error: ", e)
