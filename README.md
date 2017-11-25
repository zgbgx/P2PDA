# P2PDA
use the data scrapied from a third-party website to analyse chinese P2P industry(使用从第三方数据网站爬取的数据分析中国P2P行业现状)<br>
## 关于数据
爬虫位于crawl下，主要是 网贷之家和 人人贷两家的数据<br> 
数据来源于第三方网站，存在数据不完整，数据缺失以及数据错误的状况.<br>
表数量在二十张左右，表结构存储在 table.txt中.具体字段含义存在很多不明确。
![image](https://github.com/zgbgx/P2PDA/blob/master/3.png)<br>
还有关于人人贷的数据，没有给出 数据，可以运行 crawl下的相应爬虫爬虫
## 数据分析
数据分析使用python配合海致BDP完成，python 用到库主要有 numpy，matplotlib,pandas,sklearn,fbprophet,tushare.<br>
推荐使用python3，因为fbprophet等库不支持python2.<br>
海致BDP分析得到的只有图片的图表。<br>
数据量较大，运行python代码可能对系统内存有一定要求。<br>
本人做接触数据分析不久。所做数据分析都比较浅。<br>
jupyter notebook 代码 保存在 P2P.ipynb ,如若未安装jupyter notebook  可直接 看P2P.html 查看 代码输出结构。
![image](https://github.com/zgbgx/P2PDA/blob/master/2.png)<br>
