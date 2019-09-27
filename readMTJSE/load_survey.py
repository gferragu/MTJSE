# -*- coding: utf-8 -*-

import glob

##                     Loading survey data files                             ##
##                        Gabriel Ferragut                                   ##
##                         Sept 25th 2019                                    ## 

def loadSurvey(experiment,src_dir,sv_dir):
    
    # Get list of directory contents
    files = glob.glob(src_dir + "*.segy")
    

#%% Define the experiment used #
#experiment="MENI"
experiment="MENII"
#experiment="MENDO"
#experiment="MENA"
#experiment="MCKSH"

## Directories to be used in pulling data ##
dir1 = "/Volumes/research/users/gferragu/"
#dir2 = "/Volumes/research/users/gferragu/MTJ/MTJ_Data/" + experiment + "/"

## For testing ##
#dir2 ="/Users/gabriel/local_testing/segy_test/" + experiment + "/" #local files for testing
dir2 ="/Volumes/research/users/gferragu/MTJ/MTJ_Data/" + experiment + "/segy_test/" #newberry files for testing

## Directories for saving data ##
svdir1 = "/Volumes/research/users/gferragu/MTJ/TXT/metadata/" + experiment + "/"
svdir2 = "/Volumes/research/users/gferragu/MTJ/graphics/" + experiment + "/shot_receiver_check/"

# Create File List
#files=glob.glob(dir2 + "*")
files = glob.glob(dir2 + "*.segy")

# Select file from list #
index = 1
file = files[index]

plt_svname = file.split('/')[-1].split('-')[:-1]

line = ''

if index == 0 :
    line = 'Line_1'
elif index == 1 :
    line = 'Line_6'
elif index == 2 : 
    line = 'Line_9'
    

print('\n##############################################################################################################################\n')
print("Loading file: " + str(file))
print('\n##############################################################################################################################\n')
      
st = Stream()

#%%

##########################################
# Read segy files into the Stream() object


##          For the MTJ Data            ##
##########################################

st = read(file, unpack_trace_headers=True)
