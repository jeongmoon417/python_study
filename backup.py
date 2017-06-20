# -*- coding: utf-8 -*-
##파일 백업 프로그램##
""" 
copy files from defined source directories (C:\jmoon),
make zip file, save zipped file to target directory
"""

import os
import time

#The files and directories to be backed up
source = ['"C:\jmoon"']

#main backup dirextory
target_dir = 'C:\TestBakup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    print 'backup directory ' + target_dir +' is not exist'
    os.mkdir(target_dir)
else: print 'backup directory is already exit'

zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

print "Zip command is:",
print zip_command

print "Running:"
if os.system(zip_command) ==0:
    print 'Successful back up to', target
else:
    print 'Backup FAILED'

