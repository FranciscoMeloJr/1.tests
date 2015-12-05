#This will call program, tracer, trace compare and trace analysis -
#which is execute_analysis
#subprocess call:
import subprocess   
import sys
import os
subprocess.call(["clear"])
#tiger beetle:
os.chdir("/home/frank/Documents/Artigo/tibeecompare")
subprocess.call(["ls", "-l"])
subprocess.call(['source', 'setenv.sh'])

#prototype:
os.chdir("/home/frank/Documents/Artigo/1.tests/python/prototype")
subprocess.call(["ls", "-l"])
#subprocess.call(["cd",".."])

# enter the directory like this:

#Print output
#p = subprocess.Popen(["cd", ".."], stdout=subprocess.PIPE)
#output, err = p.communicate()
#print  output

#code:
#pid = subprocess.Popen([sys.executable, "execute_analysis.py"]) # call subprocess
#subprocess.call(['python', 'execute_analysis.py','open1000.json'])
#subprocess.call(['lttng-simple', '-k','-s','--','./open'])
#subprocess.call('cd ..', shell=True)
#subprocess.call(['source', 'setenv.sh'])

subprocess.call(["date"])
#subprocess.call(['ping', 'localhost'])
