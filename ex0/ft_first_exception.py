def check_temperature(temp_str: str) -> int:

    try:
        temp: int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")

    if not (0 <= temp <= 40):
        if temp < 0:
            raise ValueError(
                f"Error: {temp}°C is too cold for plants (min 0°C)"
                )
        else:
            raise ValueError(
                f"Error: {temp}°C is too hot for plants (max 40°C)"
                )
    return temp


def test_temperature_input() -> None:

    print("=== Garden Temperature Checker ===\n")

    test = ["25", "abc", "100", "-50"]

    for i in test:
        print(f"Testing temperature: {i}")
        try:
            valid_temp = check_temperature(i)
            print(f"Temperature {valid_temp}°C is perfect for plants!")
        except ValueError as e:
            print(e)
        print("")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print("Error: ", e)
