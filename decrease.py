import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    answer = re.sub(r'\b(\w*?)((\w)\3+)\2*(\w*?)\b', r'\1\3\2\4', line)
    if answer is not None:
        print(answer)