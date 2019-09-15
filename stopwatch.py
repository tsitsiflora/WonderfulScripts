#! python3
# stopwatch.py - A simple stopwatch program

import time

# display program instructions
print('Press Enter to begin. Afterwards, press enter to "click the" stopwatch. Press "CTRL + C" to quit.')

input()  # press Enter to begin
print('Started!')
start_time = time.time()  # note the first lap's start time
last_time = start_time
lap_count = 1

try:
    while True:
        input()
        lap_time = round((time.time() - last_time)/60, 2)
        total_time = round((time.time() - start_time)/60, 2)
        print('Lap #{0} : {1} minute(s) ({2} minute(s))'.format(
            lap_count, total_time, lap_time))
        lap_count += 1
        last_time = time.time()  # reset the last lap time
except KeyboardInterrupt:
    print('Done!')

# TODO - convert seconds to human readable minutes
