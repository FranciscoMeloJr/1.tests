import sys
from babeltrace import *

traces = TraceCollection()
ret = traces.add_trace(sys.argv[1], "ctf")

lockers = {}
for event in traces.events:
    # metadata about mutex and thread context
    addr, name = event["addr"], event["name"]
    thread_id = event["pthread_id"]

    # identifies a thread interacting with a mutex
    locker = (thread_id, addr)

    # record a thread entering Mutex::Lock
    if event.name == "mutex:lock_enter":
        lockers[locker] = event.timestamp

    # calculate time spent in Mutex::Lock
    elif event.name == "mutex:lock_exit":
        try:
            duration = event.timestamp - lockers[locker]
            del lockers[locker]
            print (duration, name)
        except KeyError:
            continue

