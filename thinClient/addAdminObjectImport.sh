#!/bin/bash
#
# Script to admin import of Admin objects to all of the modules in the
# WAS script libraries.  
#
# NOTES
#    This script takes advantage of the fact that every module except 
#    AdminUtilities has an import AdminUtilities statement in it.
#    So sed is used to substitute an additional line that is the
#    import for the Admin objects.  For the AdminUtilities module
#    there is an import sys statement that is used as the marker
#    for doing the import of the Admin objects.
#
# INPUTS
#    -libraryHome     - (required) full path to WAS script library home
#    -add             - (optional) add the import statements (this is the default)
#    -remove          - (optional) remove the previously added import statement
#    -sedBackup       - (optional) option to -i of sed to use as suffix for backup
#                       file creation. Not normally provided.
#
function usage {
  echo "Usage: addAdminObjectImport.sh <options>"
  echo "Options:"
  echo "       -libraryHome <pathToLibraryRootDirectory>  - (required) path to root of script library directory"
  echo "       -add                                       - (optional) Add the import statement to the Admin modules in the library."
  echo "                                                    The default is to add the import statement."
  echo "       -remove                                    - (optional) Remove the previously added import statement for the admin" 
  echo "                                                    objects in the Admin modules in the library."
  echo "                                                    The remove operation is intended for testing to restore Admin modules to"
  echo "                                                    their original content."
  echo "       -sedBackup <extension>                     - (optional) argument to -i option of sed to use as suffix for creating"
  echo "                                                    backup file name."
  echo "                                                    If -sedBackup option is not provided an in-place edit is done and"
  echo "                                                    no backup file is created by sed. Typically, this option is not used."
  echo "Example: "
  echo "  ./addAdminObjectImport -libraryHome ./wasScriptLibraries"
}

# adminObjects holds the full list of Admin objects of interest
adminObjects="AdminConfig AdminControl AdminTask AdminApp"

# 
# getImportList uses egrep to see if the given module uses
# a given Admin object.  The test is to find a line in the given
# module that has the Admin object name followed immediately by the
# period character, e.g., AdminConfig.showAttribute.  The thinking
# is that if there is a line in the given module where an Admin 
# object method is invoked then in fact that object is really used.
# Testing for just the Admin object name picks up things like
# AdminApplication or AdminController or AdminConfigurator if 
# those sorts of names would be used.
#
# This function could be fooled by the presence of commented out
# lines where an Admin object is used in the given module. 
#
# INPUTS
#    module - $1 argu - path to the module
#
# OUTPUT
#    imports - a comma and space separated list of Admin objects 
#    used by the module.  The caller can use this list to create an
#    appropriate Jython import statement for the module.
#
function getImportList {
  local module
  module=$1
  imports=""
  for obj in $adminObjects; do
    usesObject=$(egrep -m 1 -e "$obj\." $module)
    if [ -n "$usesObject" ]; then
      if [ -n "$imports" ]; then
        imports="$imports, $obj"
      else
        imports="$obj"
      fi
    fi
  done
  echo "$imports"
}


# The addImportStatement() function is usually what gets invoked.  
# It is the function used to add the appropriate import statement
# to all of the Admin modules in the WAS script library.
#
# In each module after the "import AdminUtilities" statement, insert 
# a line that imports the Admin objects used in that module.
# AdminUtilities.py is special since it doesn't have an import of itself.
# So we have to use a different text pattern to determine where to 
# add its Admin object import. For AdminUtilities, we look for an 
# "import ExtClassLoader" instead.
#
function addImportStatement {
  # Get a list of all the Admin .py files in the library directory tree
  modules=$(find "$libraryHome" -name "Admin*.py")

  for m in $modules; do
    importList=$(getImportList $m)
    #echo "For module: $m, import list = $importList"    # for debug
    if [ -z "$importList" ]; then
      echo "Module $m doesn't use any of the Admin objects.  No modification necessary."
    else
      sedPattern="import AdminUtilities"
      if [ "${m##*/}" = "AdminUtilities.py" ]; then 
        sedPattern="import ExtClassLoader"
      fi

      # Check to see if module already has proper import of Admin objects
      alreadyImported=$(grep "import $importList" $m)
      if [ -n "$alreadyImported" ]; then
        echo "Module $m already has an \"import $importList\" statement."
      else
        sed -i${sedBackup} /"$sedPattern"/a"import $importList" $m
        if [ "$?" = "0" ]; then
          # edit was successful, report results
          echo "Added \"import $importList\" statement to module: $m"
        else
          # We don't expect this to happen, but in case it does, report it.
          echo "Skipped modifying $m. Expected to find \"$sedPattern\", but did not."  
        fi
      fi
    fi
  done 
}

# The removeImportStatement() function removes the previously added
# import statement of the Admin objects from the Admin modules in 
# the WAS script library.  This method gets invoked when the -remove
# option is provided on the command line.  It is primarily intended
# for testing purposes.  After this method is run the Admin library
# modules should be restored to their original state.
#
function removeImportStatement {
  # Get a list of all the Admin .py files in the library directory tree
  modules=$(find "$libraryHome" -name "Admin*.py")

  for m in $modules; do
    importList=$(getImportList $m)
    #echo "For module: $m, import list = $importList"    # for debug
    sedPattern="import $importList"

    # Check to see if module already has proper import of Admin objects
    sed -i${sedBackup} /"$sedPattern"/d $m
    if [ "$?" = "0" ]; then
      # edit was successful, report results
      echo "Removed \"import $importList\" statement to module: $m"
    else
      echo "The \"$sedPattern\" statement is not present in the module: $m"  
    fi
  done 
}

# BEGIN MAIN

if (( $# == 0 )); then
  usage
  exit 0
fi

libraryHome=""
sedBackup=""
operation="add"

# process the input args
# For keyword-value arguments the arg gets the keyword and
# the case statement assigns the value to a script variable.
# If any "switch" args are added to the command line args,
# then it wouldn't need a shift after processing the switch
# keyword.  The script variable for a switch argument would
# be initialized to "false" and if the switch is provided on
# the command line it would be assigned "true".
#
while (( $# > 0 )); do
  arg=$1
  case $arg in
    # explicit -? for help
    "-?" )          usage; exit 0
                    ;;

    # other options to get help
    -h|-help )      usage; exit 0
                    ;;

    -add )          operation="add"
                    ;;

    -libraryHome )  libraryHome=$2; shift
                    ;;

    -sedBackup )    sedBackup=$2; shift
                    ;;

    -remove )       operation="remove"
                    ;;

    * ) usage; echo "Unknown option: $arg in command line." 
        exit -1
        ;;
  esac
  # shift to next key-value pair
  shift
done


if [ -z "$libraryHome" ]; then
  echo "libraryHome is a required input."
  usage 
  exit -1
fi

if [ ! -d "$libraryHome" ]; then 
  echo "Script library directory does not exist: $libraryHome"
  exit -1
fi

if [ "add" = "$operation" ]; then
  addImportStatement
elif [ "remove" = "$operation" ]; then
  removeImportStatement
else
  echo "Unexpected operation provided: \"$operation\""
  exit -1
fi

exit 0

# END
