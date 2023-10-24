import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect("MYDATA.db")
cursor = db.cursor()
# Locations and their corresponding variables
locations = [
    "brownsville",
    "harlingen",
    "los fresnos",
    "la feria",
    "san benito",
    "rio hondo",
    "south padre island",
    "laguna heights",
    "laguna vista",
    "olmito",
    "port isabel",
]
avg_rent_values = []

# Retrieve average rent values for each location
for location in locations:
    cursor.execute(f"SELECT AVG(field80) FROM CDCB WHERE LOWER(field26) = ?", (location.lower(),))
    avg_rent = cursor.fetchone()[0]
    avg_rent_values.append(avg_rent)
    print(f"Average {location.capitalize()}: {avg_rent}")

# Close the database connection
db.close()


# Colors for the bars
colors = ['blue', 'green', 'red', 'purple', 'orange', 'pink', 'cyan', 'magenta', 'lime', 'teal', 'brown', 'gray']
# Create a histogram with custom colors and labels
plt.bar(locations, avg_rent_values, color=colors)
plt.xlabel('Locations (Palm Valley not reported)')
plt.ylabel('Average Rent')
plt.title('Average Rent by Location')

plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
# Add average rent values as text labels under the bars
for x, y in zip(locations, avg_rent_values):
    plt.text(x, y, round(y, 2), ha='center', va='bottom')
plt.show()


