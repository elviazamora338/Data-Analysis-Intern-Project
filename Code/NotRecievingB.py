import sqlite3
import matplotlib.pylab as pie

db = sqlite3.connect('MYDATA.db')
cursor = db.cursor()



# Execute an SQL query to select rows where the 'field30' column contains the keyword
cursor.execute("SELECT * FROM CDCB WHERE LOWER(field38) LIKE %not receiving% AND LOWER(field38) LIKE %unemployment%")

# Fetch the matching rows
matching_rows = cursor.fetchall()
overall = len(matching_rows)


# Initialize a counter for the number of women
brownsville = 0
harlingen = 0
losFresnos = 0
sanBenito = 0
rioHondo = 0
spi = 0
lagunaHeights = 0
lagunaVista = 0
olimito = 0
palmValley = 0
portIsabel = 0
others = 0

# Count how many of the matching rows have 'female' or 'Female' in 'field32 and 'brownsville' or 'Brownsville'
for row in matching_rows:
    if row[25].lower() == 'brownsville' or row[25].lower() == 'browwnsville' or row[25].lower() == 'brownsvilee':
        brownsville += 1
    elif row[25].lower() == 'harlingen' :
        harlingen += 1
    elif row[25].lower() == 'los fresnos' :
        losFresnos += 1
    elif row[25].lower() == 'san benito' :
        sanBenito += 1
    elif row[25].lower() == 'rio hondo' :
        rioHondo += 1
    elif row[25].lower() == 'south padre island' :
        spi += 1
    elif row[25].lower() == 'laguna heights' :
        lagunaHeights += 1
    elif row[25].lower() == 'laguna vista' :
        lagunaVista += 1
    elif row[25].lower() == 'olmito' :
        olimito += 1
    elif row[25].lower() == 'palm valley' :
        palmValley += 1
    elif row[25].lower() == 'port isabel' :
        portIsabel += 1
    else:
        others += 1

    


#percentage of women
percentageB = round(((brownsville/overall) *100),2)

percentageH = round(((harlingen/overall) *100),2)

percentageLF = round(((losFresnos/overall) *100),2)

percentageSB = round(((sanBenito/overall) *100),2)

percentageRH = round(((rioHondo/overall) *100),2)

percentageSPI = round(((spi/overall) *100),2)

percentageLH = round(((lagunaHeights/overall) *100),2)

percentageLV = round(((lagunaVista/overall) *100),2)

percentageO = round(((olimito/overall) *100),2)

percentagePV = round(((palmValley/overall) *100),2)

percentagePI = round(((portIsabel/overall) *100),2)

percentageOthers = round(((others/overall) *100),2)

#others = 100 - (percentageB+percentageH)

#rounded
db.close()

print(f"Total women: {brownsville}")

print(f"Total men: {harlingen}")

print(f"Total people: {overall}")



#pie chart

sizes = [percentageB, percentageH, percentageLF, percentageSB, percentageRH,percentageSPI, percentageLH, percentageLV, percentageO, percentagePV, percentagePI, percentageOthers]
labels = ['Brownsvile', 'Harlingen', 'Los Fresnos', 'San Benito', 'Rio Hondo', 'SPI', 'Laguna Heights', 'LagunaVista', 'Olmito', 'Palm Valley', 'Port Isabel', 'Others Cities']
colors = ['#9CCFE7',    '#FFFFC2',    '#89C9B8',    '#977FD7',     '#EC46C3','#FFB31C','#FF5750',      '#FFC0CB',     '#BDDEA9','#E37383',    '#B242BB' ,     '#EDB4B4' ]

#EDB4B4

# Create a pie chart
pie.pie(sizes, autopct='', startangle=140, colors=colors)
pie.title('Percentage of People Not Receiving Unemployment')
pie.axis('equal')

# Add a combined legend with labels and percentages on the side
legend_labels = [f"{label} ({size:.1f}%%)" for label, size in zip(labels, sizes)]
pie.legend(legend_labels, title="Cities", bbox_to_anchor=(0.8, 0.5), loc="center left")


pie.show()

