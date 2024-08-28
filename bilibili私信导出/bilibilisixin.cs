using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace bilibili私信导出
{
    class bilibilisixin
    {

        public class Rootobject
        {
            public int code { get; set; }
            public string msg { get; set; }
            public string message { get; set; }
            public int ttl { get; set; }
            public Data data { get; set; }
        }

        public class Data
        {
            public Message[] messages { get; set; }
            public int has_more { get; set; }
            public ulong min_seqno { get; set; }
            public ulong max_seqno { get; set; }
            public E_Infos[] e_infos { get; set; }
        }

        public class Message
        {
            public long sender_uid { get; set; }
            public int receiver_type { get; set; }
            public long receiver_id { get; set; }
            public int msg_type { get; set; }
            public string content { get; set; }
            public long msg_seqno { get; set; }
            public long timestamp { get; set; }
            public int[] at_uids { get; set; }
            public ulong msg_key { get; set; }
            public int msg_status { get; set; }
            public string notify_code { get; set; }
            public int new_face_version { get; set; }
        }

        public class E_Infos
        {
            public string text { get; set; }
            public string url { get; set; }
            public int size { get; set; }
        }
        //私信内容序列化
        public class Content_content
        {
            //分享视频使用
            public string author { get; set; }
            public string headline { get; set; }
            public ulong id { get; set; }
            public int source { get; set; }
            public string thumb { get; set; }
            public string title { get; set; }
            public string bvid { get; set; }
            //pictrue使用
            public string url { get; set; }
            public int height { get; set; }
            public int width { get; set; }
            public string imageType { get; set; }
            public int original { get; set; }
            public int size { get; set; }
            //正常内容
            public string content { get; set; }
            //分享内容
            public string text { get; set; }
            public string jump_text { get; set; }
            public string jump_uri { get; set; }
            public object modules { get; set; }
            public string jump_text_2 { get; set; }
            public string jump_uri_2 { get; set; }
            public string jump_text_3 { get; set; }
            public string jump_uri_3 { get; set; }
            public object notifier { get; set; }
            public Jump_Uri_Config jump_uri_config { get; set; }
            public Jump_Uri_2_Config jump_uri_2_config { get; set; }
            public Jump_Uri_3_Config jump_uri_3_config { get; set; }
            public object biz_content { get; set; }
        }

        public class Rootobject_picture
        {
            public string url { get; set; }
            public int height { get; set; }
            public int width { get; set; }
            public string imageType { get; set; }
            public int original { get; set; }
            public int size { get; set; }
        }
        public class Rootobject_content
        {
            public string content { get; set; }
        }

        public class Jump_Uri_Config
        {
            public string all_uri { get; set; }
            public string text { get; set; }
        }

        public class Jump_Uri_2_Config
        {
            public string text { get; set; }
        }

        public class Jump_Uri_3_Config
        {
            public string text { get; set; }
        }

    }

}
