#define

def add(link,total_current_asset):

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
            lst_commonstock.append(host)