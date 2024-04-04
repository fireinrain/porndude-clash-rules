## All site on theporndude clash rules

## How to use

在clash 配置的rule-provider 添加

```yml

rule-providers:
    theporndude: { type: http, behavior: domain, url: 'https://ghproxy.com/https://raw.githubusercontent.com/fireinrain/porndude-clash-rules/master/porndude.txt', path: ./ruleset/porndude.yaml, interval: 86400 }
  
  
或者添加为

rule-providers:
    adults: { type: http, behavior: domain, url: 'https://ghproxy.com/https://raw.githubusercontent.com/fireinrain/porndude-clash-rules/master/adults.txt', path: ./ruleset/adults.yaml, interval: 86400 }
  

```
最后在配置 rules 添加

```bash
rules:
    - 'RULE-SET,theporndude,🚀 节点选择'
或者添加为
rules:
    - 'RULE-SET,adults,🚀 节点选择'

```