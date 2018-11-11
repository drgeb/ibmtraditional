#!/usr/bin/env python

import yaml
try:
    my_dict = yaml.load(open('example.yaml'))
#    nodeName serverName templateID jdbcProvider implementationClass
    print(my_dict)
    for key in my_dict:
        print (key)
except yaml.YAMLError as exc:
    print(exc)
