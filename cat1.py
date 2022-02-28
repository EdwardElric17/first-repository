import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    answer = re.search(r'\b(cat)\b', line)
    if answer is not None:
        print(line)