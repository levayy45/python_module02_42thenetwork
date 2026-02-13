def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
        ) -> str:
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if not (1 <= water_level <= 10):
        if water_level > 10:
            raise ValueError(
                f"Error: Water level {water_level} is too high (max 10)"
                )
        else:
            raise ValueError(
                f"Error: Water level {water_level} is too low (min 1)"
                )
    if not (2 <= sunlight_hours <= 12):
        if sunlight_hours > 12:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
                )
        else:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
                )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    try:
        print("Testing good values...")
        res = check_plant_health("tomato", 5, 5)
        print(res)
    except ValueError as e:
        print(e)

    print("")
    try:
        print("Testing empty plant name...")
        res = check_plant_health("", 5, 5)
        print(res)
    except ValueError as e:
        print(e)

    print("")
    try:
        print("Testing bad water level...")
        res = check_plant_health("name", 15, 5)
        print(res)
    except ValueError as e:
        print(e)

    print("")
    try:
        print("Testing bad sunlight hours...")
        res = check_plant_health("name", 5, 0)
        print(res)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
