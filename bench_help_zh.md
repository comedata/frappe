# Bench 命令帮助文档

## 基本用法

```
Usage:  [OPTIONS] COMMAND [ARGS]...
```

## 选项

| 选项 | 说明 |
| --- | --- |
| `--version` | 显示版本信息 |
| `--use-feature TEXT` | 使用特定功能 |
| `-v, --verbose` | 显示详细信息 |
| `--help` | 显示帮助信息并退出 |

## 基础命令

| 命令 | 说明 |
| --- | --- |
| `app-cache` | 查看或删除属于bench的缓存项 |
| `backup-all-sites` | 备份当前bench中的所有站点 |
| `config` | 更改bench配置 |
| `disable-production` | 为bench禁用生产环境 |
| `download-translations` | 下载最新的翻译 |
| `drop` | 删除数据库或表 |
| `exclude-app` | 从更新中排除应用 |
| `find` | 从指定位置递归查找benches |
| `get` | 从互联网或文件系统克隆应用 |
| `get-app` | 从互联网或文件系统克隆应用 |
| `include-app` | 将应用包含在更新中 |
| `init` | 在指定位置初始化新的bench实例 |
| `install` | 安装设置bench的系统依赖项 |
| `migrate-env` | 将虚拟环境迁移到所需的Python版本 |
| `new-app` | 在apps文件夹下创建新的Frappe应用 |
| `pip` | 使用`bench pip help [COMMAND]`获取pip帮助 |
| `remote-reset-url` | 将应用远程URL重置为frappe官方URL |
| `remote-set-url` | 设置应用远程URL |
| `remote-urls` | 显示应用远程URL |
| `remove` | 从bench完全删除应用并重新构建 |
| `remove-app` | 从bench完全删除应用并重新构建 |
| `renew-lets-encrypt` | 设置最新的cron并更新Let's Encrypt证书 |
| `restart` | 重启supervisor进程或systemd单元 |
| `retry-upgrade` | 重试失败的升级 |
| `rm` | 从bench完全删除应用并重新构建 |
| `set-mariadb-host` | 为bench设置MariaDB主机 |
| `set-nginx-port` | 为站点设置NGINX端口 |
| `set-redis-cache-host` | 为bench设置Redis缓存主机 |
| `set-redis-queue-host` | 为bench设置Redis队列主机 |
| `set-redis-socketio-host` | 为bench设置Redis socketio主机 |
| `set-ssl-certificate` | 为站点设置SSL证书路径 |
| `set-ssl-key` | 为站点设置SSL证书私钥路径 |
| `set-url-root` | 为站点设置URL根路径 |
| `setup` | 用于启用设置bench的命令组 |
| `src` | 打印bench源文件夹路径 |
| `start` | 启动Frappe开发进程 |
| `switch-to-branch` | 将所有应用切换到指定分支 |
| `switch-to-develop` | 将frappe和erpnext切换到develop分支 |
| `update` | 在当前bench上执行更新操作 |
| `validate-dependencies` | 验证package.json中指定的所有依赖项 |

## 框架命令

| 命令 | 说明 |
| --- | --- |
| `add-database-index` | 添加新的数据库索引并创建属性设置器 |
| `add-system-manager` | 向站点添加新的系统管理员 |
| `add-to-email-queue` | 将电子邮件添加到电子邮件队列 |
| `add-to-hosts` | 将站点添加到hosts文件 |
| `add-user` | 向站点添加用户 |
| `backup` | 备份站点 |
| `browse` | 在网络浏览器中打开站点 |
| `build` | 编译JS和CSS源文件 |
| `build-message-files` | 构建用于翻译的消息文件 |
| `build-search-index` | 重建全局搜索使用的搜索索引 |
| `bulk-rename` | 通过CSV文件重命名多个记录 |
| `clear-cache` | 清除缓存、文档类型缓存和默认值 |
| `clear-log-table` | 如果任何日志类型表增长过大，则清除它 |
| `clear-website-cache` | 清除网站缓存 |
| `compile-po-to-mo` | 翻译：将PO文件编译为MO文件 |
| `console` | 为站点启动ipython控制台 |
| `create-patch` | 交互式创建新补丁 |
| `create-po-file` | 翻译：为区域设置创建新的PO文件 |
| `create-rq-users` | 创建Redis队列用户并添加到acl |
| `data-import` | 从CSV或XLSX文件批量导入文档 |
| `db-console` | 进入给定站点的数据库控制台 |
| `describe-database-table` | 描述表的各种统计信息 |
| `destroy-all-sessions` | 清除所有用户的会话（将他们注销） |
| `disable-scheduler` | 禁用调度器 |
| `disable-user` | 在站点上禁用用户账户 |
| `doctor` | 获取有关后台工作者的诊断信息 |
| `drop-site` | 从数据库和文件系统中删除站点 |
| `enable-scheduler` | 启用调度器 |
| `execute` | 执行函数 |
| `export-csv` | 导出带有数据的数据导入模板 |
| `export-doc` | 将单个文档导出为csv |
| `export-fixtures` | 导出固定装置 |
| `export-json` | 将文档列表导出为json到给定路径 |
| `generate-pot-file` | 翻译：生成POT文件 |
| `get-untranslated` | 获取语言的未翻译字符串 |
| `import-doc` | 导入（插入/更新）文档列表 |
| `import-translations` | 更新翻译的字符串 |
| `install-app` | 在站点上安装新应用，支持多个应用 |
| `jupyter` | 启动交互式jupyter笔记本 |
| `list-apps` | 列出站点中的应用 |
| `make-app` | 创建应用模板 |
| `mariadb` | 进入给定站点的mariadb控制台 |
| `migrate` | 运行补丁，同步架构并重建搜索 |
| `migrate-csv-to-po` | 翻译：从CSV文件迁移到PO文件 |
| `migrate-to` | 将站点迁移到指定提供商 |
| `migrate-translations` | 迁移目标应用特定的翻译 |
| `new-language` | 为给定应用创建lang-code.csv |
| `new-site` | 创建新站点 |
| `ngrok` | 启动到本地环境的ngrok隧道 |
| `partial-restore` | 部分恢复，参考https://frappeframework.com/docs |
| `postgres` | 进入给定站点的postgres控制台 |
| `publish-realtime` | 从bench发布实时事件 |
| `purge-jobs` | 如果事件发生器失败，清除任何待处理的定期任务 |
| `ready-for-migration` | 准备迁移，参考https://frappeframework.com/docs |
| `rebuild-global-search` | 在当前站点中设置帮助表 |
| `reinstall` | 重新安装站点 |
| `reload-doc` | 重新加载DocType的架构 |
| `reload-doctype` | 重新加载DocType的架构 |
| `remove-from-installed-apps` | 从站点的已安装应用列表中删除应用 |
| `request` | 以管理员身份运行请求 |
| `reset-perms` | 重置所有文档类型的权限 |
| `restore` | 从sql文件恢复站点数据库 |
| `run-parallel-tests` | 运行并行测试，参考https://frappeframework.com/docs |
| `run-patch` | 运行特定补丁 |
| `run-tests` | 运行Python单元测试 |
| `run-ui-tests` | 运行UI测试 |
| `schedule` | 启动调度器进程 |
| `scheduler` | 控制调度器状态 |
| `serve` | 启动开发Web服务器 |
| `set-admin-password` | 为站点设置管理员密码 |
| `set-config` | 在site_config.json中插入/更新值 |
| `set-last-active-for-user` | 将用户最后活动日期设置为当前日期时间 |
| `set-maintenance-mode` | 将站点置于维护模式以进行升级 |
| `set-password` | 为站点上的用户设置密码 |
| `show-config` | 以STDOUT格式打印配置文件 |
| `show-pending-jobs` | 获取有关后台作业的诊断信息 |
| `start-recording` | 启动Frappe记录器 |
| `stop-recording` | 停止Frappe记录器 |
| `transform-database` | 更改表的内部设置 |
| `trigger-scheduler-event` | 触发调度器事件 |
| `trim-database` | 删除已删除DocTypes的数据库表 |
| `trim-tables` | 从表中删除字段已删除的列 |
| `uninstall-app` | 删除应用和链接的模块 |
| `update-csv-from-po` | 从PO文件添加缺失的翻译到CSV |
| `update-po-files` | 翻译：将PO文件与POT文件同步 |
| `update-translations` | 更新翻译的字符串 |
| `use` | 设置默认站点 |
| `version` | 显示所有已安装应用的版本 |
| `watch` | 监视并编译JS和CSS文件 |
| `worker` | 启动后台工作进程 |
| `worker-pool` | 启动后台工作池 |