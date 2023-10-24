import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
myDB = sqlite3.connect('MYDATA.db')
#.cursor() used to make queries in the database
cursor = myDB.cursor()

# To count the number of female records in the 'field30' column
cursor.execute("SELECT COUNT(*) FROM CDCB WHERE field30 = 'Female'")
# Retrieves the count of female records from the result of the SQL query and assigns that count to femaleCount
femaleCount = cursor.fetchone()[0]

# Count the total number of records in the 'field30' column (including null values)
cursor.execute("SELECT COUNT(field30) FROM CDCB")
total_count = cursor.fetchone()[0]

# Calculate the percentage of females based on non-null, non-empty values
if femaleCount > 0:
    percentageF = (femaleCount / total_count) * 100
else:
    percentageF = 0  # To avoid division by zero if there are no records


# Round the percentage to two decimal places
roundedF = round(percentageF, 2)

# Closing the database
myDB.close()

# Print the percentage of females
print(f"Percentage of females in the 'gender' column: {roundedF}%")

# Create a pie chart
labels = ['Female', 'Male']
sizes = [roundedF, 100 - roundedF]
colors = ['#ff9999', '#66b3ff']

# autopct = how the percent will be formatted
# startangle affects the initial rotation of the pie chart but doesn't change the actual data or proportions.
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

# Add a title
plt.title('Female Percentage'+ '\n')

# Display the chart
plt.axis('equal')
plt.show()