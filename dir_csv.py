#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
from os import walk
from functools import reduce
from datetime import datetime

# things to add / alter:
    # add column indicating from what csv the rows came from before collate!!
    # change class name to something more general for csv utility functions
    # create a function saves list of dict to csv
        # parameters:
            # specify path name
            # specify alternate column names
    # use walklevel to be able to limit collate csvs per directory level
    # create a method that will retrieve the latest summaries from each directory (within root) then compiles them
        # prompt user if to continue if columns mismatch; show mismatch columns
    # create a method that will join latest summaries in the same subdirec (but different levels) on target column
    # create a method that automatically loads the latest csv in a given directory
    
    # possible parameters: 
        # option to save on different path

class dir_csv():
    
    def __init__(self, direc_path):
        '''Initialize directory to summarize and set file name.
        
        File name: summary with suffix date time.
        
        Parameters:
            direc_path: directory path(s) to summarize.
        '''

        self.dir = direc_path
        now = datetime.now()
        self.date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    def csv_collate(self, fname='Summary'):
        '''Collates all the csv files in the given directory.
        
        Adds the column from where the row data csv came from.
        
        Parameters:
        -----------
            fname: string
                Filename to use for the summary
        '''
        
        list_df = []
        for root, path, files in walk(self.dir):
            for file in files:
                df_tmp = pd.read_csv(root+r'/'+file)
                df_tmp['csv_file'] = [file]*df_tmp.shape[0]
                list_df.append(df_tmp)
        df = reduce(lambda x, y: x.append(y), list_df)
        df = df.drop_duplicates()
        print(fr'Summary File: {self.dir}/{fname}-{self.date_time}.csv')
        df.to_csv(fr'{self.dir}/{fname}-{self.date_time}.csv', index=False)

