#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:07:44 2019

@author: gabriel
"""

import pandas as pd

#%% Define functions for metadata module

def getTraceHeaderKeys(experiment,stream,index):
    
    if experiment == "MENII":
        
        header_dict = stream[index].stats.segy.trace_header
        header_keys = list(header_dict.keys())
        return header_keys
        
        
    else:
        print("Only functionanl for the MENII survey presently")


def getTraceHeaderValues(experiment, stream, index, keys):
            
    if experiment == "MENII":
        
        header_dict = stream[index].stats.segy.trace_header
        header_values=[header_dict.get(x) for x in keys]
        return header_values
        
        
    else:
        print("Only functionanl for the MENII survey presently")

    
def headerToCSV(experiment, stream, index, keys):
    
    tmp_keys = getTraceHeaderKeys("MENII",stream,index)
    trace_header = pd.DataFrame(columns=tmp_keys)
    
    for idx,tr in enumerate(stream):
        tmp_keys = getTraceHeaderKeys("MENII",stream,idx)
        tmp_values = getTraceHeaderValues("MENII",stream,idx,tmp_keys)
        trace_header.loc[idx]=tmp_values
        
        print('\n' + "Working on trace " + str(idx) + " out of " + str(len(stream)))