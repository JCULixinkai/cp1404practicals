from prac_09.unreliable_car import UnreliableCar


def main():
    """Tests cars reliability"""
    perfect_car = UnreliableCar("Perfect", 100, 100)
    medium_car = UnreliableCar("Medium", 100, 50)
    bad_car = UnreliableCar("Bad", 100, 10)

    for i in range(1, 20):
        print(f"Trying to drive {i} km")
        print(f"{perfect_car.name} drove {perfect_car.drive(i)}km")
        print(f"{medium_car.name} drove {medium_car.drive(i)}km")
        print(f"{bad_car.name} drove {bad_car.drive(i)}km")

    print("Final values")
    print(perfect_car)
    print(medium_car)
    print(bad_car)


main()
