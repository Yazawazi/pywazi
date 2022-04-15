<p align="center">
<img src="https://i.loli.net/2021/10/09/vGaO5TtPFzkQRx2.jpg" width="80%"/>
</p>

<p align="center">
PyWazi 是一个针对一些网站的数据采集、处理和操作模块，使用 Python3 语言。目前版本为 2.0 dev，如果你有想法或在使用中出现问题了，欢迎提出 issue。
</p>

<p align="center">
<a href="https://www.python.org/"><img src="https://shields.io/badge/Python-3-green?style=flat-square" /></a>
<a href="https://github.com/Yazawazi/pywazi"><img src="https://shields.io/badge/Version-1.5-green?style=flat-square" /></a>
</p>

> 其实没有什么好说的。

## 需要更新内容

- [ ] 单个文件的多线程下载（在爬取视频时使用）（暂时不考虑多个连接的多线程，容易寄）；
- [x] 修复 PicAcg 相关内容；
- [x] 增加自动化全局配置。

### 可能会增加的网站支持

仍在考虑中...

## 声明
依 GPL-3.0 许可协议开源（更多信息见下），随意 Fork，请不要使用本项目的代码进行商业用途（*当然，谁知道呢？*）。

## 支持网站或应用列表

+ [AsianSister](https://asiansister.com/)
+ [Danbooru](https://danbooru.donmai.us/) *等一系列基于 Danbooru 的网站 (API 相近)*
+ [ExHentai](https://exhentai.org/) *没有 E-Hentai 的支持*
+ [JavBus](https://javbus.com/)
+ [Nyaa](https://nyaa.si/) *当然也有 sukebei 的支持*
+ [PicAcg](https://picacomic.xyz/)

更多信息请阅读 `doc.md` 文档以获取帮助。

## 前置库

需要安装：
+ beautifulsoup4>=4.9.0
+ bs4>=0.0.1
+ certifi>=2021.10.8
+ lxml>=4.6.3
+ urllib3>=1.26.6

## 一些说明
有时候我的想法比较混乱，并且我不遵守 PEP 8，所以部分代码你可能看不懂。如果你有问题的话，可以找我谈谈或者自己修改一下。如果出现以下问题了，请试着解答以下问题找找原因：

1. 前置环境有安装吗？Python 是 3 代的吗？
2. 配置对了吗，代理类型不要搞混；
3. 账号密码或 Cookies 请保证正确，账号确保不受限；
4. 查看说明文档找找相关内容或百度、谷歌等相关内容。

如果这些都解决不了问题，请发表 issue 并提供上下文，可能的代码，前置库版本等有关信息。

## 开发文档
参见 `doc.md`，在新版本中，可以使用 `help()` 函数直接获取内嵌文档。

## 普通教程
请直接访问：https://yazawazi.github.io/pywazi/

## 有什么用
你可以单独使用 PyWazi 来进行开发爬虫，也可以使用该模块开发其他开源项目。

## 有关问题报告或修复
Issue 或者提交 Pull Request 或者提交代码到仓库。

## 鸣谢
本项目的开发离不开以下开源项目：

1. JavBus 代码参考：[WWILLV/iav: 可搜索javbus、btso的磁力链接和avgle的预览视频 (github.com)](https://github.com/WWILLV/iav)；
2. PicAcg 部分：[AnkiKong/picacomic: 哔咔漫画相关api (github.com)](https://github.com/AnkiKong/picacomic) 提供了大部分的 Api 链接；使用了 [tonquer/picacg-windows: 哔咔漫画，picacomic，bika，PC客户端。 (github.com)](https://github.com/tonquer/picacg-windows)  中的最新 headers；https://www.hiczp.com/wang-luo/mo-ni-bi-ka-android-ke-hu-duan.html 提供了一些想法（GitHub 地址：[czp3009/czp-blog (github.com)](https://github.com/czp3009/czp-blog)）。

感谢 [cloudwindy (github.com)](https://github.com/cloudwindy) 提供的 ExHentai 账号，得以我进行开发测试；感谢我的朋友 **The Galaxy~ Of Dick** 给我整的 Banner。

感谢 GitHub 的 Copilot 提供的智能自动代码补全功能，让我的代码更加简洁，更加美观（大嘘，这句话是 Copilot 打出来的）。

## 版权等相关问题

1. 代码以 GPLv3 协议发布，文档，包括内嵌文档，自述等不以 GPLv3 协议发布，其内部使用的名言、歌词、相关文学作品版权归原作者所有；
2. 如果我的代码对您的网站或者程序有侵犯，请联系我，我会在一周内进行处理；
3. 如果我使用的名言、歌词、相关文学作品侵犯了您的版权，请联系我，我会在一周内进行处理；
4. 文档，包括内嵌文档，自述（非引用部分）等以 MIT 协议发布。

## Non-simplified Chinese users?
Sorrrrrrrrrrrrrry, But I don't want to translate it.
