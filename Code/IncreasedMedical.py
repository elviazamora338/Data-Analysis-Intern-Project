import sqlite3
import matplotlib.pylab as plt

db = sqlite3.connect("MYDATA.db")
cursor = db.cursor()


cursor.execute("SELECT COUNT(*) FROM CDCB WHERE LOWER(field39) LIKE %medical expenses%")
totalME = cursor.fetchone()[0]

cursor.execute("SELECT field39 FROM CDCB")
totalOthers = cursor.fetchall()
others = len(totalOthers)


if totalME > 0:
    percentageME = round((totalME/others *100),2)

db.close()

print(f"total medical: {totalME}")
print(f"total people: {others}")

sizes = [percentageME,100 - percentageME]

labels = ['Increased Medical Expenses', 'Other Expenses/Null']
colors = ['#4F7942', '#98FB98']

plt.pie(sizes, labels = labels, autopct='%1.1f%%', startangle=140, colors = colors)

plt.title("People with Increased Medical Expenses")
plt.axis('equal')

plt.show()
