import requests
import json
import datetime
import time

def timestamp_to_datetime(unix_timestamp):
    start_time = datetime.datetime(1970, 1, 1).replace(tzinfo=datetime.timezone.utc)
    dt = start_time + datetime.timedelta(seconds=unix_timestamp)
    local_dt = dt.astimezone(datetime.timezone(datetime.timedelta(hours=8))) # 当地时区
    local_dt_str = local_dt.strftime('%Y/%m/%d %H:%M:%S:%f')
    local_dt_str = local_dt_str[:-7]
    return  local_dt_str
# 用户输入两个参数
param1 = input("请输入Cookie: ")
param2 = input("请输入UID/MID: ")
end = 0
# 构造Cookie请求头
cookies = {
    "param1": param1
}

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'Origin': 'https://www.bilibili.com',
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'keep-alive'
}


messages = []  # 保存所有的消息

while(1):
    # 发送GET请求
    url = "https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs?size=200&build=0&mobi_app=web&begin_seqno=0&end_seqno="+str(end)+"&sender_device_id=1&talker_id="+ param2 + "&session_type=1"
    response = requests.get(url, cookies=cookies, headers=headers)
    # 解析JSON数据
    parsed_data = json.loads(response.text)
    #print(response.text)
    new_messages = parsed_data["data"]["messages"]
    if not new_messages:
        break
    end = parsed_data["data"]["min_seqno"]
    messages.extend(new_messages)  # 将新消息添加到消息列表中
    # # 将数据保存到文件
    # with open("data.json", "w") as file:
        # json.dump(data, file)
    with open(param2+'.txt', 'w', encoding='utf-8') as f:
        for message in reversed(messages):
            content = message["content"]
            if isinstance(content, int):
                content = str(content)
            content_json = json.loads(content)
            if isinstance(content_json, int):
                content_json = str(content_json)
            if "content" in content_json:
                content = content_json["content"]
            if "url" in content_json and "height" in content_json and "width" in content_json:
                content = f'图片：{content_json["url"]}, 高度: {content_json["height"]}, 宽度: {content_json["width"]}'
            content = content.replace('\n', ' ')

            UID = json.loads(json.dumps(message["sender_uid"]))
            Timestamp = json.loads(json.dumps(message["timestamp"]))
            f.write(str(timestamp_to_datetime(Timestamp))+'\x20'+str(UID) + '说：\x20' + content + '\n')
 
print("数据已保存到"+param2+'.txt中')
