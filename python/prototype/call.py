#This will call program, tracer, trace compare and trace analysis -
#which is execute_analysis
#subprocess call:
import subprocess   
import sys
import os

#to delete folders:
import shutil

#timer:
import time

def xis(arg):
    "This function executes bash commands"
    bashCommand = arg
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
    return process
    
def password():
    "Sudo Su function"
    os.popen("sudo -S %s"%('ls'), 'w').write('Josias2103\n')
    
def runProgramAndTrace():
    subprocess.call(['lttng-simple', '-k','-s','--','./open'])
    
def tigerBeatle():
    #tiger beetle:
    #os.chdir("/home/frank/Documents/Artigo/tibeecompare")
    #function("cd /home/frank/Documents/Artigo/tibeecompare")
    print("tigerBeatle")
    bashCommand = "sudo;cd /home/frank/Documents/Artigo/tibeecompare;pwd;ls;source setenv.sh;src/build/tibeebuild --name prototipo --begin kernel/syscall_entry_open --end kernel/syscall_entry_close --trace /home/frank/Documents/Artigo/1.tests/python/prototype/open-k;src/report/tibeereport --name prototipo;mv prototipo.json /home/frank/Documents/Artigo/1.tests/python/prototype/data"
    subprocess.call(['bash','-c', bashCommand])

    #bashCommand = "pwd"
    
    #source
    #bashCommand = "source setenv.sh"
    

    #build
    #bashCommand = "src/build/tibeebuild --name prototipo --begin kernel/syscall_entry_open --end kernel/syscall_entry_close --trace /home/frank/Documents/Artigo/1.tests/python/prototype/open-k"
    
    
    #report
    #bashCommand = "src/report/tibeereport --name prototipo"
    
    
    #move
    #bashCommand = "mv prototipo.json /home/frank/Documents/Artigo/1.tests/python/prototype/data"
    
    
def subCall(arg1,arg2):
    print("Subcall")
    if arg2 is not None:
        subprocess.call([arg1,arg2])
    else:
        subprocess.call([arg1])
        
def runProgAnalysis():
    print("Analysis")
    subprocess.call(['python', 'execute_analysis.py','data/prototipo.json','data/test.csv'])

def accumulate():
    "This function accumulates the csv for each execution"
    print("Accumulating")
    subprocess.call(['python', 'write_read_module.py','data/test.csv','data/final.csv'])# program input - output
    
    
def erase_files(arcs):
    "This function erases the files"
    print("Delete files")
    for each in arcs:
        os.remove(each)
    #erase csv
    #os.remove("data/test.csv")
    print("I am erasing a file")
    
def erase_dir(directories):
    print("Delete archive")
    for each in directories:
        shutil.rmtree(each)

def simulation():
    "This simulates"
    print("Simulation")
    #begin:
    xis("ls -1")
    password()

    #run and generate the trace:
    runProgramAndTrace()
    #tigerBeatle:
    tigerBeatle()
    #Analysis:
    runProgAnalysis()
    #Accumulate:
    accumulate()
    #Delete:
    erase_files(['data/test.csv'])
    erase_dir(["open-k"])
#    subCall("date","")
#    subprocess.call(["clear"])

def wait(time_wait):
    while True:
        "This prints once 20 cents"
        simulation()
        time.sleep(time_wait)#seconds

#prototype:
#erase_dir(["data/D"])
#accumulate()
simulation()
#wait(20)
#password()

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
