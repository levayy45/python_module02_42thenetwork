class PlantError(Exception):
    pass


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    for plant in plant_list:
        if plant == "imposter":
            raise PlantError("Error: Cannot water None - invalid plant!")
        else:
            print(f"Watering {plant}")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    normal_list = ("tomato", "lettuce", "carrots")
    succes: bool = False
    try:
        water_plants(normal_list)
        succes = True
    except PlantError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    if succes:
        print("Watering completed successfully!")

    succes = False
    print("")
    print("Testing with error...")
    err_list = ("tomato", "imposter")
    try:
        water_plants(err_list)
        succes = True
    except PlantError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    if succes:
        print("Watering completed successfully!")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
