# 附录 A 正式 r001：学术审核交接

- 原 academic：`/root/s02_academic`；轮次：1。
- 快照：`8829f8569ae0992f73e8c1f9fe747101c6c661975bf0da5ea31265109124cb22`。
- 结论：**changes_requested**；三个 minor issue，`resolved_issue_ids=[]`。

完整审核 A.1–A.4、入口、接口、交接和计算 README。主要来源链及主张边界成立：W26 的 Y=0／公共缩放／负 deficit／复杂度及低次数项均正确换算；MZ/HMT 的精确递推导出 4,8,8，保留有序分离方向；c_2(0) 计算明确使用实际 K=3 展开和 O(g^-4) 余项消去 c_3，而非输入 EGGLS 的条件预测。HMT/s03 的统一性没有偷换成 W26 固定标记结论。EGGLS 仅在计算后给 credit，Hua 未用。小顶点的完整椭圆 stack 规范与 kappa 负合并项保留，成对自环相关性、绝对／相对规范、核心完备性和数表作用均有正文规则。

需原作者修正：

1. **ACADEMIC-002**：A.1 的 `a_l/a_{l-1}` 源核比较没有定义和 l=0 初始约定。MZ 原文只定义非负索引；可直接用既有生成函数解释 source normalization，避免一次性别名，或严格限定、定义该局部源记号。正文和接口同步。
2. **ACADEMIC-003**：A.2 指导 elliptic raw connector 矩时误指含 1/2 的 side moment。表值本身正确，但照该句操作会少一倍。应直接写无 1/2 的积分及 Euler 导数，或明说取加权 side function 的两倍；zero-indicator 项另说明。
3. **ACADEMIC-004**：正文六处裸 `W26` 未引入，且书目实际标签是 `[WLQ+26]`。改为 Wang et al. 或正式 citation，保留定位即可。

十个主要陈述均直接接证明，来源及比较放在短 Remark。静态读过复现说明和体积算法，目标值在计算后核对，未把脚本输出当证明；本角色未重跑 CAS。提交、helper／entry／PDF 指纹与严格收据匹配，56 页 clean PDF 诊断为空；已查看相关 profile、ratio、预测说明、自环矩及核心小图／积分表页面。

只写本轮报告和交接，未改正文、共享、状态、旧记录或重建共享输出。请收齐本轮全部报告后统一返工，由原审核者对下一冻结快照复审；本报告不签署通过，也不宣称 Section 4 已完成。
