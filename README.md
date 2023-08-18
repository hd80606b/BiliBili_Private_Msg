# BiliBili_Private_Msg
哔哩哔哩私信私信导出工具，同时支持导出已经被撤回的/无法查看的消息（不包含私信存档）

## 环境
环境：.NET Framework 4.0  或 python 3.10.5<br />

### 操作
 (推荐使用python版本，最后返回的结果是正常显示的消息，而.net版未做过滤，最后会是json形式)<br />
 1.针对性导出请运行exe或使用python文件夹下的BiliBili_Private_Msg.py<br />
 BiliBili_Private_Msg(ALL).py是将整个私信列表中所有人的消息一块导出到由时间命名的文件夹中<br />
 2.通过游览器F12查看自己的Cookie，填入Cookie<br />
 3.选择类型，需要导出的消息是私信还是应援团<br />
 4.填入对方的UID或MID，如下图，导出与哔哩哔哩UP主执事的聊天记录，则填235555226<br />
![MID](https://www.z4a.net/images/2022/06/03/QQ20220603000417.png)
 5.点击导出，当提示成功或已保存文件即可在exe/py文件所在的文件夹找到对应的TXT文件（或时间文件夹）<br />
 6.(可选)如果要使用python版本导出应援团的消息，请将session_type的值设置为2
### 思路/博客/注意/其他
* 使用BiliBili_Private_Msg(ALL).py时，如果私信列表中的人数过多，请自行取消`time.sleep(2)`的注释，避免ip被ban
* 关于该API的详情请见 [哔哩哔哩-API收集整理](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/message/private_msg.md)
* 思路等请见[博客](https://hd80606b.com/bilibili-message/)<br />
* 在V1.1.0中添加了新的参数从根本上修正了只返回前200条消息的问题
* 在即将到来的V1.1.1中也会把C#版本的程序添加**一键导出私信列表中所有人的消息**的功能
* ~~你问我为什么要放打包文件，因为单放exe文件会报不安全~~
* ~~远古代码，为什么还是4.0？为什么当初没有做成控制台应用？~~ 所以在这里追加了python版本
* 本人B站UID：2239814，如您觉得提issue太麻烦，可直接B站私信我
