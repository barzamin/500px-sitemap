import sys
import gzip
from lxml import etree

filename = sys.argv[1]
if filename.endswith('gz')
    with gzip.open(filename) as f:
        root = etree.parse(f)
else:
    with open(filename) as f:
        root = etree.parse(f)