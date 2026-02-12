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
            raise FileNotFoundError("Caught FileNotFoundError: No such file 'missing.txt'") from e

    elif error_type == "KeyError":
        try:
            dictionary = {"name": "TALAL", "job": "UNEMPLOYED"}
            value: str = dictionary["country"]
        except KeyError as e:
            raise KeyError("Caught KeyError: 'missing\_plant'") from e


def test_error_types() -> None:

    print("=== Garden Error Types Demo ===")

    try:
        print("Testing ValueError...")
        garden_operations("ValueError")
    except ValueError as e:
        print(e)

    try:
        print("Testing ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(e)

    try:
        print("Testing FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(e)

    try:
        print("Testing KeyError...")
        garden_operations("KeyError")
    except FileNotFoundError as e:
        print(e)

