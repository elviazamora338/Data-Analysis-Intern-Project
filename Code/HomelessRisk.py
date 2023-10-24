import sqlite3
import matplotlib.pylab as plt

db = sqlite3.connect("MYDATA.db")
cursor = db.cursor()

total = 0

# Execute the SQL query to count the number of rows for each condition
cursor.execute("SELECT COUNT(*) FROM CDCB WHERE field42 = 'Yes' AND field21 = 'Yes';")
yesCount = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM CDCB WHERE field42 = 'No' AND field21 = 'No';")
noCount = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM CDCB WHERE field42 IS NULL AND field21 IS NULL;")
nullCount = cursor.fetchone()[0]

total = yesCount + noCount + nullCount

if total > 0:
    percentageY = round((yesCount / total * 100), 2)
    percentageN = round((noCount / total * 100), 2)
    percentageNull = round((nullCount / total * 100), 2)
else:
    percentageY = 0
    percentageN = 0
    percentageNull = 0

db.close()

print(f"total yes: {yesCount}")
print(f"Total no: {noCount}")
print(f"Total null: {nullCount}")
print(f"Total: {total}")


#pie chart

sizes = [percentageY, percentageN, percentageNull]

labels = ['A Risk','Not at Risk', 'NA']

colors = ['#cb5382', '#FF007F', '#b21c0e']

plt.pie(sizes, labels = labels, autopct='%1.1f%%', startangle=140, colors = colors)
plt.title('Percentage of People At Risk of housing instability/homelessness')
plt.axis('equal')

plt.show()

