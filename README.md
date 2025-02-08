# AdGuardHome 优化配置方案

一个我个人使用的 AdGuardHome 配置方案，使国内域名使用国内 DNS，获取最佳节点；指定被污染的域名使用境外DNS处理，使其返回正确的ip

## 快速开始

### 方法一：使用完整配置文件

1. 下载 `AdGuardHome.yaml` 到您的 AdGuardHome 目录
2. 下载上游 DNS 配置文件：
```bash
wget -O /root/AdguardHome_Upstreams.txt https://raw.githubusercontent.com/rwx9032/AdguardHome/refs/heads/main/AdguardHome_Upstreams_Autoupdate.txt
```
3. 重启 AdGuardHome 服务
4. **立即更改管理员密码**

### 方法二：手动配置

1. 在 AdGuardHome 配置中设置 `upstream_dns_file` 指向 `AdguardHome_Upstreams.txt`
2. 导入 `AdGuardHome.yaml` 中的过滤规则
3. 重启服务生效

## 默认配置说明

- 管理界面：
  - 用户名：root
  - 密码：password（建议立即修改）
  - 端口：3001

- DNS 设置：
  - 监听端口：853

- 广告过滤：
  - 默认包含 AdGuard DNS filter, AdAway Default Blocklist, MalwareDomainList.com Hosts List, EasyList-CN, EasyList-Privacy, i-dont-care-about-cookies, 乘风-广告规则, 乘风-视频规则 若有失效请自行更新，可以手动添加其他过滤规则

## 数据来源

- 国内域名列表：[felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)
- GFW 域名列表：[gfwlist/gfwlist](https://github.com/gfwlist/gfwlist)
- 域名更新工具：[cokebar/gfwlist2dnsmasq](https://github.com/cokebar/gfwlist2dnsmasq)
- 广告过滤规则： 详见 `AdGuardHome.yaml`

## 许可证

MIT License
