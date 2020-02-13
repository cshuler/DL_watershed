# Using Deep Learning to Test the Boundaries of Physically Based and Phenominoligical Watershed Models 
 #### Using machine learning to break the boundaries of physically based watershed models

Note this project is totally in progress and everything here is super preliminary!

### Premise 
Watershed models, such as the Soil & Water Assessment Tool (SWAT) are industry standard tools for providing quantitative estimates of water, nutrient, and sediment outflows in streams, assessing impacts to watersheds from environmental changes, and estimating components of the water budget, such as surface runoff and baseflow discharge. Traditional watershed models are physically-based models, meaning they are founded upon the mathematical equations that we have developed to understand natural processes around us. However, natural systems are inherently complicated, and if our conceptual models are over-simplified, physically-based models may yield less than satisfactory results; often producing the right answers, but for the wrong reasons. Conversely, deep neural networks, a form of machine learning, have recently become a popular way to solve problems where the exact mathematical relationships between inputs and outputs have not been constrained by our presuppositions of the world. Neural networks have been widely applied to develop tools and empirical models of everything from optimizing groundwater management to predicting the stock market. In this study, we test the hypothesis that a neural network, provided with the same input information as provided to a physically based watershed model, can yield predictions of output parameters with a higher degree of certainty than can be produced by, specifically a SWAT watershed model. Preliminary results indicate that deep learning technology is promising and if provided with enough input data, can produce meaningful results. This frontier in computing has significant potential to supplement the water manager’s existing toolkit, and someday could even replace physically based models, though we are likely a ways off. 




## 1. SWAT Model Component 

### Preliminary SWAT Model Results
<p align="center">
   Total Water Yield at subbasin scale
</p>           

Fagaalu Watershed            |  Afono Watershed
:-------------------------:|:-------------------------:
![](/SWAT_model_Create/Fagaalu/model/Fagaalu/Figures/WYLD_2013.png)  |  ![](/SWAT_model_Create/Afono/model/Afono/Figures/WYLD_2013.png)

Nuuuli Watershed            |  Maloata Watershed
:-------------------------:|:-------------------------:
![](/SWAT_model_Create/Nuuuli/model/Nuuuli/Figures/WYLD_2013.png)  |  ![](/SWAT_model_Create/Maloata/model/Maloata/Figures/WYLD_2013.png)

Fagasa Watershed            |  Vaipito Watershed
:-------------------------:|:-------------------------:
![](/SWAT_model_Create/Fagasa/model/Fagasa/Figures/WYLD_2013.png)  |  ![](/SWAT_model_Create/Vaipito/model/Vaipito/Figures/WYLD_2013.png)


Leone Watershed            |  Fagasa Watershed
:-------------------------:|:-------------------------:
![](/SWAT_model_Create/Leone/model/Leone/Figures/WYLD_2013.png)  |  ![](/SWAT_model_Create/Fagasa/model/Fagasa/Figures/WYLD_2013.png)


### Daily hydrographs from all watersheds stacked into one plot. 
Note that currently the same weather database is provided to each of the models. Differences arise based only on the different topographic, land use, and soil characteristics of each watershed. Future calibration scripts will ultimately change this regularity. 



<p align="center">
  <img width="900" height="400" src=/Figures/SWAT_model/SWAT_flow_ALL.jpg >
</p>

### Close up of above graph to see differences between each watershed 
<p align="center">
  <img width="900" height="400" src=/Figures/SWAT_model/SWAT_flow_ALL_Closeup.jpg >
</p>

Note, we need to give a huge shout out to Celray James CHAWANDA, and Chris GEORGE for sharing the QSWAT_Automated_Workflow v1.5.8!
See: https://github.com/VUB-HYDR/QSWAT_Automated_Workflow
