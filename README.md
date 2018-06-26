This is a repo of different python code and UDFs to be used for data exploration and cleaning that I've done in the past and decided to standarize.

Correlation.py is a UDF for getting a simple DF of all bivariate correlations in a dataset.

String.py outputs a DF with all non numeric columns, how many distinct values are in each column, and how many distinct values there are before you reach 90% of total observations. Can be used to see if there are a few large values and then a long tail of small values or if you want to add many small values to an 'Other' bucket. 

Missing.py is outputs a DF that shows the percentage of obs that are missing in each column.
