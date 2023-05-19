from colorama import Fore
from utils import get_min_max_temperature

def bar_chart(folder_path, year, month):
    try:
        temp_data = get_min_max_temperature(folder_path, year, month)
        for value in temp_data:
            for _ in range(value["max_temp"]):
                print(Fore.RED + "+", end="")
            print(Fore.WHITE + str(value["max_temp"]) + "C")    
            for _ in range(value["min_temp"]):
                print(Fore.BLUE + "-", end="")
            print(Fore.WHITE + str(value["min_temp"]) + "C")    
            print("\t")  
    except FileNotFoundError :
        print("Either File is not available or Path is not correct. \t Press -h for more info")    














