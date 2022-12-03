# DomainCheck
域名验活脚本，写的比较简单，重复造轮子是因为在测试中发现httpx这个工具虽然比较好用，但是有些域名会出现遗漏识别（域名有站，但httpx没有扫出来）的情况，所以搞个这个辅助用。

**安装依赖**
```
pip3 install -r requirements.txt
```

**使用**
```
python main.py -f domains.txt -t 30 -o r.txt
```

**结果**
![检查结果](https://github.com/Al0neme/DomainCheck/blob/main/result.png?raw=true)
