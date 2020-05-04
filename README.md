# angerZipDecode

原理：

１.指定密码包括的字符各类：数字，小写字母，大写字母，特殊字符

２.指定密码的长度

３.遍历所有可能的组合暴力破解

 

在密码比较简单的时候比较有用。

 

使用指导:

optional arguments:

  -h, --help           show this help message and exit
  
  -a                   指定密码中包含小写字母.
  
  -A                  指定密码中包含大写字母..
  
  -n                  指定密码中包含数字.
  
  -N N              指定密码的长度.
  
  --spec SPEC         单独指定密码中包含的字符，字符串形式,指定密码中包含'.'和'*',则指定".*".
  
  --filepath FILEPATH  待破解的zip加密文件路径.

 

使用举例：

指定密码由数字构成，密码长度为３位

python main.py -n -N 3 D:/xxx.zip

 

指定密码由大小写字母构成，密码长度为１０位

python main.py -a -A -N 10 D:/xxx.zip

 

指定密码由['!', '@',  '$', '&']４个特殊字符构成，密码长度为６位

python main.py -N 10 --spec "!@$&" D:/xxx.zip

