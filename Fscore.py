import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
balance_url = url.replace('financials','balance-sheet')
cashflow_url = url.replace('financials','cash-flow')
html = urllib.request.urlopen(url, context=ctx).read()
html_balance = urllib.request.urlopen(balance_url, context=ctx).read()
html_cashflow = urllib.request.urlopen(cashflow_url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')
soup_balance = BeautifulSoup(html_balance, 'html.parser')
soup_cashflow = BeautifulSoup(html_cashflow, 'html.parser')

# GP

test=soup.findAll("div",class_='rw-expnded')[2]
lst = list()
lst2 = list()
lst3 = list()
count = 0

for link in test:
    lst = link.decode()
    lst = lst.replace('>', '\n>').rsplit()

    for i in lst:
        if not i.endswith("</span"):
            continue
        if not i.startswith('>'):
            continue
        atpos = i.find('>')

        sppos = i.find("</span", atpos)

        host = i[atpos + 1:sppos]
        host = host.replace(',', '')
        host = int(host)
        lst3.append(host)

gp = lst3[1]-lst3[2]


if gp >0:
    print("GP is higher in the current year compared to the previous one.", 'increasing amount=£', gp , "(+1point)")
    count = count + 1
else:
    print('GP is lower in the current year compared to the previous one. Decreasing amount= £',gp,"(+0point)")




total_revenue =soup.findAll("div",class_='rw-expnded')[0]
lst_revenue = list()
for link in total_revenue:
    lst = link.decode()
    lst = lst.replace('>', '\n>').rsplit()

    for i in lst:
        if not i.endswith("</span"):
            continue

        if not i.startswith('>'):
            continue
        atpos = i.find('>')
        sppos = i.find("</span", atpos)

        host = i[atpos + 1:sppos]
        host = host.replace(',', '')
        host = int(host)
        lst_revenue.append(host)

this_total_revenue = lst_revenue[1]
last_total_revenue = lst_revenue[2]

#Net income

lst_net_income = list()
net_income =soup.findAll("div",class_='rw-expnded')[13]

for link in net_income:
    lst = link.decode()
    lst = lst.replace('>', '\n>').rsplit()

    for i in lst:
        if not i.endswith("</span"):
            continue

        if not i.startswith('>'):
            continue
        atpos = i.find('>')

        sppos = i.find("</span", atpos)

        host = i[atpos + 1:sppos]
        host = host.replace(',', '')
        host = int(host)

        lst_net_income.append(host)

this_net_income = lst_net_income[1]
last_net_income = lst_net_income[2]




#total asset & average total asset


lst_ave_total_asset = list()
ave_total_asset = list()

ave_total_asset =soup_balance.findAll("div",class_='rw-expnded')[20]
for link in ave_total_asset:
    lst = link.decode()
    lst = lst.replace('>', '\n>').rsplit()
    for i in lst:
        if not i.endswith("</span"):
            continue

        if not i.startswith('>'):
            continue
        atpos = i.find('>')
        sppos = i.find("</span", atpos)

        host = i[atpos + 1:sppos]
        host = host.replace(',', '')
        host = int(host)
        lst_ave_total_asset.append(host)

this_total_asset = lst_ave_total_asset[0]
last_total_asset = lst_ave_total_asset[1]
ave_total_asset = (this_total_asset+last_total_asset)/2


#AOR = Net income / average total assets
#Return on Assets (1 point if it is positive in the current year, 0 otherwise);

this_roa = this_net_income/ave_total_asset

if this_roa >0:
    print("ROA is positive in the current year.", 'ROA=', this_roa, "(+1point)")
    count = count + 1
else:
    print("ROA is negative in the current year.", 'ROA=', this_roa,"(+0point)")

# Change in Return of Assets (ROA)
# (1 point if ROA is higher in the current year compared to the previous one, 0 otherwise);

last_roa = last_net_income/ave_total_asset

if this_roa >last_roa :
    print("ROA is higher in the current year compared to the previous one","(+1point)")
    count = count + 1
else:
    print("ROA is lower in the current year compared to the previous one","(+0point)")



# Change in Asset Turnover ratio
# Asset Turnover ratio = total revenue / the average total asset
#Change in Asset Turnover ratio
# (1 point if it is higher in the current year compared to the previous one, 0 otherwise);

this_asset_turnover_ratio = this_total_revenue / ave_total_asset
last_asset_turnover_ratio = last_total_revenue / ave_total_asset



if this_asset_turnover_ratio >last_asset_turnover_ratio :
    print("Asset Turnover ratio is higher in the current year compared to the previous one","(+1point)")
    count = count + 1
else:
    print("Asset Turnover ratio is lower in the current year compared to the previous one",'(+0point)')

#Change in Current ratio
#(1 point if it is higher in the current year compared to the previous one, 0 otherwise);
#Total current asset/Total current liabilities

# total_current_asset

lst_total_current_asset = list()
total_current_asset = list()

total_current_asset =soup_balance.findAll("div",class_='rw-expnded')[9]

for link in total_current_asset:
    lst = link.decode()
    lst = lst.replace('>', '\n>').rsplit()

    for i in lst:
        if not i.endswith("</span"):
            continue

        if not i.startswith('>'):
            continue
        atpos = i.find('>')
        sppos = i.find("</span", atpos)

        host = i[atpos + 1:sppos]
        host = host.replace(',', '')
        host = int(host)

        lst_total_current_asset.append(host)
this_total_current_asset = lst_total_current_asset[0]
last_total_current_asset = lst_total_current_asset[1]


lst_total_current_liabilities= list()
total_current_liabilities = list()

total_current_liabilities =soup_balance.findAll("div",class_='rw-expnded')[30]

for link in total_current_liabilities:
    lst = link.decode()
    lst = lst.replace('>', '\n>').rsplit()
    for i in lst:
        if not i.endswith("</span"):
            continue

        if not i.startswith('>'):
            continue
        atpos = i.find('>')
        sppos = i.find("</span", atpos)

        host = i[atpos + 1:sppos]
        host = host.replace(',', '')
        host = int(host)
        lst_total_current_liabilities.append(host)
this_total_current_liabilities = lst_total_current_liabilities[0]
last_total_current_liabilities = lst_total_current_liabilities[1]

this_current_ratio = this_total_current_asset / this_total_current_liabilities
last_current_ratio = last_total_current_asset / last_total_current_liabilities




if this_current_ratio >last_current_ratio :
    print("Current ratio is higher in the current year compared to the previous one","(+1point)")
    count = count + 1
else:
    print("Current ratio is lower in the current year compared to the previous one",'(+0point)')

# total debt
# total debt = Total non-current liabilities

lst_total_non_current_liabilities= list()
total_non_current_liabilities = list()

total_non_current_liabilities =soup_balance.findAll("div",class_='rw-expnded')[36]

for link in total_non_current_liabilities:
    lst = link.decode()
    lst = lst.replace('>', '\n>').rsplit()# 줄나누기
    #print(lst)
    #lst2 = re.findall('^>.*</span', lst)
    for i in lst:
        if not i.endswith("</span"):
            continue

        if not i.startswith('>'):
            continue
        atpos = i.find('>')
        sppos = i.find("</span", atpos)

        host = i[atpos + 1:sppos]
        host = host.replace(',', '')
        host = int(host)
        lst_total_non_current_liabilities.append(host)

this_total_non_current_liabilities = lst_total_non_current_liabilities[0]
last_total_non_current_liabilities = lst_total_non_current_liabilities[1]


#Change in Leverage(long-term)
#Change in Leverage (long-term) ratio
# (1 point if the ratio is lower this year compared to the previous one, 0 otherwise);

this_leverage = this_total_non_current_liabilities / this_total_asset
last_leverage = last_total_non_current_liabilities / last_total_asset


if this_leverage < last_leverage :
    print("Current leverage is lower in the current year compared to the previous one","(+1point)")
    count = count + 1
else:
    print("Current leverage is higher in the current year compared to the previous one",'(+0point)')

#Operating Cash Flow
#Net cash provided by operating activities
#Operating Cash Flow (1 point if it is positive in the current year, 0 otherwise);

lst_op_cashflow= list()
op_cashflow = list()

op_cashflow =soup_cashflow.findAll("div",class_='rw-expnded')[11]


for link in op_cashflow:
    lst = link.decode()
    lst = lst.replace('>', '\n>').rsplit()# 줄나누기

    for i in lst:
        if not i.endswith("</span"):
            continue

        if not i.startswith('>'):
            continue
        atpos = i.find('>')

        sppos = i.find("</span", atpos)

        host = i[atpos + 1:sppos]
        host = host.replace(',', '')
        host = int(host)
        lst_op_cashflow.append(host)


this_op_cashflow = lst_op_cashflow[1]


if this_op_cashflow > 0 :
    print("Operating Cash Flow is positive in the current year","(+1point)")
    count = count + 1
else:
    print("Operating Cash Flow is negative in the current year",'(+0point)')


#Accruals
# (1 point if Operating Cash Flow/Total Assets is higher than ROA in the current year, 0 otherwise);

accruals = this_op_cashflow / this_total_asset



if accruals > this_roa :
    print("(Operating Cash Flow/Total Assets) is higher than ROA in the current year","(+1point)")
    count = count + 1
else:
    print("(Operating Cash Flow/Total Assets) is lower than ROA in the current year",'(+0point)')



# Final score

print("final score is",count,'/8')