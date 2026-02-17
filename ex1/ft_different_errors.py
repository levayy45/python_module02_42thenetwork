def garden_operations(error_type: str) -> None:

    if error_type == "ValueError":
        int("talal")

    elif error_type == "ZeroDivisionError":
        1 / 0

    elif error_type == "FileNotFoundError":
        f = open("missing.txt", "r")
        f.close()

    elif error_type == "KeyError":
        dictionary = {"name": "TALAL", "job": "UNEMPLOYED"}
        dictionary["missing_plant"]

    elif error_type == "multiple":
        dictionary = {"name": "TALAL"}
        dictionary["country"]


def test_error_types() -> None:

    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("")
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("")
    try:
        print("Testing FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'")

    print("")
    try:
        print("Testing KeyError...")
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: '{e.args[0]}'")

    print("")
    try:
        print("Testing multiple errors together...")
        garden_operations("multiple")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print("Error: ", e)
