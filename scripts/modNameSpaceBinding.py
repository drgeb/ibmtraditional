#!/usr/bin/env python
server = sys.argv[0]
bindingName = sys.argv[1]
bindingValue = sys.argv[2]
bindingNameSpace = sys.argv[3]

# Obtain the "simple" server name
def getServerName(s):
    return AdminConfig.showAttribute(s, 'name')

# Add binding
def addBindingsToServer(s):
    for ns in AdminConfig.list( 'NameSpaceBinding' ).splitlines() :
        if bindingName == AdminConfig.showAttribute( ns, 'name' ):
            print "Removing existing binding from Server %s" % getServerName(s)
            AdminConfig.remove(ns)

    # Create binding
    print "Adding binding to Server %s" % getServerName(s)
    print AdminConfig.create('StringNameSpaceBinding', s, [['name', bindingName], ['nameInNameSpace', bindingNameSpace], ['stringToBind', bindingValue]])

# Set server and call function
server = AdminConfig.getid('/Server:'+server+'/')
addBindingsToServer(server)

# Save changes
if (AdminConfig.hasChanges()):
    AdminConfig.save()
