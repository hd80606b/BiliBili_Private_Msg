import requests
import json
import datetime
import time
import os

def timestamp_to_datetime(unix_timestamp):
    start_time = datetime.datetime(1970, 1, 1).replace(tzinfo=datetime.timezone.utc)
    dt = start_time + datetime.timedelta(seconds=unix_timestamp)
    local_dt = dt.astimezone(datetime.timezone(datetime.timedelta(hours=8))) # 当地时区
    local_dt_str = local_dt.strftime('%Y/%m/%d %H:%M:%S:%f')
    local_dt_str = local_dt_str[:-7]
    return  local_dt_str
    
def extract_content(data):
    try:
        content_data = json.loads(data)
        if isinstance(content_data, dict) and "content" in content_data:
            return content_data["content"]
        else:
            return data
    except json.JSONDecodeError:
        return data
       
param1 = input("请输入Cookie: ")
end_list = 0
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
talker_ids = []  # 用于存储提取的talker_id
talker_names = []  # 用于存储talker_id对应的昵称
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # 获取当前时间作为文件夹名
folder_path = os.path.join(".", current_time)  # 当前目录

# 拿列表
while(1):
    url = "https://api.vc.bilibili.com/session_svr/v1/session_svr/get_sessions?session_type=1&group_fold=1&unfollow_fold=0&sort_rule=2&end_ts="+str(end_list)+"&build=0&mobi_app=web&size=200"
    response = requests.get(url, cookies=cookies, headers=headers)
    # 解析JSON数据
    parsed_data = json.loads(response.text)
    List_messages = parsed_data["data"]["session_list"]
    if not List_messages:
        break
    for session in List_messages:#获取talker_id和talker_name
        talker_id = session["talker_id"]
        talker_ids.append(talker_id)
        url = "https://api.vc.bilibili.com/account/v1/user/cards?uids=" +str(talker_id)
        usersinfo_response = requests.get(url, cookies=cookies,headers=headers)
        parsed_data = json.loads(usersinfo_response.text)
        talker_names.append(parsed_data["data"][0]["name"])
    last_session = List_messages[-1]
    end_list = last_session["session_ts"]

# 创建文件夹
os.makedirs(folder_path, exist_ok=True)

# 使用保存的talker_ids进行GET请求
for talker_id,talker_name in list(zip(talker_ids, talker_names)): 
    file_name = talker_name+ '_' +str(talker_id) +".txt"
    file_path = os.path.join(folder_path, file_name)
    while(1):
        # 发送GET请求
        url = "https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs?size=200&build=0&mobi_app=web&begin_seqno=0&end_seqno="+str(end)+"&sender_device_id=1&talker_id="+ str(talker_id) + "&session_type=1"
        response = requests.get(url, cookies=cookies, headers=headers)
        # 解析JSON数据
        parsed_data = json.loads(response.text)
        new_messages = parsed_data["data"]["messages"]
        if not new_messages:
            break
        end = parsed_data["data"]["min_seqno"]
        messages.extend(new_messages)  # 将新消息添加到消息列表中
        with open(file_path, 'w', encoding='utf-8') as f:
            for message in reversed(messages):
                content = message["content"]
                if isinstance(content, int):
                    content = str(content)
                if '"content"' in content:
                    try:
                        content = json.loads(content)["content"]
                    except KeyError:                 
                        content = "default"
                else:
                    if '"text"' in content:
                        try:
                            content = json.loads(content)["text"]
                        except KeyError:
                            #print("出错行：",content)
                            content = "default"
                            #print("出错结束")
                    if '"url"' in content:
                        try:
                            content = json.loads(content)["url"]
                        except KeyError:
                            content = "default"
                    if '"bvid"' in content:
                        try:
                            content = json.loads(content).get("title", "")+","+json.loads(content)["bvid"]
                        except KeyError:
                            content = "default"                    
                content = extract_content(content)
                content = content.replace('\n', ' ')
                
                
                UID = json.loads(json.dumps(message["sender_uid"]))
                if UID == talker_id:#判断消息发送者
                    sender_name = talker_name
                else:
                    sender_name = "自己_"+ str(UID)
                Timestamp = json.loads(json.dumps(message["timestamp"]))
                f.write(str(timestamp_to_datetime(Timestamp))+'\x20'+sender_name + '说：\x20' + content + '\n')
    print("数据已保存到"+talker_name+ '_' +str(talker_id)+'.txt中')
    messages.clear()
    end = 0
    #time.sleep(2)  # 这里延时 2 秒
print("数据已全部保存完毕")
