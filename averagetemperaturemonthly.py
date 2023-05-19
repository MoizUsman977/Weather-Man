from utils import average_temperature

def get_average_temperature(folder_path, year, month):
    file_path = folder_path + "/" + folder_path + "_" + str(year) +"_"+ month + ".txt"
    try:
        with open(file_path, "r") as file:
            read_content = file.readlines()
            rows = [row.strip().split(',') for row in read_content[1:]]
            data = {
                "max_temperature": [],
                "low_temperature": [],
                "max_humidity": [],
            }    
            for row in rows:
                data["max_temperature"].append(row[1])
                data["low_temperature"].append(row[3])
                data["max_humidity"].append(row[7])
        fomarted_max_temp = [int(value) for value in data["max_temperature"] if value]
        averageMaxTemp = average_temperature(fomarted_max_temp)
        fomarted_min_temp = [int(value) for value in data["low_temperature"] if value]
        averageMinTemp = average_temperature(fomarted_min_temp)
        fomarted_humidity = [int(value) for value in data["max_humidity"] if value]
        averageHumidity = average_temperature(fomarted_humidity)
        print("Highest Average:", str(averageMaxTemp) + "C")    
        print("Lowest Average:", str(averageMinTemp) + "C")    
        print("Average Humidity:", str(averageHumidity) + "%")      
    except FileNotFoundError:
        print("Either File is not available or Path is not correct. \t Press -h for more info")
    