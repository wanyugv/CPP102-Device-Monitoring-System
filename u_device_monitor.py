"""Simulated Device Monitoring and Alert System for CPP102 Week 17."""

def get_initial_readings():
    """Return the initial simulated temperature readings."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Return True when text represents a whole number, including negatives."""
    if len(text) == 0:
        return False

    start = 0
    if text[0] == "-":
        start = 1

    if start == len(text):
        return False

    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False

    return True


def get_valid_integer(prompt, lowest, highest):
    """Keep asking until the user enters a whole number within the range."""
    while True:
        text = input(prompt)

        if len(text) == 0:
            print("Invalid input. The reading cannot be empty.")
        elif not is_whole_number(text):
            print("Invalid input. Enter a whole number only.")
        else:
            value = int(text)
            if value < lowest or value > highest:
                print(f"Invalid reading. Enter a value from {lowest} to {highest}.")
            else:
                return value


def add_reading(readings):
    """Validate one new reading and append it only when valid."""
    text = input("Enter new reading: ")

    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    else:
        reading = int(text)
        if reading < 0 or reading > 100:
            print("Invalid reading. Enter a value from 0 to 100.")
        else:
            readings.append(reading)
            print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return the classification for one temperature reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    """Return the total of all readings using a loop."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Return the average of the readings."""
    if len(readings) == 0:
        return 0
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the smallest reading using a loop."""
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Return the largest reading using a loop."""
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Count how many readings belong to the requested category."""
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def determine_overall_status(warning_count, critical_count):
    """Return the overall status, checking critical readings first."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_readings(readings):
    """Display every reading with its position."""
    print("\nCURRENT READINGS")
    print("----------------")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def display_classifications(readings):
    """Display each reading and its classification."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        category = classify_reading(reading, 30, 35)
        print(f"{reading} °C -> {category}")


def display_summary(readings):
    """Compute and display the numerical and classification summary."""
    if len(readings) == 0:
        print("No readings are available.")
        return

    number_of_readings = len(readings)
    total = compute_total(readings)
    average = total / number_of_readings
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, 30, 35, "NORMAL")
    warning_count = count_category(readings, 30, 35, "WARNING")
    critical_count = count_category(readings, 30, 35, "CRITICAL")

    normal_percentage = normal_count / number_of_readings * 100
    warning_percentage = warning_count / number_of_readings * 100
    critical_percentage = critical_count / number_of_readings * 100
    overall_status = determine_overall_status(warning_count, critical_count)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings : {number_of_readings}")
    print(f"Total of readings : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")
    print()
    print(f"NORMAL : {normal_count} ({normal_percentage:.2f}%)")
    print(f"WARNING : {warning_count} ({warning_percentage:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_percentage:.2f}%)")
    print()
    print(f"Overall Status: {overall_status}")


def display_menu():
    """Display the main menu."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def main():
    """Run the menu loop and coordinate the program functions."""
    readings = get_initial_readings()

    while True:
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            display_classifications(readings)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()