import re
import sys


def pattern_search():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'(\w)\1+'
        result = re.sub(pattern, r'\1', line)
        if result:
            print(result)


pattern_search()