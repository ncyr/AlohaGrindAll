import os, time

iberdir = os.popen('echo %IBERDIR%').read().strip()
pathdir = os.listdir(iberdir)
qsts = input('q or t?')

if qsts == 'q':
    grindexe = 'grindq'
else:
    grindexe = 'grind'

for row in pathdir:
    
    if row.isnumeric() is True:
        print('Running:'+ iberdir + '\\bin\\'+ grindexe + ' /date ' + row)
        result = os.popen(iberdir + '\\bin\\'+ grindexe + ' /date ' + row)
        print(result.read() + '-OK')

print("I've completed processing all dated subdirs!")
