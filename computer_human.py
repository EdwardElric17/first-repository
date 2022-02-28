import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    answer = re.sub(r'human', 'computer', line)
    if answer is not None:
        print(line)