#### 在原先[SpiderClub/haipproxy cli](https://github.com/SpiderClub/haipproxy.git) 的基础上，稍微修改了下

* 可以通过scrapy中的settings配置来覆盖默认配置，
* 编写了scrapy download middleware ,自动配置proxy,前提是你通过haipproxy配置好了redis proxy pool

###  todo

* delete proxy 逻辑,删除连接失败的代理