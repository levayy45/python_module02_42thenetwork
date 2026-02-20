def garden_operations() -> None:

    try:
        print("Testing ValueError...")
        int("talal")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("")
    try:
        print("Testing ZeroDivisionError...")
        1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("")
    try:
        print("Testing FileNotFoundError...")
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'")

    print("")
    try:
        print("Testing KeyError...")
        dictionary = {"name": "TALAL", "job": "UNEMPLOYED"}
        dictionary["missing\\_plant"]
    except KeyError as e:
        print(f"Caught KeyError: '{e.args[0]}'")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    garden_operations()

    print("")
    try:
        print("Testing multiple errors together...")
        dictionary = {"name": "TALAL"}
        dictionary["country"]
        1 / 0
        int("talal")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print("Error: ", e)
