# Car Management
# - car: object
# - instance variables: current_speed, fuel
# - instance methods: accelerate(), brake(), speed()


class Car:
    def __init__(self, name, speed=0, fuel=100, minimum_speed=0, maximum_speed=200):
        self.name = name.strip()
        self.minimum_speed = minimum_speed
        self.maximum_speed = maximum_speed
        self.current_speed = max(self.minimum_speed, min(speed, self.maximum_speed))
        self.fuel = max(0, fuel)

    def accelerate(self, amount):
        if amount <= 0:
            print("Acceleration amount must be greater than 0.")
            return

        if self.fuel <= 0:
            print(f"{self.name} cannot accelerate. Fuel is empty.")
            return

        available_increase = self.maximum_speed - self.current_speed
        if available_increase <= 0:
            print(f"{self.name} is already at maximum speed: {self.maximum_speed} km/h")
            return

        speed_increase = min(amount, available_increase)
        self.current_speed += speed_increase

        fuel_used = max(1, speed_increase // 10)
        self.fuel = max(0, self.fuel - fuel_used)

        print(f"{self.name} accelerated by {speed_increase} km/h")
        self.speed()

    def brake(self, amount):
        if amount <= 0:
            print("Brake amount must be greater than 0.")
            return

        previous_speed = self.current_speed
        self.current_speed = max(self.minimum_speed, self.current_speed - amount)
        reduced_by = previous_speed - self.current_speed

        print(f"{self.name} slowed down by {reduced_by} km/h")
        self.speed()

    def speed(self):
        print(
            f"{self.name} | Speed: {self.current_speed} km/h | "
            f"Fuel: {self.fuel}% | Range: {self.minimum_speed}-{self.maximum_speed}"
        )


def get_int(prompt, minimum=None, maximum=None):
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if minimum is not None and value < minimum:
            print(f"Please enter a value >= {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"Please enter a value <= {maximum}.")
            continue

        return value


def create_car(cars):
    car_name = input("Enter car name: ").strip()
    if not car_name:
        print("Car name cannot be empty.")
        return
    if car_name in cars:
        print("A car with this name already exists.")
        return

    speed = get_int("Enter initial speed: ", minimum=0)
    fuel = get_int("Enter fuel percentage (0-100): ", minimum=0, maximum=100)
    minimum_speed = get_int("Enter minimum speed: ", minimum=0)
    maximum_speed = get_int("Enter maximum speed: ", minimum=minimum_speed)

    cars[car_name] = Car(
        name=car_name,
        speed=speed,
        fuel=fuel,
        minimum_speed=minimum_speed,
        maximum_speed=maximum_speed,
    )
    print(f"Car '{car_name}' created successfully.")
    cars[car_name].speed()


def select_car(cars):
    if not cars:
        print("No cars available. Create a car first.")
        return None

    print("Available cars:")
    for car_name in cars:
        print(f"- {car_name}")

    selected_name = input("Enter car name: ").strip()
    car = cars.get(selected_name)
    if car is None:
        print("Car not found.")
    return car


def show_all_cars(cars):
    if not cars:
        print("No cars to display.")
        return

    print("\nCar List:")
    for car in cars.values():
        car.speed()


def main():
    cars = {}

    while True:
        print("\n=== Car Management System ===")
        print("1. Create Car")
        print("2. Accelerate Car")
        print("3. Brake Car")
        print("4. Show Car Speed")
        print("5. Show All Cars")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            create_car(cars)
        elif choice == "2":
            car = select_car(cars)
            if car:
                amount = get_int("Enter acceleration amount: ", minimum=1)
                car.accelerate(amount)
        elif choice == "3":
            car = select_car(cars)
            if car:
                amount = get_int("Enter brake amount: ", minimum=1)
                car.brake(amount)
        elif choice == "4":
            car = select_car(cars)
            if car:
                car.speed()
        elif choice == "5":
            show_all_cars(cars)
        elif choice == "6":
            print("Exiting Car Management System.")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")


if __name__ == "__main__":
    main()