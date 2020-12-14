#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:38:37 2019

@author: user

This is a script to read multiple plate reader outputs and plot the growth curves of allthe samples
"""

import csv

bio_replicates = input("How many biological replicates do you have?\n")

all_data = [None] * bio_replicates

for i in bio_replicates:
    with open() as csvfile:
        all_data[i] = csv.reader(csvfile, delimiter=',')