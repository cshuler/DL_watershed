"""
This Module creates wnd file
"""
import cj_function_lib as cj
import mdbtools as mdb
import init_file as variables
from datetime import datetime
import calendar, os

class station:
    def __init__(self, wnd_line):
        self.name = wnd_line.split(",")[1]
        self.elev = wnd_line.split(",")[4]
        self.lon = wnd_line.split(",")[3]
        self.lat = wnd_line.split(",")[2]
        self.data_list = self.get_data()

    def get_data(self):
        self.data = cj.read_from(variables.WeatherDIR + self.name + ".txt")
        return  self.data


stations_dict = {}
stations_list = []
station_nr = []

if not os.path.isfile(variables.wnd_file_txt):
    pass
else:
    used_stations = cj.extract_table_from_mdb(variables.ProjMDB, "SubWnd", variables.path + "\\subwnd.tmp~")
    all_stations = cj.extract_table_from_mdb(variables.ProjMDB, "wnd", variables.path + "\\wnd.tmp~")

    count = 0
    for station_line in used_stations:
        if not station_line.split(",")[4] in stations_list:
            for wnd_file_line in all_stations:
                if station_line.split(",")[4] == wnd_file_line.split(",")[1]:
                    count += 1
                    stations_list.append(station_line.split(",")[4])
                    station_nr.append(count)
                    stations_dict[str(count)] = station(wnd_file_line)

    # Header creation
    now = datetime.now()

    DateAndTime = str(now.month) + "/" + str(now.day) + "/" + \
        str(now.year) + " " + str(now.time()).split(".")[0]
    SWAT_Vers = "QSWAT Workflow v1.5.2"


    wnd_string = "Input File wnd.wnd          " + DateAndTime + " " + SWAT_Vers + "\n"

    current_tear = int(stations_dict["1"].data_list[0][0:4])
    end_day = cj.get_days_in_year(current_tear)
    current_day = 0

    for i in range(1, len(stations_dict["1"].data_list)):
        line = ""
        current_day += 1

        if current_day <= end_day:
            datecode = str(current_tear) + cj.trailing_zeros(3, current_day, 0)
            #print datecode
        else:
            current_day = 1
            current_tear += 1
            end_day = cj.get_days_in_year(current_tear)
            datecode = str(current_tear) + cj.trailing_zeros(3, current_day, 0)
            #print end_day

        for sta_nr in station_nr:
            rec = cj.trailing_zeros(8, stations_dict[str(sta_nr)].data_list[i], 3)
            line += rec

        line = datecode + line + "\n"
        wnd_string += line

    cj.write_to(variables.DefaultSimDir + "TxtInOut\\wnd.wnd", wnd_string)
