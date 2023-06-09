from averagetemperaturemonthly import get_average_temperature
from barcharts import bar_chart
from datetime import datetime
from horizontalbarcharts import horizontal_bar_chart
from maxtemperatureyearly import get_highest_temperature
import argparse

parser = argparse.ArgumentParser(description='Weather Man')
parser.add_argument('folder_path', help='Path to the folder containing weather data files')
parser.add_argument('-e', dest='year', type=int, help='Year for highest, lowest, and most humid day')
parser.add_argument('-a', dest='year_month', help='Year and month for average temperature and humidity')
parser.add_argument('-c', dest='bar_chart', help='Year and month for bar chart')
parser.add_argument('-v', dest='bar_chart_in_line', help='Year and month for bar chart for in line representation')
args = parser.parse_args()


if args.year:
    year = args.year
if args.year_month:
    year =  args.year_month
if args.bar_chart:
    year = args.bar_chart
if args.bar_chart_in_line:
    year = args.bar_chart_in_line
try:
    if not args.year :
        date_obj = datetime.strptime(year, "%Y/%m")
        month_name = date_obj.strftime("%b")
        year = date_obj.year
except:
    print("Format of Date Should be yyyy/mm or yyyy")
else:
    if args.year and len(str(args.year)) == 4:
        get_highest_temperature(args.folder_path, args.year)
    if args.year_month: 
        get_average_temperature(args.folder_path, year, month_name)
    if args.bar_chart: 
        bar_chart(args.folder_path, year, month_name)
    if args.bar_chart_in_line: 
        horizontal_bar_chart(args.folder_path, year, month_name)