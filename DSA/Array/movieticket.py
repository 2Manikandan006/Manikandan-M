class MovieTicketBookingSystem:
    def __init__(self, rows, cols):
        self.seats = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append('O')
            self.seats.append(row)   #[['O', 'O', 'O', 'O', 'O']]
        self.rows = rows
        self.cols = cols

    def display_seats(self):
        print("\n Current Seating Arrangement")

        for col in range(1, cols + 1):
            print(col, end= " ")   # 1 2 3 4 5
        print()

        for i in range(self.rows):
            print(f"{i + 1}", end= " ")  # 1 2 3 4 5
            for j in range(self.cols):
                print(self.seats[i][j], end= " ")  # prints 'O' if available or print 'X' if it is Booked
            print()

    def book_seat(self, row, col):
        if self.seats[row-1][col-1] == 'O':
            self.seats[row-1][col-1] = 'X'
            print(f"Seat ({row}, {col}) successfully booked.")
        else:
            print(f"Seat ({row}, {col}) is already booked. Please choose another seat.")

    def cancel_seat(self, row, col):
        if self.seats[row-1][col-1] == 'X':
            self.seats[row-1][col-1] = 'O'
            print(f"Booking for seat ({row} {col}) has been cancelled")
        else:
            print(f"Seat ({row} {col}) is not booked")

    def show_booked_seats(self):
        booked_seats = []

        for i in range(self.rows):
            for j in range(self.cols):
                if self.seats[i][j] == 'X':
                    booked_seats.append((i + 1, j + 1))

        if len(booked_seats) > 0:
            print("Booked Seats :")
            for seat in booked_seats:
                print(f"({seat[0]}, {seat[1]})", end= " ")
            print()
        else:
            print("No seats have been booked yet")

if __name__ == "__main__":
    rows = 5
    cols = 5
    booking_system = MovieTicketBookingSystem(rows, cols)

    while True:
        print("\n1. Display Seats")
        print("2. Book Seats")
        print("3. Cancel Seats")
        print("4. Show Booked Seats")
        print("5. Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            booking_system.display_seats()    

        elif choice == 2:
            row = int(input("Enter row number to book : "))
            col = int(input("Enter seat number to book : "))
            booking_system.book_seat(row, col) 

        elif choice == 3:
            row = int(input("Enter the row number to cancel booking : "))
            col = int(input("Enter the seat number to cancel the booking : "))
            booking_system.cancel_seat(row, col)      

        elif choice == 4:
            booking_system.show_booked_seats() 

        elif choice == 5:
            print("Exiting the system. Thank you!. ")
            break

        else:
            print("Invalid choice. Please try again.")                       
