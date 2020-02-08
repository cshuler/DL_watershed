"""------------------QSWAT Workflow v1.5.8 Settings File---------------"""

# Project Identification
Project_Name     = "Fagaitua_2"
Model_2_namelist = False        # True = get settings from existing model 
                                # False = get model from current settings

"""---------------------------   File Names  --------------------------"""
# Raster files (Should be projected with the same projection)
Topography         = "DEM_clipped_12.tif"
Soils              = "soil_clipped_12.tif"
Land_Use           = "LU_clipped_12.tif"


# LookUp Files
soil_lookup        = "brokensoil2.csv"
landuse_lookup     = "landuse_lookup.csv"

# Database table files
Usersoil           = "usersoil_mod.csv"
WGEN_user          = "WGEN_user_theirs.csv"    # note this is just their file not sure about it

# Shape Files
Outlet             = "Fagaitua.shp" # it should have same format as in the example

# Weather stationinformation files
Precipitation      = "1_Pcp_loc.txt"
Temperature        = "2_Tmp_loc.txt"
Rel_Humidity       = "3_HMD_loc.txt"
Solar_Radiation    = "5_SLR_loc.txt"
Wind               = "4_WND_loc.txt"


"""---------------------------  Project Options  ----------------------"""
# Watershed Deliniation (1 = Cells)
WS_thresholds_type    = 1            
WS_threshold          = 998
OUT_Snap_threshold    = 300                # metres 
Burn_in_shape         = ""                 # leave as "" if none


#  -------------------  HRU Definition  ------------------
Slope_classes         = "0, 1, 3, 9999"

# HRU creation method   (1 = Dominant landuse, soil, slope , 2 = Dominant HRU,
#                        3 = Filter by Area,                 4 = Target Number of HRUs,
#                        5 = Filter by landuse, soil, slope)

HRU_creation_method   = 5

# Thresholds           (1 = Total Area , 2 = Percent)
HRU_thresholds_type   = 2

HRU_thres_LandUse     = 0             # Only used if HRU_creation_method 5 is selected
HRU_thres_Soil        = 0             #        can be set to "" if 5 is not selected
HRU_thres_Slope       = 0

Target_Value          = None           # used if HRU_creation_method 3 and 4 are selected


# Routing and ET and infiltration
ET_method             = 2           # 1 = Priestley-Taylor, 2 = Penman-Monteith,   3 = Hargreaves,        (4 = Observed - Not supported Currently)
Routing_method        = 2           # 1 = Muskingum,        2 = Variable Storage
Routing_timestep      = 1           # 1 = Daily,            2 = Hourly
Rainfall_timestep     = 1           # 1 = Daily,            2 = Sub-hourly timestep (works with Green & Ampt infiltration)
Run_off_method        = 1           # 1 = SCS Curve Number, 2 = Green & Ampt


# model run settings
Model_Run_period      = "2005 - 2017"# e.g. "1975 - 1980". period to run the simulation from file.cio,
                                     # leave as "" to run whole period where weather data is available
Warm_up_period        = 8            # the number of years for running the model without printing output
timestep              = 0            # timestep for printing results: 0 = monthly, 1 = daily 3 = yearly

cal_file              = ""           # a model.in file (format of swatcup) with parameters for the calibrated model
                                     # leave as "" if there is no file to be used.
calibrate              = False       # set to "True" to perform calibration, "False" to skip calibration
make_figures           = True        # set to "True" to create maps, "False" to skip map creation

# Log progress or not? If yes, you will not see updates
log                   = False        # True or False
"""---------------------------  Settings End  -----------------------"""
