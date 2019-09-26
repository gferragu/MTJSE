#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:07:44 2019

@author: gabriel
"""

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

    
