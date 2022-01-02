import re
from collections import namedtuple
import pandas as pd
import codecs
import sys
Line = namedtuple('Line', 'House_No Name NIC Gender Index')

#පි ගැ
# line_test = "[1]49/1 වැල්මිල්ල ආරච්චිගේ දොන උදය ප්‍රියශාන්ත කුමාර 821173167V     ගැ 1"
line_test ="""[1]49/1 වැල්මිල්ල ආරච්චිගේ දොන උදය ප්‍රියශාන්ත කුමාර 821173167V     ගැ 1
| 1]49/2 මපතිරණගේ නිශාන්ත මොහන වික්‍රමසිංහ 662141682V පි 4"""
# line_re = re.compile(r'(V\s+පි|V\s+ගැ)')
# line_re = re.compile(r'([\[|]\W*\d+[\]|]\d+\/?\d+)\s+(\W+)(\d+[VvXx]?)\s*(\W+)\s*(\d+)')
line_re = re.compile(r'([\[|]\W*\d+[\]|]\d+\/?\d+).*(\d+[VvXx]?)\s*(\W+)\s*.*(\d+)',re.M)
# line_re = re.compile(r'([\[|]\W*\d+[\]|]\d+\/?\d+)\s+(\W+)(\d+[VvXx]?)\s*(\W+)\s*(\d+)',re.UNICODE)

lines = []
if line_re.search(line_test):
    items = line_test.split()
    lines.append(Line(*items))
    # df = pd.DataFrame(lines)
    # df.to_csv('tester2.csv', header=True, index=False, encoding='utf-8')

else:
    print('nope')

# print(lines)

# ------------------------------------
print(re.match(r'([\[|]\W*\d+[\]|]\d+\/?\d+)\s+', line_test).group(2))
heading  = r'[1]49/1 වැල්මිල්ල ආරච්චිගේ දොන උදය ප්‍රියශාන්ත කුමාර 821173167V     ගැ 1'
print(re.match(r'([\[|]\W*\d+[\]|]\d+\/?\d+)(.*\s+)(\d+[VvXx]?)\s*(\W+)\s*.*(\d+)', line_test).group(2))
print(re.match(r'[^\W\d_]', line_test).group(2))
print(line_re.findall(line_test))
# for match in matches:
#     print(match)
# ------------------------------------
# df = pd.DataFrame(lines)
# print(df['Name'])

# df.info()
# df['Name'] = df['Name'].astype('unicode')
# df['Name'] = df['Name'].apply(lambda x: x.encode('utf-8').strip())
# df['Name'] = df['Name'].map(lambda x: x.encode('unicode-escape').decode('utf-16'))
# df['Name'] = df['Name'].map(lambda x: x.encode('unicode-escape'))
# print(df['Name'])
# df['Name'] = df['Name'].map(lambda x: x.decode('utf-16'))
# print(df['Name'])
# df.info()
# df.to_csv('tester.csv', index=False)
# df.to_csv('tester2.csv', header=True, index=False, encoding='utf-8')

# text = u'pi: π'
# wrapped_stdout = codecs.getwriter('UTF-8')(sys.stdout)
# wrapped_stdout.write(u'Via write: ' + text + '\n')

# # Replace sys.stdout with a writer
# sys.stdout = wrapped_stdout

# print (u'Via print:', text)