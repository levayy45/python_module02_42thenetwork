def check_temperature(temp_str: str) -> int:
    try:
        temp: int = int(temp_str)
    except ValueError as e:
        raise ValueError(f"Error: '{temp_str}' is not a valid number") from e
    if 0 < temp < 40:
        print(f"Temperature {temp}°C is perfect for plants!")
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    else:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    test = ["25", "abc", "100", "-50"]
    for i in test:
        print(f"Testing temperature: {i}")
        try:
            check_temperature(i)
        except ValueError as e:
            print(e)
        print("")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
