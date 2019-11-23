数据库说明：
1、创建数据库字符集选择utf-8；
2、执行tebonxspider.sql初始化表结构；

使用说明：
1、调用initdata.py获取初始数据（1989年-至今的所有数据）；
2、后续调用getdata.py增量获取当前季度的数据（数据源一个季度更新一次）；

依赖说明：
1、基于python3.6；
2、pip install -r requirements.txt 安装第三方依赖包；

to_sql()参数说明：
    name:表名，pandas会自动创建表结构
    con：数据库连接，最好是用sqlalchemy创建engine的方式来替代con
    flavor:数据库类型 {‘sqlite’, ‘mysql’}, 默认‘sqlite’，如果是engine此项可忽略
    schema:指定数据库的schema，默认即可
    if_exists:如果表名已存在的处理方式 {‘fail’, ‘replace’, ‘append’},默认‘fail’
    index:将pandas的Index作为一列存入数据库，默认是True
    index_label:Index的列名
    chunksize:分批存入数据库，默认是None，即一次性全部写人数据库
    dtype:设定columns在数据库里的数据类型，默认是None


参考：
https://blog.csdn.net/qq_30981779/article/details/52891530
http://www.waditu.cn/billboard.html
https://blog.csdn.net/new_stranger/article/details/83346258