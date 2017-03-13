
CFLAGS  = -g -Wall -finstrument-functions -ldl -llttng-ust
main: main.cpp 
	$(CXX) $(CFLAGS) $? $(LDFLAGS) -o $@
clean:
	$(RM) *.o main

