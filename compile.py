# -*- coding: utf-8 -*-
import subprocess
import os
import codecs
import re
import time
import datetime
now = str(int(time.mktime(datetime.datetime.now().timetuple())))
#path = os.path.abspath('')
cur_path = os.getcwd()


#处理css，将所有css中的 img加上时间戳
cssFiles = ['test']
for css in cssFiles:
    file = os.path.abspath(cur_path + '/' + css + '.css')
    fp = codecs.open(file,'r','UTF-8')
    outerCssFile = os.path.abspath(cur_path + '/' + css + '.min.css')
    outerCssFp = codecs.open(outerCssFile,'w+','utf-8')
    content = fp.read()
    print content
    content = re.sub(r'(\.jpg|\.png|\.gif)','\g<1>?' + now,content)
    print content
    outerCssFp.write(content)
    #close
    fp.close()
    outerCssFp.close()
    #创建子进程调用 node cleancss进行css压缩
    outfile = os.path.abspath(cur_path + '/'+ css +'.min.css') 
    subprocess.call("C:/Users/pc/AppData/Roaming/npm/cleancss.cmd -o " + outfile + " " + outerCssFile)

#压缩js
jsFiles = ['test']
for js in jsFiles:
    file = os.path.abspath(cur_path + '/' + js + '.js')
    fp = codecs.open(file,'r','UTF-8')
    outerJsFile = os.path.abspath(cur_path + '/' + js + '.min.js')
    outerJsFp = codecs.open(outerJsFile,'w+','utf-8')
    content = fp.read()
    outerJsFp.write(content)
    #close
    fp.close()
    outerJsFp.close()
    #创建子进程调用 node cleancss进行css压缩
    outfile = os.path.abspath(cur_path + '/'+ js +'.min.js') 
    subprocess.call("C:/Users/pc/AppData/Roaming/npm/uglifyjs.cmd -o " + outfile + " " + outerJsFile)



#处理html调用静态资源，给静态资源加上缓存时间戳
targetsHtml = ['test']
for html in targetsHtml :
    file = os.path.abspath( cur_path + '/' + html + '.html')
    fp = codecs.open(file,'r','UTF-8')
    outerFile = os.path.abspath( cur_path + '/' + html + '-dist.html')
    outerFileFp = codecs.open(outerFile,'w+','utf-8');
    content = fp.read()
    #删除空格
    content = re.sub(r'\s*\r?\n\s*', '', content)
    #删除注释
    content = re.sub(r'<!--.*?-->', '', content)
    content = re.sub(r'href="(.*)\.css"','href="\g<1>.min.css?t=' + now + '"',content)
    content = re.sub(r'href="(.*)\.js"','href="\g<1>.min.js?t=' + now + '"',content)
    #print content
    outerFileFp.write(content)
    
    fp.close()
    outerFileFp.close()
    
    #print index


print now
