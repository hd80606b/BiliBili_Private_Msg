using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Runtime.InteropServices;

namespace bilibili私信导出
{
    class LogWrite
    {


        public static void DataWrite(string logstring,string savePath, string savefilename)
        {
            try
            {
                

                string path = savePath + savefilename;
                //判断文件是否存在，没有则创建。
                if (!System.IO.File.Exists(path))
                {
                    FileStream stream = System.IO.File.Create(path);
                    stream.Close();
                    stream.Dispose();
                }

                //写入日志
                using (StreamWriter writer = new StreamWriter(path, true))
                {
                    writer.WriteLine(logstring);
                }

               
            }
            catch
            {

            }
        }
    }
}
