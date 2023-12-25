import re
import sys


def pattern_search():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'(\ba+\b)'
        result = re.sub(pattern, 'argh', line, count=1, flags=re.IGNORECASE)
        if result:
            print(result)


pattern_search()