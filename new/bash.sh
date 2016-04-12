#!/bin/bash  
echo "I am done running ls"  
SOMEVAR='text stuff'  
echo "$SOMEVAR" 

lttng create my-session3
lttng enable-event -u -a
lttng enable kernel -all
lttng start
lttng stop



