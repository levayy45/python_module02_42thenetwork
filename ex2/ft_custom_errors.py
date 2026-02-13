class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def check_for_error(error_type: str, valide: int) -> None:
    plant_name = "tomato"
    if error_type == "PlantError":
        if valide == 1:
            raise PlantError(f"Caught {PlantError.__name__}: The {plant_name} plant is wilting!")
        else:
            raise PlantError(f"The {plant_name} plant is wilting!")
    elif error_type == "WaterError":
        if valide == 1:
            raise WaterError(f"Caught {WaterError.__name__}: Not enough water in the tank!")
        else:
            raise WaterError("Not enough water in the tank!")


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print(f"Testing {PlantError.__name__}...")
        check_for_error("PlantError", 1)
    except PlantError as e:
        print(e)

    print("")
    try:
        print(f"Testing {WaterError.__name__}...")
        check_for_error("WaterError", 1)
    except WaterError as e:
        print(e)

    print("")
    print("Testing catching all garden errors...")
    my_list = ("PlantError", "WaterError")
    for err in my_list:
        try:
            print("Caught a garden error: ", end="")
            check_for_error(err, 0)
        except GardenError as e:
            print(e)
    
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
