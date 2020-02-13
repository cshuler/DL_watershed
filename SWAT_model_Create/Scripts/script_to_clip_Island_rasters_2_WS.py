# This script simply splits the island wide rasters into major watershed sections for smaller file storage. 

import arcpy 

arcpy.env.overwriteOutput = True

# make individual soil rasters
for i in (range(0,33)):
    arcpy.Select_analysis("H:/watersheds.shp", "H:/workspace/tempselect.shp", '"FID" = {}'.format(i))
    arcpy.Clip_management("H:/soil_4.tif", "#", "H:/workspace/soil_clipped_{}.tif".format(i), "H:/workspace/tempselect.shp", "1", "ClippingGeometry")
	
# make individual land use rasters
for i in (range(0,33)):
    arcpy.Select_analysis("H:/watersheds.shp", "H:/workspace/tempselect.shp", '"FID" = {}'.format(i))
    arcpy.Clip_management("H:/lu_4.tif", "#", "H:/workspace/LU_clipped_{}.tif".format(i), "H:/workspace/tempselect.shp", "1", "ClippingGeometry")
	
# make individual DEM rasters
for i in (range(0,33)):
    arcpy.Select_analysis("H:/watersheds.shp", "H:/workspace/tempselect.shp", '"FID" = {}'.format(i))
    arcpy.Clip_management("H:/DEM_prj.tif", "#", "H:/workspace/DEM_clipped_{}.tif".format(i), "H:/workspace/tempselect.shp", "1", "ClippingGeometry")
	
	
	# Note that only WS #s [6, 11, 12, 16, 18, 23, 24, 27] have ASPA-UH gauges   
	# # 6 is afono