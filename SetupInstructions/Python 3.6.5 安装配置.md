####Python 3.6.5 安装配置
* 在已有Python 2.7的PC上安装Python 3.6.5，记得勾选`Add Python Path to environment`。
* 安装列表
数据库：Mongodb   ——> pip install pymongo==3.6.1
数据分析：pandas  ——> v0.23.0 Final (May 15, 2018)  pip install pandas==0.23.0
爬虫库：
requests ——>  requests 2.18.4  3.6   pip install requests==2.18.4
lxml(Xpath)——>  lxml 4.2.1 3.7
BeautifulSoup ——>  pip install beautifulsoup4==4.3.2  Beautiful Soup 4 works on both Python 2 (2.7+) and Python 3.
Scrapy
		pip install pywin32==223(pywin32-223-cp36-cp36m-win_amd64.whl)
		pip install setuptools==39.2.0
		pip install lxml==4.2.1
		pip install zope.interface==4.5.0
		pip install pyOpenSSL==18.0.0
		pip install Twisted-18.4.0-cp36-cp36m-win_amd64.whl // pip install Twisted==18.4.0
		pip install w3lib==1.19.0
		pip install Scrapy==1.5.0




---
#### 安装遇到的问题及解决方案
1. 安装失败：`0x80091007 - 哈希数值不正确。`
重装，但不勾选`Download Debugging Symbols`，成功安装。
2. 执行`pip install Twisted==18.4.0`时，报错`error: Microsoft Visual C++ 14.0 is required.`
下载 whl 版本，使用`pip install Twisted-18.4.0-cp36-cp36m-win_amd64.whl`安装即可。