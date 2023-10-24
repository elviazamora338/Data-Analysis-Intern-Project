import sqlite3;
import matplotlib.pyplot as plt

#connection to my data base
db = sqlite3.connect("MYDATA.db")
cursor = db.cursor()

#array holding number of rooms
bedrooms = ["1","2", "3", "4", "5"]

#array to store rent avg depending on rooms
avgRentVal = []

#for loop to go through bedrooms array
for rooms in bedrooms:
    #searching average rent per room
    cursor.execute("SELECT AVG(field80) FROM CDCB WHERE field79 = ?", (rooms))
    #initializing the average to avgRoomRent
    avgRoomRent = cursor.fetchone()[0]
    #adding the average value into the avgRentVal array
    avgRentVal.append(avgRoomRent)
    #prints the average room rent
    print(f"Average room rent: {rooms}: {avgRoomRent}")
#closing the connection
db.close()

#histogram code

# colors for the bars
colors = ['blue', 'green', 'red', 'purple', 'pink']
# creates a histogram with the colors, labels, and avg rent values
plt.bar(bedrooms, avgRentVal, color=colors)
plt.xlabel('Number Of Rooms')
plt.ylabel('Average Rent')
plt.title('Average Rent By Number of Rooms')

plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
# Adds average rent values as text labels under the bars
for x, y in zip(bedrooms, avgRentVal):
    plt.text(x, y, round(y, 2), ha='center', va='bottom')
plt.show()

