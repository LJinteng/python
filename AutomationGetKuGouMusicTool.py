#导入包
import requests
import json
import os
# 创建文件夹
path="飘向北方合集"
if not os.path.exists(path):
    os.mkdir(path)
#伪装浏览器发送请求
headers={
"cookie": "kg_mid=a7207ad367bac23add05f5d95943fc9c; kg_dfid=3x8Boj0lYIyo27NtLT34QZYR; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1672052361,1672054847,1672060282; kg_mid_temp=a7207ad367bac23add05f5d95943fc9c; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1672061211",
"referer": "https://www.kugou.com/",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
#获取url地址
list_url="https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1672063568181&mid=a7207ad367bac23add05f5d95943fc9c&uuid=a7207ad367bac23add05f5d95943fc9c&dfid=3x8Boj0lYIyo27NtLT34QZYR&keyword=%E9%A3%98%E5%90%91%E5%8C%97%E6%96%B9&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=8fea4e44f854b2bdcfe68d4e420a76bb"
#发送请求到服务器，获取资源
list_rsq=requests.get(url=list_url,headers=headers)
#获取值
song_list=json.loads(list_rsq.text[12:-2])["data"]["lists"]
# 遍历获取的值
for i,s in enumerate(song_list):
    #获取当前歌曲url
    message_url = f"https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id={s.get('EMixSongID')}"
    message_rsq=requests.get(url=message_url,headers=headers)
    get_music_url=json.loads(message_rsq.text)
    #获取歌名
    audio_name=get_music_url['data']['audio_name']
    name1=f"{i+1}.{audio_name}"
    #去除：以及|字符否则文件无法命名
    name2=name1.replace(":","")
    name=name2.replace("|","")
    # 获取MP3文件url
    music_url=get_music_url["data"]['play_backup_url']
    music_rsq=requests.get(url=music_url,headers=headers)
    #将数据存储文件夹
    with open(path+"/"+f"{name}.mp3","wb") as f:
        f.write(music_rsq.content)
    print(f"<-----{name}.mp3 下载完毕！----->")