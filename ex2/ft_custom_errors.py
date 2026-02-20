class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    plant_name = "tomato"
    print("Testing PlantError...")
    try:
        raise PlantError(f"The {plant_name} plant is wilting!")
    except PlantError as e:
        print(f"Caught {PlantError.__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught {WaterError.__name__}: {e}")

    print("\nTesting catching all garden errors...")
    errors = [
        PlantError(f"The {plant_name} plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]
    for err in errors:
        try:
            raise err
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print("Error: ", e)
