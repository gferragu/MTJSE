#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Gabriel
"""
#%% Import necessary packages

from obspy import read
from obspy import Stream
from obspy.io.segy.core import _read_segy
from obspy.core.utcdatetime import UTCDateTime
from obspy.geodetics import locations2degrees

#%%

##          Script to read MENII SEGY files and extract metadata             ##
##                        Gabriel Ferragut                                   ##

