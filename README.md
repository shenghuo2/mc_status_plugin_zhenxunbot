# mc_status_plugin_zhenxunbot

![Python Version](https://img.shields.io/badge/python-3.7.3+-blue.svg)![Pypi Version](https://img.shields.io/pypi/v/nonebot-plugin-mcstatus.svg)

基于[zhenxunbot](https://github.com/HibiKier/zhenxun_bot)和[mcstatus](https://github.com/py-mine/mcstatus)模块开发的minecraft服务器状态查询插件

以图片的形式返回查询结果	满足 ~~(我的)~~ 强迫症

### 当前版本

v0.20

### 安装

1. 将mc_status文件夹放入plugins文件夹即可
2. 安装**依赖**

```
pip3 install -r requirements.txt
```



### 使用

**使用前请先确保命令前缀为空，否则请在以下命令前加上命令前缀 (默认为 `/` )**

- `mc ip` 获取当前服务器的状态

- `mcplayer` 获取当前服务器一部分在线玩家列表   （一般只支持纯原版服）

- `mcsrv` 获取当前服务器IP的srv解析地址

  



### TO DO

- [x] 修复srv解析报错的问题
- [x] 添加查询玩家列表功能（没啥用）
- [x] 修复过长的版本号 直接超出图片的问题
- [x] 添加srv解析查询功能
- [x] 对于motd的彩色字符进行支持
- [ ] 对于基岩版服务器进行支持
- [ ] 高版本的RGB三原色渐变
- [ ] 符号显示为方块的问题没有头绪



### 更新日志

##### 2022.6.8 [v0.01-v0.0.2]

第一次更新

修复srv解析报错的问题

添加查询玩家列表功能（没啥用）

##### 2022.6.9 [v0.11]

第二次更新

修复过长的版本号 直接超出图片的问题

##### 2022.6.10 [v0.12]

添加srv解析查询功能

修改github排版

##### 2023.1.17 [v0.20]

增加以§作为彩色样式的MOTD的支持

发现其他问题，比如1.17后高版本的RGB三原色渐变

增加了字体bug (由于字库不全)



### 碎碎念

我半年的时间找了各大QQ机器人框架

一直没找到合适的查询mc服务器状态插件

我作为一个n年的mc老玩家	~~怎么能容忍这种事情呢~~

所以我写了这么个插件



写完放到我某度云的服务器上发现有解析srv的IP全报错

改了防火墙也没用	最后找了个在线网站 爬他
