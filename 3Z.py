import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    answer = re.search(r'z.{3}z', line)
    if answer is not None:
        print(line)