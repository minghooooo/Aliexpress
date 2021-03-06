import requests
from bs4 import BeautifulSoup
import re
import csv
import os

def getHTML(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'cookie': 'ali_apache_id=11.180.122.166.1581519957537.209784.0; cna=EeN/FGEqfmQCAXhVmboVPGzi; _bl_uid=OakRk65Fjytg6j5q0iahqj3v8305; _ga=GA1.2.1616301780.1581519965; aep_common_f=9dwRdEhrgxNHYuoAg4wh58vRegJR9pkGMwuo4sMB+xML00AcfiRiRA==; aeu_cid=8b121b753a804d22a6d20ce0c3479f72-1582458008876-00322-UneMJZVf; _gac_UA-17640202-1=1.1582458010.Cj0KCQiA4sjyBRC5ARIsAEHsELHszpXtYkiX6tL_T7cAmMzTjMlS5rAI5Co034gTV2FeKJjHwZp-bEIaAsxKEALw_wcB; intl_locale=en_US; _gid=GA1.2.29437168.1584242381; havana_tgc=eyJjcmVhdGVUaW1lIjoxNTg0MjQyMzg3NDExLCJsYW5nIjoiZW5fVVMiLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDc0NTM5NTE4NDYsInRndElkIjoiMU9adGpqSWgzcWl1QTlyUEdQXzQzbmcifX19fQ; _hvn_login=13; aep_usuc_t=ber_l=A0; xman_f=R2dvfsZ8v5Gtbazi0vRKmlM+bNPnNPILDS4mjVgCVk6hxSXxcJG5ynKUrqkVSVmf3wf51s1MZ5N9ByJ5zwsCq2w0eDBP974CqtY4nEGjb53N2kZicS6RGYJLW8UcPQnMB2k0JC//K627scaXgQSnKXPRzX5vztWpVzX96XgQDCKUwQasqYfA1LPLnVEMyI9UVpLvmtv/5pBckyV4Ils+NgGQAg/gwXXfH4Q9ot1gIF9zsEgv/k+c7fDRVTA4wFtGGsLp2qM7iStarTS6wg892jfzkLbu5Fa+PaVEnzUBBZnRAPzEcZHdTOQDfgr1luTNxht1+CaXDFFxEfqkVoCKK+Z9lQP0jLREjG5PzhfEmdNaS0J+gabKX4c/RHGjTjl+wdzauBtDUCWEwaZE25PNwSkcreus+XB75rLXJR8fHMg=; aep_usuc_f=site=glo&aep_cet=mobile&c_tp=USD&x_alimid=1864402296&isb=y&region=CN&b_locale=en_US; ali_apache_tracktmp=W_signed=Y; aefeMsite=amp-YtVGiyFyiWWfyvy9t3xiug; AMP_ECID_GOOGLE=amp-WsJ5Zs1IflFJIn7v5wr-fA; amp-user-notification=amp-uXrNxB5xkz1WvnbJGIfh1g; _mle_tmp_enc0=Ey%2Fp8LswzxA3J47VsqxI%2B8a4Ym8kyO048TcXvlTUNL3ont1FCe43ZypV%2FXvLbNDjJY%2BHJigJtty6GgUQbSwkhxuuehzwE2OqLg8pniQziHvkDpEtN9mjY07ri5vLULe8; XSRF-TOKEN=46353a7a-37b2-49c2-9e34-6f58a2488d9a; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%094000359918533%094000336779543%094000432861690%094000336779543%094000029798367%094000623210877%094000418807267%094000170650077; ali_apache_track=mt=1|mid=cn264982305xzqae; acs_usuc_t=x_csrf=11kms9t1c6e4c&acs_rt=2c9314ba18144e63b7256fb29a65c2fb; xman_t=BDLs4TeibjMhjrrHpm4KmOlzfXzyu79mxdCCdrttXtFNMoRzshQNdlPTJW5+23Es; _m_h5_tk=4485237517ad78fbbedc28d8ba36b84b_1584254382535; _m_h5_tk_enc=0ca2a961e1db24d83a78e1b61514ddcf; intl_common_forever=Iw+wun2O+dg6bb3ywQ3BovXCDvZW676vfuZ13ElNS/ArINfYjGXVwQ==; JSESSIONID=8EADD76023E731B17CD7D0A3CA61DE4C; xman_us_f=x_l=1&x_locale=en_US&no_popup_today=n&x_c_chg=0&x_user=CN|CN|shopper|ifm|1864402296&zero_order=y&acs_rt=aa037bc8e2dd4bcbb6928671dc4d4ec3&last_popup_time=1582390416806&x_as_i=%7B%22aeuCID%22%3A%228b121b753a804d22a6d20ce0c3479f72-1582458008876-00322-UneMJZVf%22%2C%22affiliateKey%22%3A%22UneMJZVf%22%2C%22channel%22%3A%22PREMINUM%22%2C%22cv%22%3A%222%22%2C%22isCookieCache%22%3A%22N%22%2C%22ms%22%3A%220%22%2C%22pid%22%3A%22178094261%22%2C%22src%22%3A%22aaf%22%2C%22tagtime%22%3A1582458008876%7D; _gat=1; l=dBT2-SdqQYx7593SBOfwdASWsybOVIOb4mVy7qjn4ICP_JfH5GvFWZqCbC8MCnhNHsCDR354uljQBeYBqCcYIM3IER3U7LMSndC..; isg=BAcHaGmfFfPiV5FW3XNs3FRklrvRDNvuyhAX6Nn1DBa8SCcK4dwiPkUC6wAWnLNm'
    }
    try:
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return "exception"

def parseGoodsHTML(Alist, neededDepth):
    for A in Alist:
        for a in A:
            print("type = %s %s" % (type(a), a))
            dir = os.path.join(os.curdir, a.string)
            if not os.path.isdir(dir):
                os.makedirs(dir)
            GLs = []  # 存放每个类商品信息，每爬完一个类就清空
            aHTML = getHTML('https:'+a['href'])  # 进入分类html
            # 用正则抓取商品名"title"以及"productDetailUrl"存放进临时list变量
            depth = 1
            while depth <= neededDepth:
                if depth == 1:
                    GoodsNames = re.findall(
                        r'"title":"([\w/?=\\\-&,\s#\']+)"', aHTML)
                    GoodsUrls = re.findall(
                        r'"productDetailUrl":"//([\w/?=\\\-&,\s#\'\.]+)"', aHTML)
                    soup1 = BeautifulSoup(aHTML, 'html.parser')
                    linkToNext = soup1.find('link', attrs={'rel': 'next'})

                    NextUrl = linkToNext['href']
                else:
                    GoodsNames = re.findall(r'\"title\":\".+\"', nextpageHTML)
                    GoodsUrls = re.findall(
                        r'\"productDetailUrl\":\".+\"', nextpageHTML)
                    soup2 = BeautifulSoup(nextpageHTML, 'html.parser')
                    linkToNext = soup2.find('link', attrs={'rel': 'next'})
                    NextUrl = linkToNext['href']
                for i in range(len(GoodsNames)):
                    hrefDic = {}
                    hrefDic['name'] = GoodsNames[i]
                    hrefDic['url'] = GoodsUrls[i]
                    # 进入"productDetailUrl"
                    parseGoods(hrefDic['url'], GLs, dir)
            nextpageHTML = NextPage(NextUrl)  # 判断是否爬取完当页商品，爬完则在aHTML中获取下一页url
            depth = depth+1
            # 爬完这一页的商品后，保存成csv，用类名
            GoodsHeader = {'price', 'name', 'like',
                           'comments', 'tradecount', 'star'}
            # dir = os.path.join(os.curdir, a.string)
            # if not os.path.isdir(dir):
            #     os.makedirs(dir)
            file_dir = os.path.join(dir, a.string + '.csv')
            with open(file_dir, 'w', newline='') as fp:
                writer = csv.DictWriter(fp, GoodsHeader)
                writer.writeheader()
                writer.writerows(GLs)
        # 保存html文件

def parseHTML(html):
    AList = []
    soup = BeautifulSoup(html, 'html.parser')
    uls = soup.find_all('ul', attrs={'class': 'sub-item-cont util-clearfix'})
    for ul in uls:
        As = ul.find_all('a')
        AList.append(As)
    return AList

def parseGoods(url, list, dir):

    header = {
        # need refer
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'cookie': 'ali_apache_id=11.180.122.166.1581519957537.209784.0; cna=EeN/FGEqfmQCAXhVmboVPGzi; _bl_uid=OakRk65Fjytg6j5q0iahqj3v8305; _ga=GA1.2.1616301780.1581519965; aep_common_f=9dwRdEhrgxNHYuoAg4wh58vRegJR9pkGMwuo4sMB+xML00AcfiRiRA==; aeu_cid=8b121b753a804d22a6d20ce0c3479f72-1582458008876-00322-UneMJZVf; _gac_UA-17640202-1=1.1582458010.Cj0KCQiA4sjyBRC5ARIsAEHsELHszpXtYkiX6tL_T7cAmMzTjMlS5rAI5Co034gTV2FeKJjHwZp-bEIaAsxKEALw_wcB; intl_locale=en_US; _gid=GA1.2.29437168.1584242381; havana_tgc=eyJjcmVhdGVUaW1lIjoxNTg0MjQyMzg3NDExLCJsYW5nIjoiZW5fVVMiLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDc0NTM5NTE4NDYsInRndElkIjoiMU9adGpqSWgzcWl1QTlyUEdQXzQzbmcifX19fQ; _hvn_login=13; aep_usuc_t=ber_l=A0; xman_f=R2dvfsZ8v5Gtbazi0vRKmlM+bNPnNPILDS4mjVgCVk6hxSXxcJG5ynKUrqkVSVmf3wf51s1MZ5N9ByJ5zwsCq2w0eDBP974CqtY4nEGjb53N2kZicS6RGYJLW8UcPQnMB2k0JC//K627scaXgQSnKXPRzX5vztWpVzX96XgQDCKUwQasqYfA1LPLnVEMyI9UVpLvmtv/5pBckyV4Ils+NgGQAg/gwXXfH4Q9ot1gIF9zsEgv/k+c7fDRVTA4wFtGGsLp2qM7iStarTS6wg892jfzkLbu5Fa+PaVEnzUBBZnRAPzEcZHdTOQDfgr1luTNxht1+CaXDFFxEfqkVoCKK+Z9lQP0jLREjG5PzhfEmdNaS0J+gabKX4c/RHGjTjl+wdzauBtDUCWEwaZE25PNwSkcreus+XB75rLXJR8fHMg=; aep_usuc_f=site=glo&aep_cet=mobile&c_tp=USD&x_alimid=1864402296&isb=y&region=CN&b_locale=en_US; ali_apache_tracktmp=W_signed=Y; aefeMsite=amp-YtVGiyFyiWWfyvy9t3xiug; AMP_ECID_GOOGLE=amp-WsJ5Zs1IflFJIn7v5wr-fA; amp-user-notification=amp-uXrNxB5xkz1WvnbJGIfh1g; _mle_tmp_enc0=Ey%2Fp8LswzxA3J47VsqxI%2B8a4Ym8kyO048TcXvlTUNL3ont1FCe43ZypV%2FXvLbNDjJY%2BHJigJtty6GgUQbSwkhxuuehzwE2OqLg8pniQziHvkDpEtN9mjY07ri5vLULe8; XSRF-TOKEN=46353a7a-37b2-49c2-9e34-6f58a2488d9a; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%094000359918533%094000336779543%094000432861690%094000336779543%094000029798367%094000623210877%094000418807267%094000170650077; ali_apache_track=mt=1|mid=cn264982305xzqae; acs_usuc_t=x_csrf=11kms9t1c6e4c&acs_rt=2c9314ba18144e63b7256fb29a65c2fb; xman_t=BDLs4TeibjMhjrrHpm4KmOlzfXzyu79mxdCCdrttXtFNMoRzshQNdlPTJW5+23Es; _m_h5_tk=4485237517ad78fbbedc28d8ba36b84b_1584254382535; _m_h5_tk_enc=0ca2a961e1db24d83a78e1b61514ddcf; intl_common_forever=Iw+wun2O+dg6bb3ywQ3BovXCDvZW676vfuZ13ElNS/ArINfYjGXVwQ==; JSESSIONID=8EADD76023E731B17CD7D0A3CA61DE4C; xman_us_f=x_l=1&x_locale=en_US&no_popup_today=n&x_c_chg=0&x_user=CN|CN|shopper|ifm|1864402296&zero_order=y&acs_rt=aa037bc8e2dd4bcbb6928671dc4d4ec3&last_popup_time=1582390416806&x_as_i=%7B%22aeuCID%22%3A%228b121b753a804d22a6d20ce0c3479f72-1582458008876-00322-UneMJZVf%22%2C%22affiliateKey%22%3A%22UneMJZVf%22%2C%22channel%22%3A%22PREMINUM%22%2C%22cv%22%3A%222%22%2C%22isCookieCache%22%3A%22N%22%2C%22ms%22%3A%220%22%2C%22pid%22%3A%22178094261%22%2C%22src%22%3A%22aaf%22%2C%22tagtime%22%3A1582458008876%7D; _gat=1; l=dBT2-SdqQYx7593SBOfwdASWsybOVIOb4mVy7qjn4ICP_JfH5GvFWZqCbC8MCnhNHsCDR354uljQBeYBqCcYIM3IER3U7LMSndC..; isg=BAcHaGmfFfPiV5FW3XNs3FRklrvRDNvuyhAX6Nn1DBa8SCcK4dwiPkUC6wAWnLNm'
    }
    header['refer'] = str(url)
    try:
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # return r.text
        html = r.text
    except:
        return "exception"

    # 用正则去获取商品信息
    # href = re.match(r'"detailPageUrl":"//([\w$\s\.-/]+)"', html)
    # title = re.match(r'"title":"([\w./?=\-&,\s]+)"', html)  # 商品名称
    # like = re.match(r'"itemWishedCount":([\d]+)', html)  # 收藏数
    # comments = re.match(r'"totalValidNum":(\d+)', html)  # 评论数
    # star = re.match(r'"averageStar":(\d+\.\d*)', html)  # 星级
    # tradeCount = re.match(r'"tradeCount":(\d+)', html)  # 订单数、
    # price = re.match(r'"formatedActivityPrice":"(US\s\$\d+\.\d+\s-\s\d+\.\d+)"', html)  # 价格
    product = {}
    product['href'] = re.match(r'"detailPageUrl":"//([\w$\s\.-/]+)"', html)
    product['title'] = re.match(r'"title":"([\w./?=\-&,\s]+)"', html)  # 商品名称
    product['like'] = re.match(r'"itemWishedCount":([\d]+)', html)  # 收藏数
    product['comments'] = re.match(r'"totalValidNum":(\d+)', html)  # 评论数
    product['star'] = re.match(r'"averageStar":(\d+\.\d*)', html)  # 星级
    product['tradeCount'] = re.match(r'"tradeCount":(\d+)', html)  # 订单数、
    product['price'] = re.match(r'"formatedActivityPrice":"(US\s\$\d+\.\d+\s-\s\d+\.\d+)"', html)  # 价格
    list.append(product)
    file_dir1 = os.path.join(dir, product['title']+'.html')
    with open(file_dir1, 'wb') as fp1:
        fp1.write(html)
    return list

def NextPage(url):
    # 获取下一页
    header = {
        # need refer
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'cookie': 'ali_apache_id=11.180.122.166.1581519957537.209784.0; cna=EeN/FGEqfmQCAXhVmboVPGzi; _bl_uid=OakRk65Fjytg6j5q0iahqj3v8305; _ga=GA1.2.1616301780.1581519965; aep_common_f=9dwRdEhrgxNHYuoAg4wh58vRegJR9pkGMwuo4sMB+xML00AcfiRiRA==; aeu_cid=8b121b753a804d22a6d20ce0c3479f72-1582458008876-00322-UneMJZVf; _gac_UA-17640202-1=1.1582458010.Cj0KCQiA4sjyBRC5ARIsAEHsELHszpXtYkiX6tL_T7cAmMzTjMlS5rAI5Co034gTV2FeKJjHwZp-bEIaAsxKEALw_wcB; intl_locale=en_US; _gid=GA1.2.29437168.1584242381; havana_tgc=eyJjcmVhdGVUaW1lIjoxNTg0MjQyMzg3NDExLCJsYW5nIjoiZW5fVVMiLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDc0NTM5NTE4NDYsInRndElkIjoiMU9adGpqSWgzcWl1QTlyUEdQXzQzbmcifX19fQ; _hvn_login=13; aep_usuc_t=ber_l=A0; xman_f=R2dvfsZ8v5Gtbazi0vRKmlM+bNPnNPILDS4mjVgCVk6hxSXxcJG5ynKUrqkVSVmf3wf51s1MZ5N9ByJ5zwsCq2w0eDBP974CqtY4nEGjb53N2kZicS6RGYJLW8UcPQnMB2k0JC//K627scaXgQSnKXPRzX5vztWpVzX96XgQDCKUwQasqYfA1LPLnVEMyI9UVpLvmtv/5pBckyV4Ils+NgGQAg/gwXXfH4Q9ot1gIF9zsEgv/k+c7fDRVTA4wFtGGsLp2qM7iStarTS6wg892jfzkLbu5Fa+PaVEnzUBBZnRAPzEcZHdTOQDfgr1luTNxht1+CaXDFFxEfqkVoCKK+Z9lQP0jLREjG5PzhfEmdNaS0J+gabKX4c/RHGjTjl+wdzauBtDUCWEwaZE25PNwSkcreus+XB75rLXJR8fHMg=; aep_usuc_f=site=glo&aep_cet=mobile&c_tp=USD&x_alimid=1864402296&isb=y&region=CN&b_locale=en_US; ali_apache_tracktmp=W_signed=Y; aefeMsite=amp-YtVGiyFyiWWfyvy9t3xiug; AMP_ECID_GOOGLE=amp-WsJ5Zs1IflFJIn7v5wr-fA; amp-user-notification=amp-uXrNxB5xkz1WvnbJGIfh1g; _mle_tmp_enc0=Ey%2Fp8LswzxA3J47VsqxI%2B8a4Ym8kyO048TcXvlTUNL3ont1FCe43ZypV%2FXvLbNDjJY%2BHJigJtty6GgUQbSwkhxuuehzwE2OqLg8pniQziHvkDpEtN9mjY07ri5vLULe8; XSRF-TOKEN=46353a7a-37b2-49c2-9e34-6f58a2488d9a; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%094000359918533%094000336779543%094000432861690%094000336779543%094000029798367%094000623210877%094000418807267%094000170650077; ali_apache_track=mt=1|mid=cn264982305xzqae; acs_usuc_t=x_csrf=11kms9t1c6e4c&acs_rt=2c9314ba18144e63b7256fb29a65c2fb; xman_t=BDLs4TeibjMhjrrHpm4KmOlzfXzyu79mxdCCdrttXtFNMoRzshQNdlPTJW5+23Es; _m_h5_tk=4485237517ad78fbbedc28d8ba36b84b_1584254382535; _m_h5_tk_enc=0ca2a961e1db24d83a78e1b61514ddcf; intl_common_forever=Iw+wun2O+dg6bb3ywQ3BovXCDvZW676vfuZ13ElNS/ArINfYjGXVwQ==; JSESSIONID=8EADD76023E731B17CD7D0A3CA61DE4C; xman_us_f=x_l=1&x_locale=en_US&no_popup_today=n&x_c_chg=0&x_user=CN|CN|shopper|ifm|1864402296&zero_order=y&acs_rt=aa037bc8e2dd4bcbb6928671dc4d4ec3&last_popup_time=1582390416806&x_as_i=%7B%22aeuCID%22%3A%228b121b753a804d22a6d20ce0c3479f72-1582458008876-00322-UneMJZVf%22%2C%22affiliateKey%22%3A%22UneMJZVf%22%2C%22channel%22%3A%22PREMINUM%22%2C%22cv%22%3A%222%22%2C%22isCookieCache%22%3A%22N%22%2C%22ms%22%3A%220%22%2C%22pid%22%3A%22178094261%22%2C%22src%22%3A%22aaf%22%2C%22tagtime%22%3A1582458008876%7D; _gat=1; l=dBT2-SdqQYx7593SBOfwdASWsybOVIOb4mVy7qjn4ICP_JfH5GvFWZqCbC8MCnhNHsCDR354uljQBeYBqCcYIM3IER3U7LMSndC..; isg=BAcHaGmfFfPiV5FW3XNs3FRklrvRDNvuyhAX6Nn1DBa8SCcK4dwiPkUC6wAWnLNm'
    }
    header['refer'] = str(url)
    try:
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "NextPageException"

if __name__ == "__main__":
    neededDepth = 10
    urlOfC = 'https://www.aliexpress.com/all-wholesale-products.html'
    html = getHTML(urlOfC)
    ListOfClass = parseHTML(html)
    parseGoodsHTML(ListOfClass, neededDepth)



