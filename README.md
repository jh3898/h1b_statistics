# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run](README.md#instructions)

# Problem

1. To create a mechanism to analyze data and calculate the "Top 10 Occupations" and "Top 10 states" for "certified" visa appliations, and sort the occupation/states alphabetically
2. Calculate the percentage of certified application for the first 10 different occupations/ different states over the total certified application. 
3. Read data from  `input` directory, running the `run.sh` script should produce the results in the `output` folder.

# Approach
1. search columns indexes for current occupation/worksite_state, each requires two keys words. For example, the occupation name column should have keys: 'SOC' and 'NAME'.
2. read input data line by line, use a dictionary, if the line has the 'certified' word, then add 1 to the current occupation/worksite_state, also add 1 to the total number of 'certified' appearances.
2. sort the dictionary value (number of person for each occupation/state) in decending order and the the occupation name/ state name in ascending order, choose the first 10 elements
3. calculate the percentage of each occupation/state by dividing the each occupation/state number over the total number 
4. output two txt files in the output folder


# Run 

run run.sh file, no extra work needed.
