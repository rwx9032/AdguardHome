# 我个人使用的Adguardhome配置

指定大陆域名给大陆dns 使其返回最近的ip

指定被污染的域名给境外dns 使其返回正确的ip

可直接在配置文件的 upstream_dns_file 中指定文件

也可以直接复制懒人配置 AdGuardHome.yaml 到手动设置里面

然后wget AdguardHome_Upstreams.txt 到 /root 里面（一般就是ssh连上的默认的位置

默认配置账号root密码password记得更改

# 特别感谢

国内域名列表取自 felixonmars/dnsmasq-china-list

Gfw域名列表取自 gfwlist/gfwlist
