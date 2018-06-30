import sys
import gzip
from lxml import etree
import re

filename = sys.argv[1]
if filename.endswith('gz'):
    with gzip.open(filename) as f:
        root = etree.parse(f)
else:
    with open(filename) as f:
        root = etree.parse(f)

urlset = root.getroot()

RE_URL = re.compile(r'https?\://500px.com/photo/(\d+)')

for url_e in urlset:
    loc_e = url_e.find('{*}loc')
    uri = loc_e.text
    uri_match = RE_URL.match(uri)
    assert uri_match is not None

    idx = uri_match.group(1)
