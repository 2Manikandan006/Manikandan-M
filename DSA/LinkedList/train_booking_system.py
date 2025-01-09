class Node:
    def __init__(self, train_name, seats):
        self.train_name = train_name
        self.seats = seats
        self.booked_seats = 0
        self.next = None

class Train_booking:
    def __init__(self):
        self.head = None

    def add_train(self, train_name, seats):
        new_train = Node(train_name, seats)
        if not self.head:
            self.head = new_train
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_train
        print(f"The train {train_name} is added with {seats} seats")

    def display_train(self):
        if not self.head:
            print("There is no train")
            return
        current = self.head
        while current:
            print(f"Train : {current.train_name}, Seats : {current.seats}, Booked seats : {current.booked_seats}, Available seats : {current.seats - current.booked_seats}")
            current = current.next

    def seat_to_book(self, train_name, seat_to_booking):

        current = self.head
        while current:
            if current.train_name == train_name:
                if current.booked_seats + seat_to_booking <= current.seats:
                    current.booked_seats += seat_to_booking
                    print(f"{seat_to_booking} seat(s) booked on train {train_name}")
                else:
                    print(f"Not enough available seats on {train_name}")
                return
            current = current.next
        print(f"{train_name} not found")

    def seat_to_cancel(self, train_name, seat_to_cancel):
        current = self.head
        while current:
            if current.train_name == train_name:
                if current.booked_seats >= seat_to_cancel:
                    current.booked_seats -= seat_to_cancel
                    print(f"{seat_to_booking} seat(s) canceled on train {train_name}")
                else:
                    print(f"Not enough available seats on {train_name}")
                return
            current = current.next
        print(f"{train_name} not found")

if __name__ == "__main__":
    train_booking = Train_booking()

    while True:

        print("\n----Train Booking System----")
        print("1. Add train ")
        print("2. Display_train ")
        print("3. Seat to book ")
        print("4. seat to cancel ")
        print("5. Exit ")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            train_name = input("Enter the name of the train to be added : ")
            seats = int(input("Enter the number of seats : "))
            train_booking.add_train(train_name, seats)

        elif choice == 2:
            train_booking.display_train()

        elif choice == 3:
            train_name = input("Enter the name of the train : ")
            seat_to_booking = int(input("Enter the seats to book : "))
            train_booking.seat_to_book(train_name, seat_to_booking)

        elif choice == 4:
            train_name = input("Enter the name of the train : ")
            seat_to_cancel = int(input("Enter the seats to cancel : "))
            train_booking.seat_to_cancel(train_name, seat_to_cancel)
        
        elif choice == 5:
            print("Exiting..! Thankyou.")
            break

        else:
            print("Invalid input! Please try again.")