import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    answer = re.search(r'.*cat.*cat.*', line)
    if answer is not None:
        print(answer.group())