# Functional relationships - review paper

## Introduction
This repository contains the code used for the analyses and some of the figures in the corresponding publication. 
Many other figures are from previously published papers.
The final figures in the paper were created using image processing software.

## Overview
- literature_analysis.py and organize_relationships.py are used for the bibliometric analysis shown in the Supporting Information.
- plot_Darcys_experiment.py replots the results of Darcy's column experiment,
- plot_recharge_karst.py plots precipitation-recharge relationships from different datasets, including karst data by Hartmann et al. (2017),
- plot_recharge_cold_season_P.py plots the Moeck et al. (2020) groundwater recharge data against aridity and colored according to cold season precipitation fraction,
- prepare_global_forcing_data.py prepares data.

## Data sources
Data from Darcy's experiment can be found in Darcy (1856, p. 591ff). 

Groundwater recharge observations from MacDonald et al. (2021) are available from https://www2.bgs.ac.uk/nationalgeosciencedatacentre/citedData/catalogue/45d2b71c-d413-44d4-8b4b-6190527912ff.html. 

Groundwater recharge data from Moeck et al. (2020) are available from https://opendata.eawag.ch/dataset/globalscale_groundwater_moeck. 

Groundwater recharge data can be found in the Supporting Information of Hartmann et al. (2017). 

Cold season and total precipitation from ERA5 are available from https://cds.climate.copernicus.eu/datasets/sis-biodiversity-era5-global. 

Daily averaged ERA5 reanalysis data (e.g., precipitation) are available from https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics.

## References
Darcy (1856). Les fontaines publiques de la ville de Dijon: exposition et application des principes à suivre et des formules à employer dans les questions de distribution d’eau. Victor Dalmont.

Moeck et al. (2020). “A Global-Scale Dataset of Direct Natural Groundwater Recharge Rates: A Review of Variables, Processes and Relationships.” Science of The Total Environment 717 (May):137042. https://doi.org/10.1016/j.scitotenv.2020.137042.

MacDonald et al. (2021). “Mapping Groundwater Recharge in Africa from Ground Observations and Implications for Water Security.” Environmental Research Letters 16 (3): 034012. https://doi.org/10.1088/1748-9326/abd661.

Hartmann et al. (2017). “Enhanced Groundwater Recharge Rates and Altered Recharge Sensitivity to Climate Variability through Subsurface Heterogeneity.” Proceedings of the National Academy of Sciences 114 (11): 2842–47. https://doi.org/10.1073/pnas.1614941114.

Wouters (2021). "Global bioclimatic indicators from 1979 to 2018 derived from reanalysis." Copernicus Climate Change Service (C3S) Climate Data Store (CDS). DOI: 10.24381/cds.bce175f0 

Hersbach et al. (2023). "ERA5 post-processed daily-statistics on pressure levels from 1940 to present." Copernicus Climate Change Service (C3S) Climate Data Store (CDS), DOI: 10.24381/cds.4991cf48 
