# --------------------- People and Plane class ------------------------------- #

# This class is to assign seats to people
class People:

    filled_seats = 0     # Global Variable for this class

    def __init__(self, number_of_people, seatsMatrix, seats):
        self.number_of_people = number_of_people
        self.seatsMatrix = seatsMatrix
        self.seats = seats
        self.length = len(seatsMatrix)


    #  Fuction for filling aisle seats of the plane
    def fill_aisle_seat(self):
        row = 0
        tempFilled = -1
        while People.filled_seats < self.number_of_people and People.filled_seats != tempFilled:
            
            tempFilled = People.filled_seats

            for i in range(self.length):
                
                if self.seatsMatrix[i][1] > row:
                    
                    People.filled_seats += 1
                    
                    if i == 0 and self.seatsMatrix[i][0] > 1:
                        aisleCol = self.seatsMatrix[i][0] - 1
                        self.seats[i][row][aisleCol] = People.filled_seats
                        if People.filled_seats >= self.number_of_people:
                            break
                    
                    elif i == self.length - 1 and self.seatsMatrix[i][0] > 1:
                        aisleCol = 0
                        self.seats[i][row][aisleCol] = People.filled_seats
                        if People.filled_seats >= self.number_of_people:
                            break
                    
                    else:
                        aisleCol = 0
                        self.seats[i][row][aisleCol] = People.filled_seats
                        if People.filled_seats >= self.number_of_people:
                            break
                        if self.seatsMatrix[i][0] > 1:
                            People.filled_seats += 1
                            aisleCol = self.seatsMatrix[i][0] - 1
                            self.seats[i][row][aisleCol] = People.filled_seats
                            if People.filled_seats >= self.number_of_people:
                                break
            row += 1


    #  Fuction for filling window seats of the plane
    def fill_window_seats(self):
        row = 0
        tempFilled = 0
        
        while People.filled_seats < self.number_of_people and People.filled_seats != tempFilled: 
            
            tempFilled = People.filled_seats
            
            if self.seatsMatrix[0][1] > row:
                People.filled_seats += 1
                window = 0
                seats[0][row][window] = People.filled_seats
                if People.filled_seats >= self.number_of_people:
                    break
            
            if self.seatsMatrix[self.length - 1][1] > row:
                People.filled_seats += 1
                window = self.seatsMatrix[self.length-1][0] - 1
                self.seats[self.length- 1][row][window] = People.filled_seats
                if People.filled_seats >= self.number_of_people:
                    break
            
            row += 1

    #  Fuction for filling center seats of the plane
    def fill_center_seats(self):
        row = 0
        tempFilled = 0
        while People.filled_seats < self.number_of_people and People.filled_seats != tempFilled:
            tempFilled = People.filled_seats

            for i in range(self.length):
                if self.seatsMatrix[i][1] > row: 
                        if self.seatsMatrix[i][0] > 2:
                            for col in range(1, self.seatsMatrix[i][0] - 1):
                                People.filled_seats += 1
                                self.seats[i][row][col] = People.filled_seats
                                if People.filled_seats >= self.number_of_people:
                                    break
            row += 1









# This class constructs the seating output
class Plane:


    def __init__(self, seatMatrix):
        self.seatMatrix = seatMatrix
        self.length = len(seatMatrix)
        self.seats = self.construct(seatMatrix)

    
    # function to create a seat matrix with empty seats
    def construct(self, seatMatrix):
        seats = []
        for i in self.seatMatrix:
            rows = i[1]
            cols = i[0]
            mat = []                      # this will be for one block
            for i in range(rows):
                mat.append([-1]*cols)
            seats.append(mat)
        return seats
    
    
    # Function to display seating arrangements on console
    def printSeats(self, number_of_people):

        for i in range(3):                              #To create space in terminal 
            print()


        blksize = len(str(number_of_people))            #Space For Writing SeatNumbers
        rows = [x[1] for x in self.seatMatrix]
        cols = [x[0] for x in self.seatMatrix]
        maxi = max(rows)
        top = True
        for i in range(maxi):
            rowlist = []
            rowlistl = []                               # Creating seat design 
            for j in range(self.length):
                row = " "
                rowl = " "
                if len(self.seats[j]) <= i:
                    for k in range(cols[j]):
                        row += " "*blksize
                        rowl += " "*blksize
                        row += " "
                        rowl += " "
                else:
                    row = "|"
                    rowl = "+"
                    for k in self.seats[j][i]:
                        if k == -1:
                            row += " "*blksize
                        else:
                            row += str(k) +(' '*(blksize - len(str(k))))
                        rowl += "-"*blksize
                        row += "|"
                        rowl += "+"

                rowlist.append(row)
                rowlistl.append(rowl)
            if top:
                print('    '.join(rowlistl))
                top = False
            print('    '.join(rowlist))
            print('    '.join(rowlistl))







 # --------------------------- Test Cases ------------------------------ #

if __name__ == "__main__":

    tests = 2

    test_number_of_people = [12, 36]
    
    
    test_seats_matrix = [
        [[3,4], [4,5], [2,3], [3,4]],
        [[3,2], [4,3], [2,3], [3,4]]
        ]


       

 # ------------------------------ Calling functions -------------------------------- #

    
    for i in range(tests):                   # Intermatching of Test Cases
        for j in range(tests):

            aeroplane = Plane( test_seats_matrix[i] )
            seats = aeroplane.seats


            persons = People(test_number_of_people[j] , test_seats_matrix[i], seats)
            persons.fill_aisle_seat()
            persons.fill_window_seats()
            persons.fill_center_seats()


            aeroplane.printSeats(test_number_of_people[j])
            People.filled_seats = 0
        

# ------------------------------- Task completed successfully :) ----------------------- #



