class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    def __init__(self):
        self.items = [
            Beverage("Coke", 1.50),
            Beverage("Pepsi", 1.25),
            Beverage("Water", 1.00),
            Beverage("Sprite", 2.00),
            Beverage("Coffee", 1.75),
            Beverage("Gatorade", 1.25)
        ]

    def show_menu(self):
        print("\nChoose a drink:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter a number (1-6): ")

            if not choice.isdigit() or not 1 <= int(choice) <= len(self.items):
                print("Invalid selection.\n")
                continue

            drink = self.items[int(choice) - 1]
            print(f"You selected {drink.name} (${drink.price:.2f})")

            try:
                money = float(input("Insert money: $"))
            except ValueError:
                print("Invalid amount.\n")
                continue

            if money < drink.price:
                print(f"Not enough money. You still owe ${drink.price - money:.2f}.\n")
            elif money == drink.price:
                print(f"Here is your {drink.name}. Enjoy!\n")
            else:
                change = money - drink.price
                print(f"Here is your {drink.name}. Your change is ${change:.2f}.\n")

if __name__ == "__main__":
    machine = VendingMachine()
    machine.run()
