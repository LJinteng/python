import requests
import re
import json
import pprint
import csv
import os
path="拉勾岗位信息获取"
if not os.path.exists(path):
    os.mkdir(path)
Post=input("请输入查询岗位>>>")
f=open(path+"/"+f"{Post}相关岗位信息.csv","w",encoding="UTF-8")
csv_write=csv.writer(f)
csv_write.writerow(["职位","薪资","工作时间","公司","工作地点","所在城市"])
n=int(input("请输入获取页数(30页以内)>>>"))
for i in range(1,n+1):
    url=f"https://www.lagou.com/wn/jobs?pn={i}&fromSearch=true&kd={Post}"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        # "Cookie": "RECOMMEND_TIP=true; user_trace_token=20221229135941-d8e43f01-c6cf-448c-9b0f-eefcf9cc9646; LGUID=20221229135941-ef95d82b-bb74-422b-8266-f29578e1c83c; _ga=GA1.2.490307107.1672293582; sajssdk_2015_cross_new_user=1; _gid=GA1.2.968309043.1672293582; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; __lg_stoken__=7f20c2baec391fd872a9ed660accdefc80b0bb2fdcdb120cc421ae8088b6132c2d8c4d0d401f131af431a6924e47d8af16e28c7de03276742f754c6a7f85c3bcdfdedaa2075c; PRE_HOST=www.baidu.com; _gat=1; LGSID=20221229174117-194a6468-82bc-40d1-bbaa-3537e3893d1b; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.060000jYAOcGJIMt0-Fu72HEnf-dkj%5FmLJlUOxl6vRc1-FlQP%5Fh4LBrZEwEshH2ETanh3d2hXWXTjcOfGWoq4VG0mUSsw3uqD5nL8aD398GqQeok1ybLwk4dHdmoGvlqyy5YNhECV0B6Ijz3GP2tPI58DDlN-m2g-3i-z6sUMTFlLFHHVcayJgiOOuKRh7mIW1r1OSJxLiSMpf8P1kAjZZjZMTL3.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4V0KdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujL0oUhY0ZFWIWYs0ZNzU7qGujYkPHfknWc4n1T40Addgv-b5HDdnjR4P1Ds0AdxpyfqnHD3rjndrHR0UgwsU7qGujYknW6zP6KsI-qGujYs0A-bm1dcHbD0TA-b5Hf0mv-b5HDsrfKWThnqnH0dnjD%26dt%3D1672306874%26wd%3D%25E6%258B%2589%25E5%258B%25BE%26tpl%3Dtpl%5F12826%5F30685%5F0%26l%3D1541229379%26us%3DlinkVersion%253D1%2526compPath%253D10036.0-10032.0%2526label%253D%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkType%253D%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; JSESSIONID=ABAAAECABIEACCA14A7F269DEF357903A3515581F5A12A6; WEBTJ-ID=20221229174437-1855d44f1f4641-0a5d28b201dad7-26021151-1327104-1855d44f1f5949; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1672293582,1672307078; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1672307078; sensorsdata2015session=%7B%7D; TG-TRACK-CODE=index_search; LGRID=20221229174443-29fbcb1c-220b-4b5b-ab41-0ba0cba7f295; X_HTTP_TOKEN=fb0126cc6ccebc143807032761ef66d0880c10050f; X_MIDDLE_TOKEN=f5c212d6030d8b0cb53580fca9b0f3b9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221855c770655a7f-0a3b1c6c3e3a1b-26021151-1327104-1855c770656bc1%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22108.0.0.0%22%7D%2C%22%24device_id%22%3A%221855c770655a7f-0a3b1c6c3e3a1b-26021151-1327104-1855c770656bc1%22%7D"
        "Cookie": "RECOMMEND_TIP=true; user_trace_token=20221229135941-d8e43f01-c6cf-448c-9b0f-eefcf9cc9646; LGUID=20221229135941-ef95d82b-bb74-422b-8266-f29578e1c83c; _ga=GA1.2.490307107.1672293582; sajssdk_2015_cross_new_user=1; _gid=GA1.2.968309043.1672293582; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; __lg_stoken__=7f20c2baec391fd872a9ed660accdefc80b0bb2fdcdb120cc421ae8088b6132c2d8c4d0d401f131af431a6924e47d8af16e28c7de03276742f754c6a7f85c3bcdfdedaa2075c; PRE_UTM=; LGSID=20221229202646-70f8456b-5fa1-47c8-ba60-60d7f34257dc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DMQI7clfqB63lDo4s8Dl0N6ZXTOcKmQIzgURBzrcemTq%26wd%3D%26eqid%3Dd07a27ed0001ac3e0000000663ad6180; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; gate_login_token=v1####f1de85125d75a5b2756fd9ceca447b54c3536812f459c1dfd8d9061ea440a0ce; LG_HAS_LOGIN=1; hasDeliver=0; __SAFETY_CLOSE_TIME__25596720=1; WEBTJ-ID=20221229205531-1855df3b828825-084ea61f072216-26021151-1327104-1855df3b829ec7; JSESSIONID=ABAAABAABAGABFAFF72B977A0DA23AABCD4C0990C1D76C2; sensorsdata2015session=%7B%7D; _putrc=5F0D017833F5C079123F89F2B170EADC; login=true; unick=%E7%94%A8%E6%88%B77979; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; X_HTTP_TOKEN=fb0126cc6ccebc145658132761ef66d0880c10050f; _gat=1; LGRID=20221229205605-193c70fc-5927-426b-bcf9-1f0bf28eb38d; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1672307078,1672316943,1672317728,1672318567; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1672318567; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2225596720%22%2C%22first_id%22%3A%221855c770655a7f-0a3b1c6c3e3a1b-26021151-1327104-1855c770656bc1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22108.0.0.0%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%221855c770655a7f-0a3b1c6c3e3a1b-26021151-1327104-1855c770656bc1%22%7D; TG-TRACK-CODE=index_search"
    }
    response=requests.get(url=url,headers=headers)
    # print(response)
    # print(response.text)
    html_data=re.findall('<script id="__NEXT_DATA__" type="application/json">(.*?)</script',response.text)[0]
    # print(html_data)
    json_data=json.loads(html_data)
    # print(json_data)
    # pprint.pprint(json_data)
    result_data=json_data['props']['pageProps']['initData']['content']['positionResult']['result']
    # pprint.pprint(result_data)
    for index in result_data:
        # pprint.pprint(index)
        # dit={
        #     "职位":index['positionName'],
        #     "薪资": index['salary'],
        #     "工作时间":index['workYear'],
        #     "公司": index['companyFullName'],
        #     "工作地点":index['positionAddress'],
        #     "所在城市": index['city'],
        # }
        # print(dit)
        csv_write.writerow([index['positionName'],index['salary'],index['workYear'],index['companyFullName'],index['positionAddress'],index['city']])
    print(f"---第{i}页获取完毕！---")
print(f'---{Post}岗位信息获取完毕---')
f.close()