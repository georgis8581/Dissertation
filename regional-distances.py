import googlemaps
import pandas as pd
import xlsxwriter

excel = pd.ExcelFile(r'C:/Users/georg/Documents/Transport and Business Management - Imperial College London/Dissertation/Orginiser.xlsx')
df = excel.parse("name_of_regions")

origin = df['Name of Regions'].values.tolist()
destination = df['Name of Regions'].values.tolist()

gmaps = googlemaps.Client(key="AIzaSyDKs_6N5z4_dzYSafEWIiZRSejQJIGGx7g")

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()
for i in range(len(origin)):
	distances = []
	for j in range(len(destination)):
		distances.append(gmaps.distance_matrix(origin[i], destination[j]))
		dist = distances[j]['rows'][0]['elements'][0]['distance']['text']
		dur = distances[j]['rows'][0]['elements'][0]['duration']['text']
		print(j)
		worksheet.write(j, i, dist)
		#worksheet.write(i, j + 1, dur)
workbook.close()