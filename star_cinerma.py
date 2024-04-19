class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(self, hall_obj):
        self.hall_list.append(hall_obj)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.hall_no =hall_no
        self.show_list = []
        self.seats = {}

        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.show_list.append((id, movie_name, time))
        matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = matrix

    def book_seats(self, id, seat_positions):
       result = next((tup for tup in self.show_list if id in tup), None)
       if result:
           show_id = result[0]
           seats = self.seats[show_id]

           for seat_pos in seat_positions:
               seats[seat_pos[0]][seat_pos[1]] = 1 
           
           print("Seat is booked successfully!")
       else:
           print("No seats available")
       
    def view_show_list(self):
        for show in self.show_list:
            print(f"{show[1]} is premiering on {show[2]}\n")

    def view_available_seats(self, id):
        print("0 -> Available\n1 -> Not Available")
        print(self.seats[id])

hall = Hall(5,5,1)
hall.entry_show(1, 'dune', '31-12-24')

isRunning = True

while isRunning:
    print("1. View All Shows")
    print("2. View Available Seats")
    print("3. Book Seats")
    print("4. Exit")

    choice = int(input("Enter a choice: "))

    if(choice == 1):
        for show in hall.show_list:
            print(f"{show[1]} is premiering on {show[2]} in hall no. {show[0]}\n")

    if(choice == 2):
        id = int(input("Enter ID: "))
        if id not in hall.seats:
            print("\nInvalid ID\n")
        else:
            for seats in hall.seats[id]:
                print(seats)

    if(choice == 3):
        seat_positions = []
        id = int(input("Enter ID: "))
        if id not in hall.seats:
            print("\nInvalid ID\n")
        else:
            total_seat = int(input("Number of Seats: "))
            if total_seat > hall.rows * hall.cols:
                print("\nSeat number exceeded maximum number of seats.")
            else:
                while(total_seat > 0):
                    row = int(input("Enter Row Number: "))
                    col = int(input("Enter Column Number: "))

                    if(row > hall.rows or col > hall.cols):
                        print("\n Invalid seat number!")
                        continue
                    
                    seats = hall.seats[id]

                    if(seats[row][col] == 1):
                        print("\nSeat is already booked\n")
                        continue

                    seat_positions.append((row, col))    
                    hall.book_seats(id, seat_positions)

                    total_seat -= 1

    if(choice == 4):
        break
            