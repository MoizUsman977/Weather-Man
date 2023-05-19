def average_temperature (lst) : 
        return sum(lst) // len(lst)

def get_min_max_temperature(folder_path, year, month):
        file_path = folder_path + "/" + folder_path + "_" + str(year) +"_"+ month + ".txt"
        with open(file_path, "r") as file:
                read_content = file.readlines()
                rows = [row.strip().split(',') for row in read_content[1:]]
                temp_data = []   
                for row in rows:
                        if row[1] and row[3]:
                                max_temp = row[1]
                                min_temp = row[3]
                                temp_data.append({"max_temp": int(max_temp), "min_temp": int(min_temp)})

        return temp_data