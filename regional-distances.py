#using this code to automatically find the distances in km from all regions to all regions and the store them in an excel sheet using the direction API from google used
import googlemaps
import pandas as pd
import xlsxwriter

#creating the dataframe to read from my excel sheet 'name_of_regions'
excel = pd.ExcelFile(r'C:/Users/georg/Documents/Transport and Business Management - Imperial College London/Dissertation/Orginiser.xlsx')
df = excel.parse("name_of_regions")

#converted the values to a list instead of a table
origin = df['Name of Regions'].values.tolist()
destination = df['Name of Regions'].values.tolist()

gmaps = googlemaps.Client(key="AIzaSyDKs_6N5z4_dzYSafEWIiZRSejQJIGGx7g")

#created an excel file name 'test' and stored there the output
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
workbook.close()
