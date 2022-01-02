
import re
from collections import namedtuple
import pandas as pd

# Writing to a csv
Line = namedtuple('Line', 'House_No Name NIC Gender Index')

line_test = "[1]49/1 වැල්මිල්ල ආරච්චිගේ දොන උදය ප්‍රියශාන්ත කුමාර 821173167V     ගැ 1"
# line_test ="""[1]49/1 වැල්මිල්ල ආරච්චිගේ දොන උදය ප්‍රියශාන්ත කුමාර 821173167V     ගැ 1
# | 1]49/2 මපතිරණගේ නිශාන්ත මොහන වික්‍රමසිංහ 662141682V පි 4"""

# line_re = re.compile(r'([\[|]\W*\d+[\]|]\d+\/?\d+)\s+(\W+)(\d+[VvXx]?)\s*(\W+)\s*(\d+)')
line_re = re.compile(r'(V\s+පි|V\s+ගැ)')
lines = []
if line_re.search(line_test):
    items = line_test.split()
    lines.append(Line(*items))
else:
    print('nope')

# df = pd.DataFrame(lines)

# df.to_csv('tester.csv', header=True, index=False, encoding='utf-8')