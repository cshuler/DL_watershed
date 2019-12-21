import cj_function_lib as cj
import init_file as variables

septwq = """ !!Variablesinorder:  idspttype (Septic type (1-conventional,2-advanced,3-failing)
      Q,BOD,TSS,TN,NH4,N03,NO2,OrgN,TP,Po4,
    Org P,F.Coli
           1         2         3         4         5         6         7         8
  1 COND Conventional Drainfield                                                 1
       0.227 170.000  75.000  60.000  58.000   0.200   0.000  14.000  10.000   9.000
       1.000 10000000.0
  2 SAS1 Septic w/SAS                                                            2
       0.227 170.000  75.000  70.000  60.000   0.000   0.000  10.000  10.000   8.500
       1.500 10000000.0
  3 SAS2 Septic w/SAS                                                            2
       0.227 170.000  75.000  70.000   0.000   0.000   0.000   0.000  10.000   9.000
       1.000 10000000.0
  4 SAS3 Septic w/in-tank N removal and SAS                                      2
       0.227 170.000  80.000  20.000   0.000  20.000   0.000   0.000  10.000   8.500
       1.500  1000000.0
  5 SAS4 Septic tank w/effluent N removal and recycle                            2
       0.227 100.000  65.000  20.000   0.000   0.000   0.000  10.000   0.000   8.500
       1.500 10000000.0
  6 SAS5 Septic w/corrugated plastic trickling filter                            2
       0.227  20.000  10.000   7.700   2.400   7.100   0.000   0.000   0.000   0.000
       0.000        0.0
  7 SAS6 Septic w/single pass sand filter                                        2
       0.227  18.000  17.000  11.000   5.600   4.100   0.000   1.300   0.000   0.000
       0.000        0.0
  8 SPF1 Single pass sand filter                                                 2
       0.227   3.500   2.000  38.000   0.000   0.000   0.000   0.000   0.000   0.000
       0.000      360.0
  9 SPF2 Single pass sand filter                                                 2
       0.227   3.200   9.000  30.000   0.000   0.000   0.000   0.000   0.000   0.000
       0.000      407.0
 10 SPF3 Single pass sand filter                                                 2
       0.227   4.000  17.000  37.500   0.000   0.000   0.000  14.100  12.000  12.000
       2.100      862.0
 11 SPF4 Single pass sand filter                                                 2
       0.227  75.100  29.100  15.500  10.600   0.300   0.000   4.600   0.000   0.000
       0.000        0.0
 12 RCF1 At grade recirculating sand filter                                      2
       0.227   3.500   3.500  13.500   0.000   0.000   0.000   0.000   0.000   0.000
       0.000     2920.0
 13 RCF2 Maryland style RSF                                                      2
       0.227   5.000   6.500  30.500   0.000   0.000   0.000   0.000   0.000   0.000
       0.000     3030.0
 14 RCF3 Recirulating sand filter                                                2
       0.227  11.500  13.500  26.500   5.500  29.000   0.000   0.000   0.000   0.000
       0.900    57000.0
 15 CWT1 Septic tank w/constructed wetland and surface water discharge           2
       0.227  26.500  12.000  38.000   0.000   0.000   0.000   0.000   0.750   0.000
       0.110      968.0
 16 CWT2 Municipal wastewater w/constructed wetland and surface water discharge  2
       0.227  27.000  15.000   0.000   0.000   0.000   0.000   0.000   0.000   0.000
       0.000        0.0
 17 CWT3 Municipal wastewater w/constructed wetland and surface water discharge  2
       0.227   0.000   4.200   0.000   0.860   0.000   0.000   0.000   0.240   0.000
       0.040       77.0
 18 CWT4 Municipal wastewater w/constructed wetland                              2
       0.227   7.500  14.000   0.000   3.290   0.000   0.000   0.000   0.000   0.000
       0.000        0.0
 19 CWT5 Municipal wastewater w/lagoon and constructed wetland                   2
       0.227   1.700   9.500   0.000   1.980   0.000   0.000   0.000   0.000   0.000
       0.000        0.0
 20 BFL1 Waterloo biofilter (plastic media)                                      2
       0.227  28.500  18.500  58.000   0.000   0.000   0.000   0.000   0.000   0.000
       0.000        0.0
 21 BFL2 Waterloo biofilter (plastic media)                                      2
       0.227  16.000   5.000   0.000  10.200   5.700   0.000   0.000   0.000   0.000
       0.000   190000.0
 22 BFL3 Peat biofilter                                                          2
       0.227   4.500   6.500   2.500   1.000  20.000   0.000   0.000   0.000   0.000
       0.450      945.0
 23 TXF1 Recirulating textile filter                                             2
       0.227  27.500  16.000  26.500   0.000   0.000   0.000   0.000   0.000   0.000
       0.000    50790.0
 24 TXF2 Foam or textile filter effluent                                         2
       0.227  10.000   7.500  45.000   0.000   0.000   0.000   0.000   0.000   0.000
       0.000      505.0
 25 GFL1 Septic, recirculating gravel filter, UV disinfection                    2
       0.227  25.000   4.900   0.400   0.000  12.200   0.000   0.000   0.000   0.000
       0.000        7.3
 26 FSPT Texas A&M reference                                                     3
       0.227 250.000 700.000  40.000  25.000   0.000   0.000  25.000  12.000  10.000
       2.000 10000000.0
"""

fileName = "septwq.dat"
cj.write_to(variables.DefaultSimDir + "TxtInOut\\" + fileName, septwq)
#print fileName