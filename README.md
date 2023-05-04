# BiliBili_Private_Msg
哔哩哔哩私信私信导出工具，同时支持导出已经被撤回的/无法查看的消息（不包含私信存档）

## 环境
环境：.NET Framework 4.0 <br />

### 操作
 1.运行exe<br />
 2.通过游览器F12查看自己的Cookie，填入Cookie<br />
 3.选择类型，需要导出的消息是私信还是应援团<br />
 4.填入对方的UID或MID，如下图，导出与哔哩哔哩UP主执事的聊天记录，则填235555226<br />
![MID](https://www.z4a.net/images/2022/06/03/QQ20220603000417.png)
 5.点击导出，当提示成功即可在exe所在的文件夹找到TXT文件
 
### 思路/博客/其他
* 关于该API的详情请见 [哔哩哔哩-API收集整理](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/message/private_msg.md)
* 思路等请见[博客](https://hd80606b.com/bilibili-message/)<br />
* 在V1.1.0中添加了新的参数从根本上修正了只返回前200条消息的问题，同时追加了python版本
* ~~你问我为什么要放打包文件，因为单放exe文件会报不安全~~
* ~~远古代码，为什么还是4.0？为什么当初没有做成控制台应用？如果可以的话你帮我回到过去问问他怎么想的~~
* 本人B站UID：2239814，如您觉得提issue太麻烦，可直接B站私信我
