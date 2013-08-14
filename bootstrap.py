#!/usr/bin/env python
import virtualenv
import os
import sys
import subprocess


home_dir = 'env'


def after_install(options, home_dir):
    _, _, _, bin_dir = virtualenv.path_locations(home_dir)
    process = os.path.join(bin_dir, 'pip')
    requirements_file = os.path.join(home_dir, '..', 'requirements.txt')
    subprocess.call([process, 'install', '-r', requirements_file])

    print
    print "Run %s/activate to load the virtual environment" % bin_dir


def adjust_options(options, args):
    if len(args) == 0:
        args.append(home_dir)


virtualenv.after_install = after_install
virtualenv.adjust_options = adjust_options

virtualenv.main()
