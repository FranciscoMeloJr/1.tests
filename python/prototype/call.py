#This will call program, tracer, trace compare and trace analysis -
#which is execute_analysis
#subprocess call:
import subprocess   
import sys
import os

def function(arg):
    "This function executes bash commands"
    bashCommand = arg
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
    return process
    
def password():
    "Sudo Su function"
    bashCommand = "sudo su"
    process = subprocess.Popen(bashCommand.split(), stdin=subprocess.PIPE)
    process.communicate("Josias2103")
    
def runProgramAndTrace():
    subprocess.call(['lttng-simple', '-k','-s','--','./open'])
    
def tigerBeatle():
    #tiger beetle:
    #os.chdir("/home/frank/Documents/Artigo/tibeecompare")
    #function("cd /home/frank/Documents/Artigo/tibeecompare")
    bashCommand = "cd /home/frank/Documents/Artigo/tibeecompare"
    output = subprocess.check_output(['bash','-c', bashCommand])

    #source
    bashCommand = "source setenv.sh"
    subprocess.call(['bash','-c', bashCommand])

    #build
    bashCommand = "src/build/tibeebuild --name prototipo --begin kernel/syscall_entry_open --end kernel/syscall_entry_close --trace /home/frank/Documents/Artigo/1.tests/naser_tests/open-k"
    subprocess.check_output(['bash','-c', bashCommand])
    
    #report
    bashCommand = "src/report/tibeereport --name prototipo"
    subprocess.check_output(['bash','-c', bashCommand])
    
    #move
    bashCommand = "mv prototipo.json /home/frank/Documents/Artigo/1.tests/python/prototype/data"
    subprocess.check_output(['bash','-c', bashCommand])
    
def subCall(arg1,arg2):
    if arg2 is not None:
        subprocess.call([arg1,arg2])
    else: 
        subprocess.call([arg1])
        
def runProgAnalysis():
    subprocess.call(['python', 'execute_analysis.py','data/prototype.json'])

def accumulate():
    "This function accumulates the csv for each execution"
    print("Accumulating")
    
def erase():
    #erase trace:
    #erase db
    #erase csv
    print("I am erasing")

#begin:
function("ls -1")
password()

#run and generate the trace:
runProgramAndTrace()
#tigerBeatle:
tigerBeatle()
#Analysis:
runProgAnalysis()

subCall("date","")
subprocess.call(["clear"])


#prototype:


#subprocess.call(["cd",".."])

# Enter the directory like this:

#Print output
#p = subprocess.Popen(["cd", ".."], stdout=subprocess.PIPE)
#output, err = p.communicate()
#print  output

#code:
#pid = subprocess.Popen([sys.executable, "execute_analysis.py"]) # call subprocess
#
#
#subprocess.call('cd ..', shell=True)
#subprocess.call(['source', 'setenv.sh'])


#subprocess.call(['ping', 'localhost'])
