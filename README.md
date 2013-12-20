##利用python的子进程调用uglifyjs,cleancss进行 js，css压缩

### 这只是一个简单的demo
此demo通过创建python的子进程，调用uglifyjs,cleancss进行静态资源压缩。
再通过正则手段，将所有css中的img图片加上版本号
通过正则，将html的空格，注释，换行符，回车符，制表符去掉，达到html压缩的目的
通过正则，将html中引用的js，css加上版本号（因为只是demo，所以加的是时间戳）

### 具体实现请参看代码注释.

* todo:将版本号根据md5值判断，如果没有修改，不需要修改版本号

* todo: 转换成纯nodejs版本，利用node-webkit进行可视化操作
