from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"Fare: ${taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()
