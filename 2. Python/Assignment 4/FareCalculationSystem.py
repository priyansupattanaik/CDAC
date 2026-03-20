class Transport:
    def calculateFare(self, distance):
        pass

class Bus(Transport):
    BASE_FARE = 2.0
    RATE_PER_KM = 0.5
    
    def calculateFare(self, distance):
        fare = self.BASE_FARE + (distance * self.RATE_PER_KM)
        return fare

class Train(Transport):
    BASE_FARE = 5.0
    RATE_PER_KM = 0.3
    
    def calculateFare(self, distance):
        fare = self.BASE_FARE + (distance * self.RATE_PER_KM)
        return fare

class Taxi(Transport):
    BASE_FARE = 3.0
    RATE_PER_KM = 2.0
    
    def calculateFare(self, distance):
        fare = self.BASE_FARE + (distance * self.RATE_PER_KM)
        return fare

print("Available Transport:")
print("1. Bus")
print("2. Train")
print("3. Taxi")

choice = int(input("Choose transport (1-3): "))
distance = float(input("Enter distance: "))

if choice == 1:
    transport = Bus()
elif choice == 2:
    transport = Train()
else:
    transport = Taxi()

fare = transport.calculateFare(distance)
print(f"Fare for {distance} km: ${fare:.2f}")

transports = [Bus(), Train(), Taxi()]
names = ["Bus", "Train", "Taxi"]

for i, t in enumerate(transports):
    fare = t.calculateFare(distance)
    print(f"{names[i]} fare:{fare:.2f}")