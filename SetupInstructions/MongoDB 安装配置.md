#### MongoDB 安装配置
* 版本：MongoDB 3.6.4
* 官网下载 Windows 64位版本`mongodb-win32-x86_64-2008plus-ssl-3.6.4-signed.msi`，双击安装。中间选择`Complete`，其他选择默认安装即可。
* 345
* 567
* 789
* 3
* 4
* 5
* 6


---
####安装遇到问题及解决方案
1. 如果选择了`Install MongoDB Compass`，安装中会卡在`Installing MongoDB Compass`。
取消，重新安装，但不勾选`Install MongoDB Compass`，之后单独下载`MongoDB Compass`进行安装。
2. 测试连接 MongoDB 时 ，提示***丢失api-ms-win-crt-runtime-l1-1-0.dll***。
在 百度—>微软—>搜索 Windows-KB2999226，选择系统匹配版本，安装即可。