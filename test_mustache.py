# -*- coding: utf-8 -*-
# @Author: jpthomas
# @Date:   2020-02-07 08:52:04
# @Last Modified by:   jpthomas
# @Last Modified time: 2020-02-07 15:24:37


import pystache
import yaml

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

with open('context.yaml', 'r') as f:
    contextData = yaml.load(f, Loader=Loader)
    print(contextData)
    for k, v in contextData.items():
        print(k, ":", v)

    renderer = pystache.Renderer()
    with open('output.txt', 'w') as outFile:

        outFile.write(renderer.render_path('template.mustache', contextData))
