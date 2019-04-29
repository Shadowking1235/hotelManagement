class hotelkingston:

    def __init__(self, rt='', n=0, s=0,r=0,c = 0, d = 0, a = 1800, Name='',Address='', cindate = '', coutdate='', rowno = 100):

        print("WELCOME TO KINGSTON HOTEL")
        print("Izhevsk, Russia, Pecochnaya 38A 426069:\n")

        self.rt = rt
        self.r = r
        self.t = ''
        self.a = a
        self.n = n
        self.s = s
        self.c = c
        self.d = d
        self.Name = Name
        self.address = Address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rowno = rowno

    def inputData(self):
        self.Name = input("Enter your Name:")
        self.Address = input("Enter your Address:")
        self.cindate = input("Enter your Arrival date:")
        self.coutdate = input("Enter your Departure date:")
        print("Your room no.:", self.rowno, "\n")

    def roomRent(self):
        print(" Please select your category of room:-")
        print("Note that prices are just for a night ")
        print("1. Single_Room -- $50 \n")
        print("2. Double_Room --$100 \n")
        print("3. Triple_Room -- $150 \n")
        print("4. Queens_Room --$250 \n")
        print("5. kings_Room --$400 \n")

        x = int(input(" Please enter Your Choice Please from One(1) - Five(5) "))
        n = int(input(" How many nights would you like to stay:"))

        if (x == 1):
            print("Thanks for choosing a Single_Room")
            self.s = 50 * n

        elif (x == 2):
            print("Thanks for choosing a Double_Room")
            self.s = 100 * n

        elif (x == 3):
            print("Thanks for choosing a Triple_Room")
            self.s = 150 * n

        elif (x == 4):
            print("Thanks for choosing a Queens_Room")
            self.s = 250 * n
        elif (x == 5):
            print("Thanks for choosing a Kings_Room")
            self.s = 400 * n

        else:
            print(" Please choose a room")
        print(" Rent  =", self.s, "\n")

    def restaurentBill(self):
        print("RESTAURANT MENU")
        print("1.Water = $0.5 ",
              "2.Tea = $0.75",
              "3.Breakfast porridge = $2.00",
              "4.Lunch meat spaghetti = $5.00",
              "5.Dinner potatoes fries = $ 3.50",
              "6.Exit")

        while (1):
            c = int(input("Enter your choice:"))
            if (c == 1):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 0.5 * d

            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 0.75 * d

            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 2.00 * d

            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 5.00 * d

            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 3.50 * d

            elif (c == 6):
                break;
            else:
                print("Invalid option")

        print("Total food Cost= $", self.r, "\n")

    def gamebill(self):
        print("GAME MENU")
        print("1.Table_tennis = $5.00", "2.Bowling = $10.00","3.Video_games = $10.00",
              "4.Pool = $15.00", "5.Exit")

        while (1):

            g = int(input("Enter your choice:"))
            if (g == 1):
                h = int(input("No. of hours required:"))
                self.p = self.p + 5.00 * h

            elif (g == 2):
                h = int(input("No. of hours:"))
                self.p = self.p + 10.00 * h

            elif (g == 3):
                h = int(input("No. of hours:"))
                self.p = self.p + 10.00 * h

            elif (g == 4):
                h = int(input("No. of hours:"))
                self.p = self.p + 15.00 * h

            elif (g == 5):
                break;

            else:

                print("Invalid option")

        print("Total Game Bill=$", self.p, "\n")

    def display(self):
        a = hotelkingston()
        print("HOTEL BILl")
        print("Clients Information:")
        print("Clients Name:", self.Name)
        print("Clients Address:", self.Address)
        print("Arrival Date:", self.cindate)
        print("Departure Date", self.coutdate)
        print("Room_no.", self.rowno)
        print("Rent:", self.s)
        print("Food bill:", self.r)
        print("Game bill :", self.p)

        self.rt = self.s + self.t + self.p + self.r

        print("Sub total bill:", self.rt)
        print("Additional Service Charges ", self.a)
        print("Grandtotal bill :", self.rt + self.a, "\n")
        self.rno += 1


def main():
    a = hotelkingston()
    while (1):
        print("1.Enter Clients Information")
        print("2.Calculate Rent")
        print("3.Calculate Restaurant_bill")
        print("4.Calculate Game_bill")
        print("5.Total_cost")
        print("6.EXIT")

        b = int(input("enter your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.roomrent()

        if (b == 3):
            a.restaurentbill()

        if (b == 4):
            a.gamebill()

        if (b == 5):
            a.display()

        if (b == 6):
            quit()


            main()


