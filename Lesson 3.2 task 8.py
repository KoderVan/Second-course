import re
import sys


def pattern_search():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'\b(\w)(\w)'
        result = re.sub(pattern, r'\2\1', line)
        if result:
            print(result)


pattern_search()