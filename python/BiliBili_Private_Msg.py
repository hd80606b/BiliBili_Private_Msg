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
while(1):
    # 发送GET请求
    url = "https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs?size=200&build=0&mobi_app=web&begin_seqno=0&end_seqno="+str(end)+"&sender_device_id=1&talker_id="+ param2 + "&session_type=1"
    response = requests.get(url, cookies=cookies)
    # 解析JSON数据
    parsed_data = json.loads(response.text)
    messages = parsed_data["data"]["messages"]
    if not messages:
        break
    end = parsed_data["data"]["min_seqno"]
    # # 将数据保存到文件
    # with open("data.json", "w") as file:
        # json.dump(data, file)
    with open(param2+'.txt', 'w') as f:
        for message in reversed(messages):
            content = json.loads(message["content"])["content"]
            content = content.replace('\n', ' ')
            UID = json.loads(json.dumps(message["sender_uid"]))
            Timestamp = json.loads(json.dumps(message["timestamp"]))
            f.write(str(timestamp_to_datetime(Timestamp))+'\x20'+str(UID) + '说：\x20' + content + '\n')
 
print("数据已保存到"+param2+'.txt中')
