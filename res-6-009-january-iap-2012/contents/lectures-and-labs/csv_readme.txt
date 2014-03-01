This data is from:
http://www.countyhealthrankings.org/ranking-methods/exploring-data
http://opengovdata.pbworks.com/w/page/27141180/County%20Health%20Rankings


To get the data into the useful csv files (additional_measures_cleaned.csv and ypll.csv), I:
- save each of the sheets of 2011 County Health Rankings.xls to a .csv file
- delete the top row in each, since it's a metaheader
- reference http://www.countyhealthrankings.org/sites/default/files/CHR%202011%20Data%20Comparability%20Across%20States.pdf to determine the measures that apply across states
- realize that z-scores and rankings are within a state, so I can't use any of those metrics to compare counties in different states
- look for ratings (per 100k people) or comparable metrics (population, percent children eligible for free lunch) that apply across states
- identify YPLL (years of preventable life loss) as a good candidate for the dependent variable
- delete all columns that don't apply to the regression from additional_measures_cleaned.csv / ypll.csv
- only consider rows where none of the values are 0, and Unreliable is not checked.
- use ols.py from https://www.scipy.org/Cookbook/OLS