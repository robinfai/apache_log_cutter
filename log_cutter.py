__author__ = 'RobinFai'

# example log_cutter.py log_path=/private/var/log/apache2/localhost-access_log out_path=/private/var/log/apache2/daily

import sys
import os

args = {}
for i, eachArg in enumerate(sys.argv):
    param = str(eachArg).split("=")
    if len(param) == 2:
        args.setdefault(param[0], param[1])
requiredParams = ['log_path', 'out_path']
for param in requiredParams:
    if not param in args:
        print param, ' is required'
        exit()

if not os.path.exists(args['out_path']):
    print 'out_path is not exists'
    exit()
if not os.path.isdir(args['out_path']):
    print 'out_path is not dir'
    exit()
if not args['out_path'][-1] is "/":
    args['out_path'] += "/"

for line in open(args['log_path']):
    row = line.split(" ")
    file_name = row[3].split(":")[0][1:].replace("/", "-")
    print file_name
    output = open(args['out_path']+file_name, 'a+')
    output.write(line)
    output.close()
