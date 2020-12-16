# Krishna Kumar et al. (2021) - Bacterial Growth Curves Analysis Scripts
---
![GitHub repo size](https://img.shields.io/github/repo-size/tmeiller-legrand/KrishnaKumar_etal_DropletPrinting)
![Github license](https://img.shields.io/github/license/tmeiller-legrand/KrishnaKumar_etal_DropletPrinting)

This repository contains the scripts used to analyse the data for the bacterial growth kinetics in the paper: "Droplet printing reveals the importance of micron-scale structure for bacterial ecology", Krishna Kumar et al. (2020-2021)
DOI:  https://doi.org/10.1101/2020.10.20.346577

### What it does
---
There are 2 scripts:
- GrowthCurvePlotter_2xtimeCalculator.py used to plot growth curves and calculate doubling times
- LagPhase-DMFit_TableFormatting.py used to reformat the plate reader data for them to be processed by the Excel add-on DMFit 3.5 (https://www.combase.cc/index.php/en/8-category-engb/21-tools, last accessed 16/12/2020). 

N.B: These scripts were designed to work on outputs from the BMG Labteh plate reader as created using the Mars data analysis software in table format. However, these should (hopefully) be easily adapted to work with outputs from other plate readers if needed.

N.B.2: They were also designed for randomised plate runs. However this should also work on non-randomised plate reads (non-tested yet).

### What you will need
---
python 3.7

### What this contains
---
This repo contains 3 folders:
- Methods: contains the analysis scripts.
- RawData: contains the raw data files as exported from the Mars data analysis software and used in the paper.
- Results: contains the outputs of the scripts in Methods applied to the data contained in the RawData folder.

### How does it work?
---
##### GrowthCurvePlotter_2xtimeCalculator.py
The script is organised like such:
- Sorting the data (we randomised the samples on the plate so they need to sorted) and calculating the mean of the technical replicates for each biological replicate).
- Calculating the mean growth curve based on three biological replicates (optional)
- Plotting the data and outputting the graph
- Calculating the doubling time using a linear fit for the OD values between 0.2 and 0.7 and outputting the results in an Excel file.

##### LagPhase-DMFit_TableFormatting.py
The script is organised like such:
- Sorting the data (we randomised the samples on the plate so they need to sorted) and calculating the mean of the technical replicates for each biological replicate).
- Reformatting the the data to the format specified by the DMFit 3.5 software.

### References
---
1. Krishna Kumar et al., "Droplet printing reveals the importance of micron-scale structure for bacterial ecology", bioRxiv (2020-2021) https://doi.org/10.1101/2020.10.20.346577
2. Baranyi, J. & Roberts, T. A., "A dynamic approach to predicting bacterial growth in food." Int. J. Food Microbiol. 23, 277–294 (1994). https://doi.org/10.1016/0168-1605(94)90157-0

### License
----
MIT
