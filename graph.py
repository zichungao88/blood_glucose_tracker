import pandas
from matplotlib import pyplot

pyplot.style.use('seaborn')

data = pandas.read_csv('veri_data_export.csv')
date_time = data['base_time_string']
date_data = data['glucose_value']

pyplot.plot_date(date_time, date_data, linestyle='solid')
pyplot.gcf().autofmt_xdate()

pyplot.title('Glucose Levels ([INSERT DATE])')
pyplot.xlabel('Time')
pyplot.ylabel('Value')

pyplot.grid(True)
pyplot.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

pyplot.show()
