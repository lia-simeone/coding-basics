#####Overall pandas info
* to follow convention, use the following code
    # Much of pandas is built on NumPy so you should always import them togther
    import numpy as np
    import pandas as pd
    # In the book they explicitly call the DataFrame and Series objects since they are used a lot (saves the prefix)
    from pandas import DataFrame, Series
* Like python, the first element in an index call is inclusive while the latter is exclusive
    #Get rows 2, 3, and 4 which are indexed 1, 2, and 3
    temps_df.Difference[1:4]
    
####Series object
* Base data struture of pandas
* Similar to NumPy array but adds indexing capabilities
    # Input
    # create a four item DataFrame
    s = Series([1, 2, 3, 4])
    s
    # Output
    0    1
    1    2
    2    3
    3    4
* We did not specific an index so pandas defaults to zero
* In pandas indexes are called labels
* Elements can be retrieved by using the labels with []
    #Input
    s[[1, 3]]
    #Output
    1    2
    3    4
* If you choose non-default labels, you will retrieve elements using those labels
    # Input
    # create a series using an explicit index
    s = Series([1, 2, 3, 4], 
        index = ['a', 'b', 'c', 'd'])
    s
    # Output
    a    1
    b    2
    c    3
    d    4
* `.index` is a pandas object that will show you the index values for the series
* Why does this create a series with the index as dates? It seems like it should create a series with the dates as the values and the default zero index
    dates = pd.date_range('2014-07-01', '2014-07-06')
* It looks like they create an actual series in the next step
    temps1 = Series([80, 82, 85, 90, 83, 87], 
                   index = dates)
* Typical NumPy mthods (like mean) and arthmetic can be applied to series

####DataFrame object
* More than one Series that is aligned by a common index (basically a dataset)
    temps_df = DataFrame({'Missoula': temps1, 'Philadelphia': temps2})
* Columns in a df can be accessed using an array indexer
    temps_def['Missoula']
* If the column name doesn't have any spaces, you can access it through a property-style index
    temps_df.Missoula #Super handy!
* You can add a column by assigning another Series to the column using an array indexer
    temps_df['Difference'] = temp_diffs
* Rows can be retrieved by using `.loc` and `.iloc`
* `.iloc` is integer position based (0 to length-1)
    #Grab the second row
    temps_df.iloc[1]
* The resulting row is a Series with the column names of the DataFrame pivoted into the index labels of the Series
    # Input
    # the names of the columns have become the index
    # they have been 'pivoted'
    # QUESTION - what does the 'ix' mean?
    temps_df.ix[1].index
    # Output
    Index([u'Missoula', u'Philadelphia', u'Difference'], dtype='object')
* `.loc` is label based
    #QUESTION - `.loc` just grabs the row, right? It doesn't create a series like `.iloc`?
    temps_df.loc['2014-07-03']
    #temps_df.loc[1] does not work because I specified dates for the labels
* You can grab specific rows from within a column
    #QUESTION  - why do we need double brackets?
    temps_df.iloc[[1,3,4]].Difference
* You can use a logical expression to filter the data as well
    # Input
    temps_df.Missoula > 82
    # Output
    2014-07-01    False
    2014-07-02    False
    2014-07-03     True
    2014-07-04     True
    2014-07-05     True
    2014-07-06     True
* This logic can be used in the [] operator of a df, so only the TRUE rows are returned (R course problem)
    temps_df[temps_df.Missoula>82]
    
#FINISHED CHAPTER 1