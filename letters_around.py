import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    answer = re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', line)
    if answer is not None:
        print(answer)