using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Net;
using System.Text;
using System.Web.Script.Serialization;
using System.Windows.Forms;

namespace bilibili私信导出
{
    public partial class Form1 : Form
    {
        /// <summary>
        /// 时间戳转换为DataTime
        /// </summary>
        /// <param name="unixTimeStamp"></param>
        /// <returns></returns>
        public DateTime TimestampToDataTime(long unixTimeStamp)
        {
            System.DateTime startTime = TimeZone.CurrentTimeZone.ToLocalTime(new System.DateTime(1970, 1, 1)); // 当地时区
            DateTime dt = startTime.AddSeconds(unixTimeStamp);
            System.Console.WriteLine(dt.ToString("yyyy/MM/dd HH:mm:ss:ffff"));
            return dt;
        }


        public Form1()
        {
            InitializeComponent();
        }
        public string path = Directory.GetCurrentDirectory()+@"\";
        public string session_type;
        public string text_dx;

        private void button1_Click(object sender, EventArgs e)
        {
            if(textBox1.Text == null || textBox1.Text == "")
            {
                MessageBox.Show("请先填写Cookie");
                return;
            }
            if (textBox2.Text == null || textBox2.Text == "")
            {
                MessageBox.Show("请先填写UID或MID");
                return;
            }
            if(comboBox1.Text=="私信")
            {
                session_type = "1";
            }
            else
            {
                session_type = "2";
            }

            if (File.Exists(path + textBox2.Text + ".txt"))
            {
                File.Delete(path + textBox2.Text + ".txt");
            }
            long end = 0;
            bilibilisixin.Rootobject root = new bilibilisixin.Rootobject();
            try
            {
                do
                {
                    HttpWebRequest req = (HttpWebRequest)WebRequest.Create("https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs?size=200&build=0&mobi_app=web&begin_seqno=0&end_seqno="+end+"&sender_device_id=1&talker_id=" + textBox2.Text + "&session_type=" + session_type);
                    req.Method = "GET";
                    req.Headers["Cookie"] = textBox1.Text;
                    HttpWebResponse resp = (HttpWebResponse)req.GetResponse();
                    StreamReader stream = new StreamReader(resp.GetResponseStream(), Encoding.UTF8);       
                    string result = stream.ReadToEnd();
                    if(result.Contains("null"))
                    {
                        return;
                    }
                    JavaScriptSerializer js = new JavaScriptSerializer();
                    root = js.Deserialize<bilibilisixin.Rootobject>(result);
                    if (root.code == 0)
                    {
                        for (int num = 0; num < root.data.messages.Length; num++)
                        {
                            text_dx = TimestampToDataTime(root.data.messages[num].timestamp) + " UID" + root.data.messages[num].sender_uid.ToString() + "说：" + root.data.messages[num].content;
                           using (StreamWriter writer = new StreamWriter(@".\" +textBox2.Text +".txt",true))
                            {
                                writer.WriteLine(text_dx);
                            }
                        }                        
                        end = root.data.min_seqno;
                    }
                    else
                    {
                        MessageBox.Show(root.message);
                    }
                } while (root.data.messages.Length>0);
                MessageBox.Show("成功");
            }
            catch(Exception abc)
            {
                MessageBox.Show("出现异常，请联系作者"+abc.ToString());
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.comboBox1.SelectedIndex = 0;
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            if(System.Text.RegularExpressions.Regex.IsMatch(textBox2.Text.ToString(), @"[\u4e00-\u9fa5]") || System.Text.RegularExpressions.Regex.IsMatch(textBox2.Text.ToString(), @"[a-zA-Z]"))
            {
                MessageBox.Show("UID或MID仅为数字！");
               
            }
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("https://github.com/hd80606b/BiliBili_Private_Msg");//调用网页的方法
        }
    }
}
