import os
import sys
import dir_ops as do #module found in Analytics-Packages/Directory
from dir_ops import Path, Dir #custom classes found in Analytics-Packages/Directory

'''
This is a file for all repository-specific parameters.
If you have something changes user by user, put it in your user profile
'''

### Set up the file structure info - these are objects from the Path/Dir classes
params_Path = Path( os.path.abspath(__file__) )
repo_Dir = Dir( params_Path.ascend() )
data_Dir = Dir( repo_Dir.join('Data') )
wiki_Dir = Dir( repo_Dir.join( repo_Dir.dirs[-1] + '.wiki' ) ) #Repository/Repository.wiki
