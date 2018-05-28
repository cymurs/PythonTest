#### Scrapy 环境部署
* 安装 **setuptools** 和 **pip**
将 ***D:\Python27\Scripts*** 添加到系统环境变量path里，注意加分号  
使用 `pip install 包的名字.whl` 或 `python setup.py install` 进行安装    
下面同理
* 安装 **lxml**
* 安装 **zope.interface**
* 安装 **Twisted**
* 安装 **pyOpenSSL**
* 安装 **pywin32**
* 安装 **Scrapy**

---
#### 安装遇到问题及解决方案
1. 安装中遇到`包名.whl is not a supported wheel on this platform.`
在python下的shell中通过`import pip;print(pip.pep425tags.get_supported())`查看当前pip命令是否支持`cp27m`或`win_amd64`。否则，升级pip版本或python版本。
2. 出现`error: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27`。
安装 ***VCForPython27.msi***, 并且**重启**。
3. 出现`[scrapy.spidermiddlewares.httperror] INFO: Ignoring response <403 https://movie.douban.com/top250>`。
提示403，这是因为服务器判断出爬虫程序，拒绝访问，在settings中设定USER_AGENT的值，伪装成浏览器访问页面。
4. 为PyCharm配置GitHub的版本控制。
首先，要访问github，需要翻墙，在**设置—>外观和行为—>常规—>HTTP Proxy**中选中**使用代理—>SOCKS**，填入主机名和端口号（比如本人设置**127.0.0.1**和**1080**），点击**Check connection**验证，随便输入一个网址，比如www.baidu.com，弹出**Connection successful**的窗口，表明代理设置成功；
其次，在**设置—>版本控制—>GitHub**中Host填写**github.com**，选择Auth Type为**Password**，然后输入用户名和密码，点击**Test**进行验证，弹出**Connection successful**的对话框，表明设置成功。
5. 运行`scrapy shell 'http://scrapy.org'`时，报错`ValueError: invalid hostname: 'http`。
只需把**单引号**改为**双引号**即可。
6. 爬取https网页并翻墙，以`scrapy shell`为例
*>>>* `data = scrapy.Request("https://support.binance.com/hc/zh-cn/sections/115000106672-%E6%96%B0%E5%B8%81%E4%B8%8A%E7%BA%BF", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}, meta={"proxy":"http://127.0.0.1:1080"})`
*>>>* `fetch(data)`
其中，**User-Agent** 获取https网页，**proxy**设置代理翻墙。


