class PlantError(Exception):
    pass


def water_plants(plant_list: list[str]) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise PlantError("Error: Cannot water None - invalid plant!")
            if plant == "":
                raise PlantError("Error: Cannot water empty - invalid plant!")
            else:
                print(f"Watering {plant}")
    except PlantError as e:
        print(e)
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    normal_list = ["tomato", "lettuce", "carrots"]
    water_plants(normal_list)

    print("")
    print("Testing with error...")
    err_list = ["tomato", None, "carrots"]
    water_plants(err_list)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    try:
        test_watering_system()
    except Exception as e:
        print("Error: ", e)
