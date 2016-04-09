#!/bin/bash  
echo "I am done running ls"  
SOMEVAR='text stuff'  
echo "$SOMEVAR" 

lttng create my-session3
lttng enable-event -u -a
lttng enable-event -u -a
lttng start
lttng stop



