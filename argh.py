import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    answer = re.sub(r'\b[Aa]+\b', 'argh', line, count=1)
    if answer is not None:
        print(answer)