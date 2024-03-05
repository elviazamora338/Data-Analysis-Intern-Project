import sqlite3
import matplotlib.pylab as plt

db = sqlite3.connect('MYDATA.db')
cursor = db.cursor()

countF = 0
countM = 0


cursor.execute("SELECT field39, field30 FROM CDCB WHERE LOWER(field39) LIKE '%child%' ")
matching = cursor.fetchall()
total = len(matching)

for row in matching:
    if row[1].lower() == 'female':
        countF +=1

if(countF > 0):
    #percentage
    percentageF = round((countF/total *100),2)
else:
    percentageF = 0
    
#closing database connection
db.close()

print(f"total people: {countF}")
print(f"total medical: {total}")

#pie chart
size = [percentageF, 100- percentageF]

labels = ['Females', 'Males']

colors = ['#E6E6FA', '#DCAE96']

plt.pie(size, labels = labels, autopct='%1.1f%%', startangle=140, colors = colors )

plt.title("Percentage of People with Increased Child Or Adult Expenses\n")
# Display the chart
plt.axis('equal')

plt.show()
