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

                long size = 0;

                //获取文件大小
                using (FileStream file = System.IO.File.OpenRead(path))
                {
                    size = file.Length;//文件大小。byte
                }

                //判断文件大于20M，自动删除。
                if (size > (1024 * 4 * 512 * 10))
                {
                    System.IO.File.Delete(path);
                }
            }
            catch
            {

            }
        }
    }
}
