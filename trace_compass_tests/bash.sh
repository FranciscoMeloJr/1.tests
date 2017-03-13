#!/bin/bash
echo "hi"

lttng create
lttng enable-event -u -a
lttng start

LD_PRELOAD=liblttng-ust-cyg-profile.so $1 

lttng stop
lttng destroy

