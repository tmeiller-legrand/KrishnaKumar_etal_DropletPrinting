#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:29:03 2020

@author: Thomas Meiller-Legrand

Script used to create the formatted table for lag phase calculation by DMFit

DMFit requires data to be formatted in a specific way to be analysed by the
Excel add-in DMFit. In brief, the excel file needs to have two spreadsheets:
    - one named Logc, containing the data to be analyized. This spreadsheet
    should have three columns:
        + logc: contains the label of the strains for each data point
        + Time: contains the time points
        + 0: contains the OD values
    - another named index0 containing only one column titled logc and listing
    all the strains used.

For more information, please refer to the DMFit user manual included in the
package. DMFit can be found at:
    https://www.combase.cc/index.php/en/8-category-en-gb/21-tools
(accessed April 21st 2020)
"""

from pathlib import Path

import pandas as pd
import numpy as np


def Technical_replicate_mean(FileName):
    # This function is used to calculate the mean OD values of the technical
    # replicates.

    df = pd.read_excel(FileName, sheet_name="All Cycles")  # Opens the raw data
    # file
    df2 = df[10:75]  # Removes the metadata included at the top of the
    # spreadsheet containing the data.
    df3 = df2.sort_values('Unnamed: 3')  # This sorts the data (if using a
    # randomised plate) so that the technical replicates values are in
    # neighbouring cells.
    df4 = df3.loc[:, 'Unnamed: 292':]  # This removes the columns containing
    # the names of the wells and the label of the strains.

    replicate_means = []

    # Here we're going through the table and calculating the mean.
    for i in range(0, (len(df4)-5), 3):
        temp_df = df4.iloc[[i, i+1, i+2]]  # Storing the 3 time series
        # containing the OD values for one strain.
        temp_mean = temp_df.mean(axis=0)  # Calculating the mean of the OD
        # values for every time point.
        replicate_means.append(temp_mean)  # Appends the time series of the
        # mean OD value to a list storing the mean time series for each strain.

    # I have 4 wells containing water so I calculate the mean OD separately for
    # these. This can be skipped in general.
    temp_df = df4.iloc[[60, 61, 62, 63]]
    temp_mean = temp_df.mean(axis=0)
    replicate_means.append(temp_mean)

    return(replicate_means)  # Returns the list containing the averaged time
    # series of OD values


# Calculating the average of the technical replicates for each biological
# replicate
br1 = Technical_replicate_mean("2019-10-11-TML_StrainRav_GrowthCurves-1.xlsx")
br2 = Technical_replicate_mean("2019-10-18-TML_StrainsRav_GrowthCurves-2.xlsx")
br3 = Technical_replicate_mean("2019-10-24-TML_StrainsRav_GrowthCurves-3.xlsx")

# If one wants to do the anlysis on the average of the biological replicates,
# this calculates it.
mean_biorep = []
for j in range(21):
    temp_concatenated_data = pd.concat((br1[j], br2[j], br3[j]), axis=1)
    mean_biorep.append(temp_concatenated_data.mean(axis=1))


def reformatingData(dataSet):
    # This function reformats the data from being organised as one row per
    # strain and a time value per column to the layout explained at the top
    # of the script.

    # This renames all the keys in the time series to the strain label.
    dataSet[0] = dataSet[0].rename(lambda x: 'WT')
    dataSet[1] = dataSet[1].rename(lambda x: 'WT GFP')
    dataSet[2] = dataSet[2].rename(lambda x: 'WT RFP')
    dataSet[3] = dataSet[3].rename(lambda x: 'E2')
    dataSet[4] = dataSet[4].rename(lambda x: 'E2 GFP')
    dataSet[5] = dataSet[5].rename(lambda x: 'E2 RFP')
    dataSet[6] = dataSet[6].rename(lambda x: 'E7')
    dataSet[7] = dataSet[7].rename(lambda x: 'E7 RFP')
    dataSet[8] = dataSet[8].rename(lambda x: 'E8')
    dataSet[9] = dataSet[9].rename(lambda x: 'E8 RFP')
    dataSet[10] = dataSet[10].rename(lambda x: 'A')
    dataSet[11] = dataSet[11].rename(lambda x: 'A GFP')
    dataSet[12] = dataSet[12].rename(lambda x: 'A RFP')
    dataSet[13] = dataSet[13].rename(lambda x: 'btuB')
    dataSet[14] = dataSet[14].rename(lambda x: 'btuB GFP')
    dataSet[15] = dataSet[15].rename(lambda x: 'btuB RFP')
    dataSet[16] = dataSet[16].rename(lambda x: 'pC001')
    dataSet[17] = dataSet[17].rename(lambda x: 'ImmE2 Ypet')
    dataSet[18] = dataSet[18].rename(lambda x: 'ImmE2 NeonGreen')

    time = np.arange(0, 1440, 5).tolist()  # Creates a vector with the time
    # points

    # Converts the time series to dataframes and inserts/adds the time vector
    # to the data.
    for j in range(21):
        dataSet[j] = dataSet[j].to_frame()
        dataSet[j].insert(0, 'Time', time, True)

    data = dataSet[0]

    for k in range(18):
        data = pd.concat([data, dataSet[k+1]])

    data.rename(columns={0: 'logc'})

    return(data)


# Here each biological replicates is reformatted using the function
# reformattingData above
data_br1 = reformatingData(br1)
data_br2 = reformatingData(br2)
data_br3 = reformatingData(br3)
# Reformatting the data the same way for the mean of the biological repliactes
data_mean = reformatingData(mean_biorep)

index0 = pd.DataFrame(['WT',
                       'WT GFP',
                       'WT RFP',
                       'E2',
                       'E2 GFP',
                       'E2 RFP',
                       'E7',
                       'E7 RFP',
                       'E8',
                       'E8 RFP',
                       'A',
                       'A GFP',
                       'A RFP',
                       'btuB',
                       'btuB GFP',
                       'btuB RFP',
                       'pC001',
                       'ImmE2 Ypet',
                       'ImmE2 NeonGreen'],
                      columns=['logc'])

# The following section saves the reformatted data to an excel file with the
# various sheets DMFit requires.
folder_path = Path('<Path to where the excel file should be saved+name.xlsx>')
# Example, in my case:
# folder_path = Path('/Users/user/Documents/DPhil_Projects/Droplet-printing/\
#                   Methods/StrainGrowthCurves/Analysis/LagPhase/\
#                   2020-02-01-TML_LagPhase_data-br3.xlsx')

writer = pd.ExcelWriter(folder_path, engine='xlsxwriter')
# data_br1.to_excel(writer, sheet_name='Logc', index_label='logc')
# data_br2.to_excel(writer, sheet_name='Logc', index_label='logc')
data_br3.to_excel(writer, sheet_name='Logc', index_label='logc')
# data_mean.to_excel(writer, sheet_name='Logc', index_label='logc')
index0.to_excel(writer, sheet_name='Index0', index=False)
writer.save()
writer.close()
