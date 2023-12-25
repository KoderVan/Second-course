import re
import sys


def pattern_search():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'z.{3}z'
        result = re.search(pattern, line)
        if result:
            print(line)


pattern_search()