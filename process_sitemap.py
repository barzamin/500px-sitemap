import sys
import gzip
from lxml import etree
import re

RE_URL = re.compile(r'https?\://500px.com/photo/(\d+)')

filename = sys.argv[1]
if filename.endswith('gz'):
    with gzip.open(filename) as f:
        root = etree.parse(f)
else:
    with open(filename) as f:
        root = etree.parse(f)

urlset = root.getroot()

for url_e in urlset:
    loc_e = url_e.find('{*}loc')
    uri_match = RE_URL.match(loc_e.text)
    assert uri_match is not None
    idx = uri_match.group(1)

    license_e = url_e.find('{*}image').find('{*}license')
    license_uri = license_e.text
    if 'creativecommons' in license_uri:
        print(idx)
