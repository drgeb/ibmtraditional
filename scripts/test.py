#!/usr/bin/env python

import yaml
try:
    my_dict = yaml.load(open('example.yaml'))

    nodeName serverName templateID jdbcProvider implementationClass

attributes = sys.argv[5]
    print(my_dict)
except yaml.YAMLError as exc:
    print(exc)
