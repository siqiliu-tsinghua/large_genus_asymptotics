# PDF-NAVIGATION：工具准备

已在 root 修改前保存精确基线：`build/pdf-navigation-20261116/baseline.json`，HEAD 为干净的 `6156e95181cc6e244182757832bcf52881ce6506`，含 9,071 个当前文件哈希、十节实际 approved/fresh 快照、原角色及来源哈希 `2e1a05d5d85d1f39c359c6f28a17cbd7abda6d6c6fbfbf93efa56137cda86ecc`。旧主 PDF、实际提取文本、aux、log 保留在同目录 baseline/ 并记录 SHA；捕获完成已立即通知 root 可以编辑。root 已确认旧 PDF 为 102 页、零内部链接及零书签项。

本次沿用精简流程，唯一辅助脚本为 `build/pdf-navigation-20261116/coordinate.py`。只允许 preamble 的 hyperref/bookmark/hypersetup 增量，原有定义和其余所有数学、章节、接口、handoff 及已有档案保持基线；所有十位作者均仅写外部 UID_writer.md。脚本没有更改生产工具或旧 helper/pin。生产 build.py 已允许标准生成的 `.out`、`.toc`，无需补生产例外。

## Root 操作

S1 已真实 start/bind/dispatch，原作者已实际 ACK/STOP，仍为 drafting；不再次 start、bind writer 或 adopt。

```text
python -B build/pdf-navigation-20261116/coordinate.py pin
python -B build/pdf-navigation-20261116/coordinate.py freeze s01
```

freeze 先真实构建唯一 full-current-main companion：abstract、TOC、全部十节、bibliography 和现有 footer。反复 XeLaTeX/BibTeX 至 aux 稳定、无 rerun 警告，检查实际 FLS 输入并与保留的旧正文文本、430 标签映射比较。该 companion 明确不是后续九节已完成本轮审批的声明。

随后使用或复用 source_hash/PDF SHA 完全匹配的真实生产单节依赖预览，focused validate、真实 submit、绑定原审核者并输出真实 followup_task 参数。root 仍须真正执行 collaboration 调用；参数文件不是已调用记录，脚本不生成作者文字或审核结论。

```text
python -B build/pdf-navigation-20261116/coordinate.py reports s01
python -B build/pdf-navigation-20261116/coordinate.py accept s01
```

其余各节按请求顺序 start→实际原作者外部 ACK/STOP→freeze→实际原三位审核者签新精确 snapshot→reports→accept。单节使用公共标准预览及 `validate --unit UID`，不用陈旧下游导致失败的提前整稿 validate。全部报告保留完整结构与证据，复用旧数学判断，只核对 preamble 差异和新快照，不重读证明、不核算、不查新库或文献、不重复逐节端点图片。

## 实际导航与最后交付

共同稿使用现有 Poppler：`pdftohtml -xml -i -hidden -enc UTF-8 -stdout` 保存 XML，统计实际内部链接及 outline 项；`pdfinfo -dests` 保存命名目标，`pdfinfo` 记录实际页数。三者必须确实存在。root 可从这些原始证据抽查目录、正文交叉引用与书签；不是仅凭加载 hyperref 就声称导航有效。

全部十节真实刷新、fresh 后：

```text
python -B build/pdf-navigation-20261116/coordinate.py final
```

final 才真实完整严格构建、官方导出及独立编译，比较共同稿、主稿和隔离稿的打印文本与标签，并实际检查主 PDF、投稿 PDF、隔离 PDF 的导航。**`submission/paper.tex` 和 `submission/paper.pdf` 从开始就是精确生成物例外**；变化必须分别匹配官方 export 收据的 SHA、当前 source_hash、主 PDF SHA 以及十节新验收，不沿用旧的单 TeX 输出白名单。两份生成文件之外不增加论文附件。

执行日志保留在新随机目录；新 snapshot 与原 ACK、标准预览、共同证据均绑定哈希。不改已冻结材料；若构建需要重建旧 aux/toc/out，仅处理生成缓存，不能更改来源快照或伪造通过。

本会话仅捕获基线、写本轮新辅助脚本/请求记录/本报告，做语法与只读 check；未执行状态命令、agent 调用、构建、导出或整套测试，未安装依赖或作新的 API/库/模型研究。这是工具准备，不是论文三角色审批。root 已读脚本增量并将自行 pin/freeze，之后本会话不再改脚本。

STOP。
