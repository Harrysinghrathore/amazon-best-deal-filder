import time
import requests as session
import re
import random
from bs4 import BeautifulSoup
import pandas

# from requests_html import HTMLSession
# requests = HTMLSession()
import lxml

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]







proxie = [
{"http": 'http://vickramkishun:k2WENqigRg@168.181.229.168:59100',"https": 'http://vickramkishun:k2WENqigRg@168.181.229.168:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@138.36.92.199:59100', "https": 'http://vickramkishun:k2WENqigRg@138.36.92.199:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@138.36.92.81:59100', "https": 'http://vickramkishun:k2WENqigRg@138.36.92.81:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@138.36.92.66:59100', "https": 'http://vickramkishun:k2WENqigRg@138.36.92.66:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@138.36.93.35:59100',"https": 'http://vickramkishun:k2WENqigRg@138.36.93.35:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@168.181.229.249:59100' ,"https": 'http://vickramkishun:k2WENqigRg@168.181.229.249:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@95.164.145.138:59100',"https": 'http://vickramkishun:k2WENqigRg@95.164.145.138:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@138.36.93.32:59100',"https": 'http://vickramkishun:k2WENqigRg@138.36.93.32:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@95.164.145.87:59100',"https": 'http://vickramkishun:k2WENqigRg@95.164.145.87:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@95.164.145.89:59100',"https": 'http://vickramkishun:k2WENqigRg@95.164.145.89:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@138.36.95.175:59100',"https": 'http://vickramkishun:k2WENqigRg@138.36.95.175:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@168.181.229.129:59100',"https": 'http://vickramkishun:k2WENqigRg@168.181.229.129:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@138.36.95.173:59100',"https": 'http://vickramkishun:k2WENqigRg@138.36.95.173:59100'},
{"http": 'http://vickramkishun:k2WENqigRg@94.131.51.207:59100',"https": 'http://vickramkishun:k2WENqigRg@94.131.51.207:59100'}
]
header = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-User": "?1",
        "Referer": "https://www.google.com",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(user_agents)
    }
df = pandas.read_csv("Experiment.csv")
# pandas.DataFrame()
urls_list_of_products = []
for key, value in df.to_dict()['Unnamed: 1'].items():
    if isinstance(value, str):
        # print(key)
        urls_list_of_products.append(value)

product_names_list = []
for product_url in urls_list_of_products[0: 2]:
    raw_product_url = product_url

    res = session.get(url=raw_product_url, headers=header, proxies=random.choice(proxie))

    soup = BeautifulSoup(res.text, 'lxml')
    items = soup.find_all('span') #{'class': re.compile(r'price')})
    # print(soup)
    prices = []
    # print(res.text)
    # print(soup.text)
    for it in items:
        # print("=+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(it)
        # print("=+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(it.text)

        if "$0" not in str(it.text) and "$" in str(it.text) and "price" in str(it) or 'Price' in str(it) or "sale" in str(it) or "money" in str(it):

            raw_price = str(it.text).replace(',', '').replace('\n', '').replace("$", ' ').replace('USD', '').replace('now', '').replace('Now','').replace('-', '').split(' ')

            # print('added')
            # print('raw price ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', raw_price)
            prices.extend(raw_price)
        else:
            # print(it.text)
            pass
    # print(prices)
    # print(prices)

    final_list = []

    for ite in prices:
        try:
            # ite = ite.replace(',', '')
            if float(ite) not in final_list:
                final_list.append(float(ite))
                # print(final_list)
        except:
            pass

    if final_list:
        try:
            # if int(final_list[0]) != 0  and int(final_list[1]) != 0:
            #     last_list = [final_list[0], final_list[1]]
            # else:
            last_list = [final_list[0]]
            pro_price = min(last_list)
        except:
            last_list = [final_list[0]]
            pro_price = last_list[0]
            # print(it)
        print(pro_price)
    else:
        pro_price = 'not found'

    # print(BeautifulSoup(str(it).split("/del>")[-1], 'html.parser').text)

    item = soup.find_all('h1')
    name = []
    for it in item:
        # print(it)
        if "name" in str(it) or "title" in str(it):
            # prices.append(str(it.text))
            name.append(str(it.text))
    try:
        pro_name = name[0]
        pro_name = pro_name.replace('\n', '').strip()
    except:
        try:
            item = soup.find_all('h2')
            name = []
            for it in item:
                # print(it)
                if "name" in str(it) or "title" in str(it):
                    # prices.append(str(it.text))
                    name.append(str(it.text))
            pro_name = name[0]
            # pro_name = name[0]
            pro_name = pro_name.replace('\n', '').strip()
        except:
            print('unscrapable')
            pro_name = 'not found prod name'
    try:
        print(pro_name)
    except:
        pro_name = 'not found prod name'
    print(pro_name)
    if pro_name != 'not found prod name':
        product_names_list.append(pro_name)
    else:
        print('website not scrapable')









for pro_name in product_names_list:
    query = pro_name.replace(" ", "+").replace(":", "%3A").replace(",", "%2C").replace("&", "%26")
    current_time = time.time()
    # query = "AOMAIS Women's High Top Sneakers Fashion Lace-Up Canvas Casual Shoes Comfortable Walking Shoes (Off-White US8)".replace(' ', '')
    pro_accuracy_score = pro_name.split()
    final_list_of_google = []
    resp = session.get(url=f'https://www.google.com/search?client=ubuntu-sn&hs=HxD&sca_esv=554155314&channel=fs&biw=1846&bih=968&tbm=shop&sxsrf=AB5stBhcs-3MvtJ7suezZ7f7s5Nldnz6DQ%3A{str(current_time).replace(".", "")[0:13]}&q={str(pro_name).replace(" ", "+").replace(":", "%3A").replace(",", "%2C").replace("&", "%26")}+Amazon.com&tbm=shop&source=lnms&sa=X&ved=2ahUKEwjorKaQ9smAAxUCdmwGHeZVDR4Q0pQJegQICxAB&biw=1846&bih=968&dpr=1', headers=header, timeout=4, proxies=random.choice(proxie))

    print(f'https://www.google.com/search?client=ubuntu-sn&hs=HxD&sca_esv=554155314&channel=fs&biw=1846&bih=968&tbm=shop&sxsrf=AB5stBhcs-3MvtJ7suezZ7f7s5Nldnz6DQ%3A{str(current_time).replace(".", "")[0:13]}&q={str(pro_name).replace(" ","+").replace(":", "%3A").replace(",","%2C").replace("&", "%26")}+amazon.com&tbm=shop&source=lnms&sa=X&ved=2ahUKEwjorKaQ9smAAxUCdmwGHeZVDR4Q0pQJegQICxAB&biw=1846&bih=968&dpr=1')
    bsr = BeautifulSoup(resp.text, 'html.parser')
    final_prices = []

    for it in bsr.select('.sh-sr__shop-result-group .sh-dgr__content .shntl .XrAfOe span .kHxwFf .a8Pemb '):
        final_prices.append(float(it.text.replace('$', '').replace('₹', '').replace('+ tax', '').replace(',', '')))

    res = bsr.select('.sh-sr__shop-result-group .sh-dgr__content .eaGTj div .shntl')

    url_list = []
    for it in res:
        if 'KoNVE' in str(it):
            simple_url = it.get('href')
            # print(simple_url)
            med_url = simple_url.replace(simple_url[simple_url.rfind('&'):], '&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwj01vOQjMaAAxUuwjgGHTpHAM0QguUECNoJ&usg=AOvVaw1QYhQY12vJoug4QjRVHsFK')
            final_url = f"https://www.google.com{med_url}"
            url_list.append(final_url)
    final_name = []
    for it in bsr.select(".Lq5OHe .EI11Pd h3"):
        # print(it.text)
        # final_accuracy.append(accuracy_for_pro)
        final_name.append(it.text)
    # print('uniscrapable')
    max_accurate = len(pro_name.split())
    # for word in product_string_cal:
        #     if word in it.text:
        #         accuracy_for_pro += 1

    try:
        for n in range(len(final_name)):
            accuracy_number = 0
            for word in final_name[n].split():
                if word in pro_name:
                    accuracy_number += 0.5
                else:
                    accuracy_number -= 0.01
            lower_pro_name = []
            for upper_word in pro_name.split():
                lower_pro_name.append(upper_word.lower())
            if str(final_name[n].split()[0]).lower() in lower_pro_name and 'amazon.com' in url_list[n]:
                final_list_of_google.append(
                    {"accuracy number": accuracy_number, 'Price': final_prices[n], 'Product Name': final_name[n]
                        , 'Url for the product': url_list[n], 'Max_accurate': max_accurate, "origal product name": pro_name})

    # final_list_of_google.append({"accuracy number": accuracy_number, "name of the product": name, "price of the product": price, "url for the product": url,})
    except:
        print('npo')
    real_final_list = sorted(final_list_of_google, key=lambda i: i['accuracy number'], reverse=True)
    print(real_final_list)
    print(len(real_final_list))
    if len(real_final_list) > 5:
        real_final_list = real_final_list[0:5]
    elif len(real_final_list) > 4:
        real_final_list = real_final_list[0:4]
    elif len(real_final_list) > 3:
        real_final_list = real_final_list[0:3]
    elif len(real_final_list) > 2:
        real_final_list = real_final_list[0:2]
    elif len(real_final_list) > 1:
        real_final_list = real_final_list[0:1]
    else:
        print("no element")

    if len(real_final_list) != 0:
        df = pandas.DataFrame(real_final_list)
        df.to_csv('final list of amazon product.csv')

    # print('Unit unscrapable')


#
#
#
#
#
#
#
#
#
#
#
#
#
final_last_google_search_all_pro = []
for pro_name in product_names_list:
    final_search_results = []
    search_results = []
    name_of_pro = pro_name
    pro_accurate_per = []

    for item in name_of_pro.split():
        pro_accurate_per.append(item.lower())
    # price_on_amazon = pro_price
    q=str(pro_name).replace(" ", "+").replace(":", "%3A").replace(",", "%2C").replace("&", "%26")
    header_1 = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-User": "?1",
        "Referer": "https://www.google.com",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(user_agents)
    }
    time.sleep(random.randint(2, 4))
    try:
        resp = session.get(f'https://www.google.com/search?channel=fs&client=ubuntu-sn&q={q}+amazon.com', headers=header_1, timeout=4, proxies=random.choice(proxie))#, auth=auth), proxies=proxie
        print("sent req page1")
        bs = BeautifulSoup(resp.text, 'html.parser')
        for name in bs.select(selector=".yuRUbf span a"):
            if "Translate" not in str(name) and "amazon.com" in str(name.get('href')) and "dp/" in str(name.get('href')):
                search_results.append({"Name": name.text.split('http')[0], 'Url': name.get('href')})
        print(search_results)
        print(resp.status_code)
    except:
        print('nf 1')
    page_1 = f'https://www.google.com/search?channel=fs&client=ubuntu-sn&q={q}+amazon.com'
    header_2 = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-User": "?1",
        "Referer": page_1,
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(user_agents)
    }

    header_3 = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-User": "?1",
        "Referer": f'https://www.google.com/search?q={q}+amazon.com&client=ubuntu-sn&hs=rzS&sca_esv=555852541&channel=fs&sxsrf=AB5stBg8JXVAbBf-xcdcqvIC7p8uNUQXkQ:1691747196755&ei=fAPWZOvFLbCG4-EP6ayuuAY&start=10&sa=N&ved=2ahUKEwjr89i1qdSAAxUwwzgGHWmWC2cQ8tMDegQIExAE&biw=1020&bih=968&dpr=1',
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(user_agents)
    }
    header_4 = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-User": "?1",
        "Referer": f'https://www.google.com/search?q={q}+amazon.com&client=ubuntu-sn&hs=Zv0&sca_esv=558074753&channel=fs&sxsrf=AB5stBja8BQZxodG8iW4uu6PybtVC-THfg:1692354264265&ei=2EbfZNe1D_Su4-EPopyfmAs&start=20&sa=N&ved=2ahUKEwjXgYX2_uWAAxV01zgGHSLOB7MQ8tMDegQIBBAG&biw=1846&bih=968&dpr=1',
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(user_agents)
    }
    time.sleep(random.randint(2, 4))
    try:
        resp2 = session.get(f'https://www.google.com/search?q={q}+amazon.com&client=ubuntu-sn&hs=rzS&sca_esv=555852541&channel=fs&sxsrf=AB5stBg8JXVAbBf-xcdcqvIC7p8uNUQXkQ:1691747196755&ei=fAPWZOvFLbCG4-EP6ayuuAY&start=10&sa=N&ved=2ahUKEwjr89i1qdSAAxUwwzgGHWmWC2cQ8tMDegQIExAE&biw=1020&bih=968&dpr=1',headers=header_2 , timeout=4, proxies=random.choice(proxie))#, auth=auth),proxies=proxie
        print("sent page2")
        bs2 = BeautifulSoup(resp2.text, 'html.parser')
        for name in bs2.select(selector=".yuRUbf span a"):
            if "Translate" not in str(name) and "amazon.com" in str(name.get('href')) and "dp/" in str(name.get('href')):
                # print(name.get('href'))
                search_results.append({"Name": name.text.split('http')[0], 'Url': name.get('href')})
    # print(search_results)
    except:
        print('nf 2')

    #
    # time.sleep(random.randint(2, 4))
    # # try:
    # #     resp3 = session.get(
    # #         f'https://www.google.com/search?q={q}+amazon.com&client=ubuntu-sn&hs=Zv0&sca_esv=558074753&channel=fs&sxsrf=AB5stBja8BQZxodG8iW4uu6PybtVC-THfg:1692354264265&ei=2EbfZNe1D_Su4-EPopyfmAs&start=20&sa=N&ved=2ahUKEwjXgYX2_uWAAxV01zgGHSLOB7MQ8tMDegQIBBAG&biw=1846&bih=968&dpr=1',headers=header_3, timeout=4, proxies=random.choice(proxie))#, auth=auth), proxies=proxie
    # #     bs3 = BeautifulSoup(resp3.text, 'html.parser')
    # #     for name in bs3.select(selector=".yuRUbf span a"):
    # #         if "Translate" not in str(name) and "amazon.com" in str(name.get('href')) and "dp/" in str(name.get('href')):
    # #             # print(name.get('href'))
    # #             search_results.append({"Name": name.text.split('http')[0], 'Url': name.get('href')})
    # #     print('sent req 3')
    # # except:
    # #     print('nf 32')
    # # print(search_results)
    # # time.sleep(random.randint(2, 4))
    # # try:
    # #     resp4 = session.get(f'https://www.google.com/search?q={q}+amazon.com&client=ubuntu-sn&hs=hv0&sca_esv=558074753&channel=fs&sxsrf=AB5stBgqbj-dSSVRuvxRQZqtoCuIu1yN4g:1692354272273&ei=4EbfZNGMEKCq4-EP6-mI2A0&start=30&sa=N&ved=2ahUKEwjR_O35_uWAAxUg1TgGHes0Ats4FBDy0wN6BAgEEAk&biw=1846&bih=968&dpr=1', headers=header_4, timeout=4, proxies=random.choice(proxie))#, auth=auth), proxies=proxie
    # #     bs4l = BeautifulSoup(resp4.text, 'html.parser')
    # #     for name in bs4l.select(selector=".yuRUbf span a"):
    # #         if "Translate" not in str(name) and "amazon.com" in str(name.get('href')) and "dp/" in str(name.get('href')):
    # #             # print(name.get('href'))
    # #             search_results.append({"Name": name.text.split('http')[0], 'Url': name.get('href')})
    # #     print('sendt req 4')
    # # except:
    # #     print('nf page 4')
    # #     pass
    # print(search_results)
    time.sleep(random.randint(2, 4))
    # print(bs.text)
    # print(len(bs.select(selector=".yuRUbf a")))
    # print(len(search_results))
    for item in search_results:
        cal_of_pro = 0
        for word in pro_accurate_per:
            # print(word)
            if word.lower() in item['Name'].lower().split() and cal_of_pro < len(pro_accurate_per):
                cal_of_pro += 1
            else:
                cal_of_pro -= 0.01
        lower_name = []
        for name_ow in item['Name'].split():
            lower_name.append(name_ow.lower())
        # print(item['Name'].split()[0].lower())
        # print(lower_name)
        # print(lower_name[0], "=============================", item["Name"].lower())
        if lower_name[0] in item['Name'].lower():
            # print('if statement correct line 349')
            final_search_results.append({"Real name": name_of_pro, "Name of Product": item['Name'], "Url of the product": item["Url"], "Accurate Percent": (cal_of_pro / len(pro_accurate_per)) * 100, "max words": len(pro_accurate_per), "Match words": cal_of_pro})
            last_search_results = sorted(final_search_results, key=lambda i: i["Accurate Percent"], reverse=True)
        else:
            pass
            # last_search_results = []
            # last_search_results = sorted(final_search_results, key=lambda i: i["Accurate Percent"]]
    # print('last serarch res ', last_search_results)
    final_last_google_search_all_pro.extend(last_search_results)

# print(last_search_results)
print('+++++++++++++++++++++DOMFKDSNFKM')
# final_result_of_csv = []
# for item in last_search_results[-1]:
    # final_result_of_csv.append(item)

final_df = pandas.DataFrame(final_last_google_search_all_pro)
final_df.to_csv('final_google.csv')
# except:
# print('no ifle')