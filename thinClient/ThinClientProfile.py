import os
from java.util import Date
from java.text import SimpleDateFormat
from java.lang import System

# Profile module to expose the wsadmin "objects", set the WebSphereVersion
# and update sys.path with the directories where Jython modules are found 
# specified by using the wsadmin.jython.libraries Java option.
#
# This profile module is primarily intended for use with the thinClient
# script that runs in an independent setup of a wsadmin thin client that
# is using a more recent version of Jython than that which comes with WAS.
# 
# The Java class that implements the wsadmin shell updates sys.path but also 
# automatically preloads Jython modules found in directory trees specified by 
# wsadmin.script.libraries.  This causes import problems for Jython libraries 
# with module interdependencies as well as dependencies on the WAS Admin objects.  
# The ThinClientProfile.py only modifies sys.path and does not preload any Jython 
# modules it finds in the libraries specified with wsadmin.jython.libraries.  
# The ThinClientProfile will load multiple libraries if there are multiple paths 
# specified with wsadmin.jython.libraries separated by a semi-colon.  Any scripts 
# that run must have a proper import statement to load desired modules from the 
# libraries. 
#
# NOTE: This profile is intended for use when the standard script libraries
# that come with WAS v7.0, v8.0, v8.5 are not used. You need to rename the 
# directory where the libraries are located to avoid having them loaded by 
# the wsadmin shell. They are located in:
#      <WAS_INSTALL_ROOT>/scriptLibraries
#
# This profile may be used when a more recent version of Jython is used.  
# You can download a more recent Jython and extract the archive into a directory 
# in <WAS_INSTALL_ROOT>/optionalLibraries.  Move the existing jython directory to 
# something like jython-v2.1.  Extract the newer Jython into a directory such as 
# jython-v2.5.2.  Make a symlink with the name jython to the newer version.  
# (The command is: ln -s jython-v2.5.2 jython )  To change back to using the 
# Jython that comes with WAS, remove the jython symlink and recreate it pointing 
# to the older jython directory. (ln -s jython-v2.1 jython) 
# 
# If you want to use a newer version of Jython as well as the WAS script 
# libraries you can include the WAS script libraries in the 
# -Dwsadmin.jython.libraries option.  You also have to add import statements 
# for the Admin objects to each Admin module in the WAS script libraries.  
# There is a shell script named addAdminObjectImport.sh that can be used to 
# modify the Admin modules appropriately. Obviously, you should make a copy
# of the WAS scriptLibraries directory tree and move it to some other location
# before modifying the individual modules to include import statements for
# the Admin objects. 
#
# This approach to setting up sys.modules with the wsadmin objects comes
# from the Gibson, McGrath, Bergman book: WebSphere Application Server
# Administration using Jython.
WASObjects = { 'AdminApp':AdminApp,
               'AdminConfig': AdminConfig,
               'AdminControl': AdminControl,
               'Help': Help
             }

# Check to see if AdminTask is in the namespace 
# and if it is, add it to the WASObjects to be added
# to sys.modules.  AdminTask won't be in the namespace
# if wsadmin is not connected to a server, e.g., connType=None.
if 'AdminTask' in dir():
  WASObjects[ 'AdminTask' ] = AdminTask
#endIf

# Now copy WASObjects into the sys.modules dictionary.
sys.modules.update( WASObjects )

# This is used as a convenient way to know what version is being used.
sys.modules[ 'WebSphereVersion' ] = '8.5'

###############################################################################
# The rest of this profile is used to set up sys.path so a Jython library 
# can be used conveniently.  

# _getTimeStamp() is for an info trace to stdout.
def _getTimeStamp():
  # WAS style time stamp.  SimpleDateFormat is not thread safe.
  sdf = SimpleDateFormat("yy/MM/dd HH:mm:ss.sss z")
  return '[' + sdf.format(Date()) + ']'
#endDef

#  
# The _updateLibraryPath() method is called from the os.path.walk()
# method with the three arguments.  See Jython Essentials for a 
# description of the os.path.walk() method.  (Or search the Internet
# for doc on os.path.walk().)
#
def _updateLibraryPath(libPath,dirname,files):
  for pathname in files:
    if (pathname.endswith('.py')):
      # At least one Jython module in the directory
      libPath.append(dirname)
      break
    #endIf
  #endFor
  return libPath
#enDef

# The _createJythonLibraryPath() method can be used to return a list
# of directories that have Jython (.py) modules defined in them that
# are somewhere in the directory tree rooted at the given library 
# directory root.  This method reproduces the wsadmin behavior of loading
# a library using the javaoption:
# -javaoption "-Dwsadmin.jython.libraries=<whatever>"
#
# NOTE: You can use java.lang.System.getProperty("wsadmin.jython.libraries")
# to get the -D property value, thus you can use the same command line
# option to set up a Jython library path as WAS v7 and later versions.
#
# NOTE: Append the result of this method to sys.path using extend()
#
def _createJythonLibraryPath(libRootDirectoryPath):
  libPath = []
  os.path.walk(libRootDirectoryPath,_updateLibraryPath,libPath)
  return libPath
#endDef

# The list of libraries associated with wsadmin.jython.libraries is assumed
# to be separated by semi-colon.  Each "library" is the path to the root 
# directory of the library directory tree.
jythonLibraries = System.getProperty("wsadmin.jython.libraries")
if (jythonLibraries != None and len(jythonLibraries) > 0):
  jythonLibraries = jythonLibraries.split(';')
  for jythonLibrary in jythonLibraries:
    timeStamp = _getTimeStamp()
    print timeStamp + " ThinClientProfile INFO loading library rooted at: " + jythonLibrary
    libraryPath = _createJythonLibraryPath(jythonLibrary)
    sys.path.extend(libraryPath)
  #endFor
else:
  timeStamp = _getTimeStamp()
  print timeStamp + " ThinClientProfile INFO No wsadmin.jython.libraries defined."
#endIf

# Remove unnecessary names from the namespace
del os, System, Date, SimpleDateFormat
del WASObjects, _updateLibraryPath, _getTimeStamp, _createJythonLibraryPath, jythonLibraries, timeStamp

# Check to make sure jythonLibrary is in the namespace.  It won't be if
# the part of the profile that deals with jython libraries didn't execute.
# A name error occurs if you try to remove something from the namespace 
# that isn't there.
if ('jythonLibrary' in dir()):
  del jythonLibrary, libraryPath
#endIf
