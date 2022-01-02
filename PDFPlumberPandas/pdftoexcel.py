import re
import parse
import pdfplumber
import pandas as pd
from collections import namedtuple

Line = namedtuple('Line', 'company_id company_name doctype reference currency voucher inv_date due_date open_amt_tc open_amt_bc current months1 months2 months3')

company_re = re.compile(r'(V\d+) (.*) Phone:')
line_re = re.compile(r'\d{2}/\d{2}/\d{4} \d{2}/\d{2}/\d{4}')

file = '2017_Col_KadMC_12Mal_12A.pdf'

lines = []
total_check = 0

with pdfplumber.open(file) as pdf:
    pages = pdf.pages
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split('\n'):
            print(line)
            # comp = company_re.search(line)
            # if comp:
            #     vend_no, vend_name = comp.group(1), comp.group(2)

            # elif line.startswith('INVOICES'):
            #     doctype = 'INVOICE'

# df = pd.DataFrame(lines)
# df.head()

# df.to_csv('invoices.csv', index=False)