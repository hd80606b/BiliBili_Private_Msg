using System;
using System.Collections.Generic;
using System.Linq;
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
            public long min_seqno { get; set; }
            public long max_seqno { get; set; }
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
            public long msg_key { get; set; }
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

    }
}
