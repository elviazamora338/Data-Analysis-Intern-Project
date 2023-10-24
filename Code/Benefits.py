import sqlite3
import matplotlib.pylab as pie

db = sqlite3.connect('MYDATA.db')
cursor = db.cursor()

# Initialize a dictionary to store counts
value_counts = {
    'snap/wic': 0,
    'ssi': 0,
    'tanf': 0,
    'ssdi': 0,
    'chip': 0,
    'medicaid': 0,
    'unemployment': 0,
    'none': 0
}

# Execute an SQL query
cursor.execute("SELECT field128 FROM CDCB")

# Fetch the matching rows
matching_rows = cursor.fetchall()
overall = len(matching_rows)


# Iterate through matching_rows
for row in matching_rows:
    value = row[0]
    if value is not None:
        value = value.lower()
        if value in value_counts:
            value_counts[value] += 1
    else:
        value_counts['none'] += 1

# Access the counts for each value
snapWic = value_counts['snap/wic']
ssi = value_counts['ssi']
tanf = value_counts['tanf']
ssdi = value_counts['ssdi']
chip = value_counts['chip']
medicaid = value_counts['medicaid']
unemployment = value_counts['unemployment']
none = value_counts['none']  



#percentage of women
percentageSW = round(((snapWic/overall) *100),2)

percentageSS = round(((ssi/overall) *100),2)

percentageT = round(((tanf/overall) *100),2)

percentageSD = round(((ssdi/overall) *100),2)

percentageC = round(((chip/overall) *100),2)

percentageM = round(((medicaid/overall) *100),2)

percentageUE = round(((unemployment/overall) *100),2)

percentageN = round(((none/overall) *100),2)


db.close()



#pie chart

sizes = [percentageSW, percentageSS, percentageT, percentageSD, percentageC,percentageM, percentageUE, percentageN]
labels = ['SNAP/WIC' , 'SSI', 'TANF', 'SSDI', 'Chip' , 'Medicaid', 'Unemployment', 'None/Null']
colors = ['#9CCFE7',  '#FFFFC2','#89C9B8', '#977FD7', '#EC46C3','#FFB31C','#FF5750','#FFC0CB']

#EDB4B4

# Create a pie chart
pie.pie(sizes, autopct='', startangle=140, colors=colors)
pie.title('Percentage of People Receiving Public Benefits')
pie.axis('equal')

# Add a combined legend with labels and percentages on the side
legend_labels = [f"{label} ({size:.1f}%%)" for label, size in zip(labels, sizes)]
pie.legend(legend_labels, title="Benefits", bbox_to_anchor=(0.8, 0.5), loc="center left")


pie.show()

