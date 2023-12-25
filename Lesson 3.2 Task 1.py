import re
import sys


def pattern_search():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = 'cat'
        result = re.findall(pattern, line)
        if len(result) >= 2:
            print(line)


pattern_search()