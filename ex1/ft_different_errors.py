def garden_operations(error_type: str) -> None:

    if error_type == "ValueError":
        try:
            int("talal")
        except ValueError as e:
            raise ValueError("Caught ValueError: invalid literal for int()") from e

    elif error_type == "ZeroDivisionError":
        try:
            1 / 0
        except ZeroDivisionError as e:
            raise ZeroDivisionError("Caught ZeroDivisionError: division by zero") from e

    elif error_type == "FileNotFoundError":
        try:
            f = open("missing.txt", "r")
            f.close()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Caught FileNotFoundError: No such file '{e.filename}'") from e

    elif error_type == "KeyError":
        try:
            dictionary = {"name": "TALAL", "job": "UNEMPLOYED"}
            value: str = dictionary["missing\_plant"]
        except KeyError as e:
            raise KeyError(f"Caught KeyError: '{e.args[0]}'") from e
        
    elif error_type == "multiple":
        try:
            dictionary = {"name": "TALAL", "job": "UNEMPLOYED"}
            value: str = dictionary["country"]
        except (ZeroDivisionError, ValueError, Exception) as e:
            raise Exception("Caught an error, but program continues!") from e



def test_error_types() -> None:

    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        garden_operations("ValueError")
    except ValueError as e:
        print(e)

    print("")
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(e)

    print("")
    try:
        print("Testing FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(e)

    print("")
    try:
        print("Testing KeyError...")
        garden_operations("KeyError")
    except KeyError as e:
        print(str(e.args[0]))

    print("")
    try:
        print("Testing multiple errors together...")
        garden_operations("multiple")
    except Exception as e:
        print(e)

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
