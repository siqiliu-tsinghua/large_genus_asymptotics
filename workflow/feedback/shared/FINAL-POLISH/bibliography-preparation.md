# Final bibliography and submission preparation

准备者：`/root/s02_academic`；日期：2026-11-16；起始 Git 基线：`fa2f374`。这是来源和投稿资料准备，**不是冻结稿审核，不签署 pass，不批准最终单文件构建**。本次只写本文件；未修改正文、书目、README、共享规则、状态或旧审核。下面区分本次在线取得的原始记录、已读本地原文和无法在线取得的材料。

已读现行 AGENTS、context、academic 职责、提纲及正文实际引用。盘点范围为第 1–8 节、附录 A/B、摘要与 main；已退休 C 的文件不计作在用正文。审前 `references.bib` 有 25 条，实际引用 24 个不同 key，无 `nocite` 通配。唯一未引条目 `KMZ96` 是 `KMZ96v1` 的期刊版重复记录。审前书目 SHA256 为 `3525ab85958b760b05b0f86a21a63bf3493230c6b1e940a8d6877ac91a68f0be`（从 `git show fa2f374:references.bib` 取得）。

## 协调者的最小共享处理清单

1. 删未引的 `KMZ96` 数据库记录即可；**保留 `KMZ96v1` 的 key、固定版本和正式出版 note**，不替换正文定位。这不是删除正文实际使用的文献。
2. `SW25` 补已发表信息，并明确仍按 v4 编号。建议下列 article 条目；190 是 article number，不是页码，故不放 `pages`。标准 alpha 不印 `eid`，用 note 明示最可靠。出版社页面和当前 Crossref 均支持卷 406、期 8、article 190、2025 年；2025-07-02 是上线日期。
3. DLMF 仍为 Release **1.2.8 of 2026-09-15**，版本和编辑名单无须改。实际本次已访问，可将访问日改为 **2026-11-16**。保留已验证的 `key = {{\relax DLMF}}`，不改宏或包。
4. `W26` 继续固定 **v4**，不追换现在的 v5。补查发现 v5 的一般结果确实覆盖无标记高阶体积系数，建议另加 `W26v5` 作明确的新版背景引用，见下节。不能将 v5 新编号倒填入旧 `W26` 的 Lemma 7.2 / Appendix C.1 引文。
5. 其余已用条目的作者、题名、出版卷年、页码、DOI 和已指定版本，未发现需要更正的实质错误。`LX26b` 的 `eprint` 未附 v1，但 howpublished 和 URL 均已固定 v1，并无版本歧义；无需为统一字段而另开科学修改。

```bibtex
@article{SW25,
  author  = {Shen, Yang and Wu, Yunhui},
  title   = {Arbitrarily Small Spectral Gaps for Random Hyperbolic
             Surfaces with Many Cusps},
  journal = {Communications in Mathematical Physics},
  volume  = {406},
  number  = {8},
  year    = {2025},
  doi     = {10.1007/s00220-025-05366-7},
  note    = {Article 190. Cited numbering follows arXiv:2203.15681v4},
  eprint  = {2203.15681v4},
  url     = {https://arxiv.org/abs/2203.15681v4}
}
```

直接证据：[Springer 出版页](https://link.springer.com/article/10.1007/s00220-025-05366-7)、[出版者提交的 Crossref 记录](https://api.crossref.org/works/10.1007/s00220-025-05366-7)、[实际采用的 arXiv v4](https://arxiv.org/abs/2203.15681v4)。不要沿用 arXiv 页面尚写的 “to appear” 作为当前出版状态，也不要据期刊发表而假定编号与预印本相同。

准备过程中观察到共享书目已并发出现删 KMZ96、SW25 article 字段、DLMF 新访问日和 LiuData26 URL 的额外 `allowbreak`。这些不是本审核者所写；本记录提供依据，不认领其编辑来源，也不把观察到的修改当作正式审核签字。

## W26 v5 的直接相关性补查

依协调者补充要求，本次只查新版摘要、目录、主要陈述及明确的无标记系数规则，没有通读 274 页或重推其证明。[当前无版本页面](https://arxiv.org/abs/2610.35492) 指向 **2026-11-10 的 v5**；[v5 原文](https://arxiv.org/pdf/2610.35492v5) 的 Theorem 1.1（印刷 p.8）给全标记数的绝对展开，§11.2（pp.55–56）、(11.6)–(11.7) 给无标记系数的有限阶规则。因此一般结果覆盖本稿所需的二阶无标记体积系数层面。所查摘要、目录和主陈述未宣称本稿四个纯 Hodge 积分定理；这不是对新版全部内容的穷尽性结论。

本稿目前写“从精确递推无条件重建，并与条件性预测核对”，没有宣称首次发现该体积系数，因而不必撤回自主推导的地位。建议在引言或附录 A 的来源说明中简短承认新版的一般背景；它不替代本稿计算链，也不成为新的证明输入。可用：

> For a uniform absolute expansion at all cusp counts, including a finite-order rule for the unmarked coefficients, see \cite[Theorem~1.1 and (11.6)--(11.7)]{W26v5}.

```bibtex
@misc{W26v5,
  author       = {Wang, Qihang and Li, Zhiyi and Qiu, Bolin and Wang, Shuaijia
                  and Zhong, Yuan and Chen, Kun and Xia, Renqiu},
  title        = {Uniform Large-Genus Asymptotics of {Weil--Petersson} Volumes},
  year         = {2026},
  howpublished = {arXiv:2610.35492v5},
  eprint       = {2610.35492v5},
  url          = {https://arxiv.org/abs/2610.35492v5}
}
```

若采纳，v4 和 v5 是分别承担精确输入与新版背景的两个实际引用，不是未引的重复 key；alpha 自动区分同作者同年标签属正常行为。旧版 profiles 的来源记号、复杂度换算和所有 locator 均维持 v4。

## 已发表来源的元数据与实际定位

以下各行的 DOI 链指原始出版者记录，Crossref 行指本次直接读取的出版者提交元数据；本地原文定位沿用原会话已经完成的逐页核查，并已与当前正文实际 cite 的位置对照。本次没有重审未变的长证明。

| Key | 出版信息与本次 primary 证据 | 当前实际使用的定位、版本和归属边界 |
| --- | --- | --- |
| Mum83 | David Mumford；*Arithmetic and Geometry*, Vol. II，Progress in Mathematics 36，Birkhäuser，1983，271–328；[Crossref](https://api.crossref.org/works/10.1007/978-1-4757-9286-7_12)。Artin/Tate 编辑信息与已有原始记录一致。 | §5，(5.2)–(5.3)；本地 PDF 34/36 页。原 Bernoulli convention 与非对数/对数 kappa 的换算已有说明，不把原印刷惯例直接移植。 |
| FP00 | Carel Faber、Rahul Pandharipande；Invent. Math. 139(1) (2000)，173–199；[Crossref](https://api.crossref.org/works/10.1007/s002229900028)。 | §1.1 未编号 Theorem (Mumford)，§1.3 (16)–(18)，Theorem 2 (6)，§4.2 Lemma 1。多点 lambda_g 在当时仍为 conjecture；本文已把后来证明归 FP03。source b_G 改记 beta_G 已明示。2000 卷年保留。 |
| ABCDGLW23 | Andersen、Borot、Charbonnier、Delecroix、Giacchetto、Lewański、Wheeler，顺序与变音符正确；JLMS 107(1) (2023)，254–332；[Crossref](https://api.crossref.org/works/10.1112/jlms.12686)。2022 上线不替代 2023 卷年。 | [v3](https://arxiv.org/abs/1905.10352v3)，Lemma 3.10，(3.18)–(3.22)；S5 用 (3.18)–(3.21) 的一般边系列。来源为 cohomology；本文 normal-line/push-pull 的 Chow 推导及有序覆盖半因子责任清楚。 |
| GP03 | Thomas Graber、Rahul Pandharipande；Michigan Math. J. 51(1) (2003)，93–110；[Crossref](https://api.crossref.org/works/10.1307/mmj/1049832895)。 | [v2 Appendix A.1](https://arxiv.org/abs/math/0104057v2)，本地 PDF pp.13–14。期刊题名用 **of**，预印本用 **on**；当前 bib 采用期刊题名正确。H/L 与本文 all-flags 的差异已说明。93–110 取 primary 记录，不改成二手所写 93–109；不声称读过不可取得的期刊 PDF。 |
| Wol86 | Scott A. Wolpert；Invent. Math. 85(1) (1986)，119–145；[Crossref](https://api.crossref.org/works/10.1007/BF01388794)。 | **§5.1，p.138** 的无标记 WP 类公式；标记/log kappa 由 MZ15 §2 补充。当前没有把 Wolpert 原文范围说成全标记情况。封面扫描的页码异文不覆盖正式 119–145。 |
| Mir07 | Maryam Mirzakhani；JAMS 20(1) (2007)，1–23；[本次 Crossref](https://api.crossref.org/works/10.1090/S0894-0347-06-00526-1) 与已读本地 AMS 已发表 PDF。 | Theorem 4.4（p.14）与 p.4 椭圆对合讨论；整个 (1,1) 长度多项式取半，而非只改常数。2006-03-08 是较早上线日期，不能据此将期刊年份改为 2006。本次 AMS 页面 403，未声称重新读取线上期刊全文。 |
| MZ15 | Maryam Mirzakhani、Peter Zograf；GAFA 25(4) (2015)，1258–1289；[Crossref](https://api.crossref.org/works/10.1007/s00039-015-0336-5)。 | [v1](https://arxiv.org/abs/1112.1151v1)，Theorem 1.2、Remark 1.3、§2。固定 n/固定阶展开和 c1(n)，不是本稿全图统一求和。v1 页面题名的 “asymtotics” 拼写不导入正式书目。其未定绝对常数不反向改写成当时已证明。 |
| EGGLS24 | Eynard、Garcia-Failde、Gregori、Lewański、Schiappa，顺序正确；Ann. Henri Poincaré 25(9) (2024)，4121–4193；[Springer](https://link.springer.com/article/10.1007/s00023-023-01412-z)。 | [v2](https://arxiv.org/abs/2305.16940v2)，§6.1，(6.10)；始终为 conditional resurgent prediction / a posteriori comparison，不输入 c2(0) 的无条件证明。本次 Crossref 只给较早 online 字段，完整卷页由出版社页面及既有原始记录核实，不能把缺字段当成尚未发表。 |
| FP03 | Carel Faber、Rahul Pandharipande；Ann. Math. 157(1) (2003)，97–124；[Annals 官方页](https://annals.math.princeton.edu/2003/157-1/p03)，DOI 10.4007/annals.2003.157.97。 | [v3，published version](https://arxiv.org/abs/math/9908052v3)，Theorem 1；稳定 genus-zero 是 (1)，beta_0=1 不指 Mbar_0,1 的积分。arXiv v3 的更新日期 2004、PDF 旧页眉均不替换正式 2003 卷年。引用积分公式，不伪造一般 Chow-class 推广。 |
| MaZ00 | Yuri I. Manin、Peter Zograf；Ann. Inst. Fourier 50(2) (2000)，519–535；[Crossref](https://api.crossref.org/works/10.5802/aif.1764) 及已读 Numdam 已发表 PDF。 | §6，(17)、**Proof 6.3 of Theorem 6.1**，pp.528–530；source x0 对应本文 R，两阶乘规范已译明。原 y0 负号不导入，本文正临界点另证。文献固定 genus / 标记数趋无穷，不替代本稿全类型/全树估计。本次 AIF URL 403，出版身份仍由直接 Crossref 和已有原文核实。 |
| Bur15 | Alexandr Buryak；CNTP 9(2) (2015)，239–271；[Crossref](https://api.crossref.org/works/10.4310/CNTP.2015.v9.n2.a1)。 | [v4](https://arxiv.org/abs/1308.5716v4)，Theorem 1.1，(1.1)–(1.2)，PDF p.2；保留本文变量译换。ILW 文献输入与本文 string/constants/characteristic/Borel 推导职责不同。 |
| Bur16 | Alexandr Buryak；Math. Res. Lett. 23(3) (2016)，675–683；[Crossref](https://api.crossref.org/works/10.4310/MRL.2016.v23.n3.a5)。 | [v2](https://arxiv.org/abs/1505.05911v2)，Theorem 1.1（PDF p.1）及 §2 短证明；正式卷页与 v2 页面一致。不把来源的形式结果说成本文所需统一复域已由其证明。 |
| FO90 | Philippe Flajolet、Andrew Odlyzko；SIAM J. Discrete Math. 3(2) (1990)，216–240；[Crossref](https://api.crossref.org/works/10.1137/0403019)。 | §2 方法级引用；本地作者预印本反序且文本映射坏，已有实际渲染核查，本文自证双主奇点转移。未捏造期刊版 theorem number；2006 数字化上线不替代 1990。 |
| CH88 | Maurizio Cornalba、Joe Harris；Ann. Sci. ENS，第 4 系列，21(3) (1988)，455–475；[Numdam](https://www.numdam.org/articles/10.24033/asens.1564/)、[Crossref](https://api.crossref.org/works/10.24033/asens.1564)。 | Theorem (1.3)，pp.457–458；a lambda-c delta 的 ample criterion 用 12>11。现有 series=4 字段身份正确；alpha 对 article 不显示 series 是版式行为，不是另一个期刊。 |
| Fuj78 | Takao Fujita；J. Math. Soc. Japan 30(4) (1978)，779–794；[J-STAGE](https://www.jstage.jst.go.jp/article/jmath1948/30/4/30_4_779/_article)、[Crossref](https://api.crossref.org/works/10.2969/jmsj/03040779)。 | Main Theorem (0.6)，pp.779–780；relative dualizing direct image 的 full-bundle semipositivity，非仅 determinant。当前 S8 的 semistable reduction 和 test-curve 条件保留。 |
| Kaw81 | Yujiro Kawamata；Compositio Math. 43(2) (1981)，253–276；[Numdam primary 期刊记录](https://www.numdam.org/item/CM_1981__43_2_253_0/)。 | Theorem 5，p.254；smooth base / SNC discriminant / unipotent monodromy 条件不省略，边界归约另由 LX26b。未核实 DOI，不新增猜测 DOI。 |

`KMZ96` 的已发表身份也由[本次 Crossref](https://api.crossref.org/works/10.1007/BF02101297)核实为 CMP 181(3) (1996)，763–787；删除的是未引数据库条目，相关正式出版信息仍在实际采用的 `KMZ96v1` note。

## 固定预印本的当前身份与定位

下列 arXiv 固定版本页面本次均实际取得。除 SW25 已有上述正式出版外，不凭没有 journal-ref 字段推断未来不会发表，也不添加未核实的期刊或 DOI。预印本 arXiv DOI 与期刊 DOI 不混同。

| Key / 实际版本 | 当前 primary 元数据与实际作用 |
| --- | --- |
| KMZ96v1 / [alg-geom/9604001v1](https://arxiv.org/abs/alg-geom/9604001v1)，1996-04-01 | Kaufmann、Manin、Zagier；(0.8)，Theorem 2.2 (2.6)，Lemma 2.2.1 (2.8)，(2.9)–(2.11)。AC、未发表 Faber–Zagier、早期 Zograf credit 均保留；原 cohomology 与本文 Chow 证明的地位不同。S6 的 (N-2)!(N-3)! 与 raw kappa/exponential 的换算已明确。 |
| SW25 / [2203.15681v4](https://arxiv.org/abs/2203.15681v4)，2025-06-04 | Yang Shen、Yunhui Wu；Lemma 14 p.11 回述 **Mirzakhani** comparisons，Lemma 18 p.12 为 **Shen–Wu** all-type bound。当前 S1 已准确分开，不因增加期刊字段而改变署名或编号。 |
| HMT25 / [2508.14874v2](https://arxiv.org/abs/2508.14874v2)，2025-11-15 | Will Hide、Davide Macera、Joe Thomas；Lemma 2.6，Theorems 4.2/4.3，(4.4)–(4.7)。主量词为固定展开阶、实际 genus/n/degree 阈值及多项式余项；全图求和是本文责任。当前无版本页也仍是 v2；保留其实际 500、c>max{600,C} 规范，不把固定 n 的其他来源偷换为 growing-valence 界。 |
| LX26 / [2610.33752v1](https://arxiv.org/abs/2610.33752v1)，2026-10-24 | Kefeng Liu、Hao Xu；Corollary 1.2 给绝对 leading constant；更高修正的 n 限制不扩展。当前无版本页仍 v1；不新增无根据的发表信息或优先权判断。 |
| W26 / [2610.35492v4](https://arxiv.org/abs/2610.35492v4)，2026-11-04 | 七位作者姓名与顺序匹配当前条目。Corollary 1.2，Lemma 6.1 (6.7)，Lemma 7.2，Appendix C.1 / (C.1)–(C.3)，§4.1 / (B.1) 均按 v4。signed profile、Y=0 common amplitude、complexity 到 1/G 因子已换算；HMT 负责增长价数桥。当前另有 v5，处理如上，不能直接换证明版。 |
| LX26b / [2610.39462v1](https://arxiv.org/abs/2610.39462v1)，2026-10-29 | Kefeng Liu、Hao Xu；S2 用 proof of Proposition 4.4 (4.2)–(4.3) 的 partial normalization；S8 才用 Proposition 4.4 的 full boundary nefness 和 Proposition 6.1 的 m=0 cover。不能混淆这两个使用层次。当前无版本页仍 v1。 |

本稿之外的撤回 Hua25/Huang 候选材料没有进入实际书目/证明输入，不为题名相近而新增条目。W26 v5 的其他谱论引用不自动成为本稿输入。

## DLMF 版本、访问日与精确条目

[官方 citation 页面](https://dlmf.nist.gov/help/cite)和[主页](https://dlmf.nist.gov/)本次均成功取得，支持 Release 1.2.8（2026-09-15）。当前十位编辑的名单与顺序正确；它是可更新的在线资源，访问日 2026-11-16 有实际依据。普通 DLMF label 的额外分组是既有 alpha 兼容修正，不能按官方示例表面少一层括号而撤销。

实际正文定位为：[25.6.2](https://dlmf.nist.gov/25.6.E2) 与 [25.2.1](https://dlmf.nist.gov/25.2.E1)（Bernoulli/zeta）；[10.21.15](https://dlmf.nist.gov/10.21.E15)（Bessel product）、[10.21.2](https://dlmf.nist.gov/10.21.E2)（interlacing）、[10.6.6](https://dlmf.nist.gov/10.6.E6) 和 [10.6.3](https://dlmf.nist.gov/10.6.E3)（derivatives）；B 用 [10.25.2](https://dlmf.nist.gov/10.25.E2)、[10.32.3](https://dlmf.nist.gov/10.32.E3)；S8 用 [10.8.2](https://dlmf.nist.gov/10.8.E2)、[10.5.2](https://dlmf.nist.gov/10.5.E2)。这些公式的实际用法沿用已完成的原始核查，未将 DLMF 基本恒等式归成本文全复域或全树估计的定理。

## LiuData26 的固定来源与可核实性

本次再次只读本地原 repository 的 Git 对象，确认 HEAD 与引用均为 **88dd4a501ecf3fbc124a823ad1589911f86a14e5**，author 为 Si-Qi Liu，author date 为 2026-11-10T00:08:19+08:00，origin 为 `git@github.com:siqiliu-tsinghua/hodge_data.git`。读取的是该固定提交的 README、NOTICE 和 Cargo.toml，没有修改 repo 或重算数据。README 的题名、g=2–20、19 份 exact rational tables 与条目一致；NOTICE 支持署名，并区分作者 wrapper 与已有计算引擎信用。不能把“精确有理表”改写成独立高亏格验证已经完成。

[固定提交的公开链接](https://github.com/siqiliu-tsinghua/hodge_data/tree/88dd4a501ecf3fbc124a823ad1589911f86a14e5)本次 web 取得结果为 **Cache miss**，因此不宣称网络页面或远端当前 HEAD 复核成功。来源身份依据用户提供的本地原 repo、固定 Git 对象和此前亲核的数据文件指纹，不虚构 DOI、期刊、发布日期或发布版本。2026 年字段与实际作者提交时间一致。

S8 末 Remark 仍直接 cite 此数据，只把所选 exact 观察转换成 scaled residual / adjacent extrapolation，候选常数另由 Bessel 值计算且明确为 conjecture。该数据不输入四定理证明，不证明余项率，不因删除旧 C 而失去直接来源。此前的数据转录/诊断核查可沿用，本任务没有重跑数据程序。正式引用中的 repository URL 与 commit 应保留；`allowbreak` 只影响印刷断行。

## 投稿资料与本次边界

- main 当前题名为 *On Large Genus Asymptotics of Pure Hodge Integrals*，署名 Si-Qi Liu，空 date，通用 article 格式。依用户决定保留作者姓名单独署名，不补猜测的 affiliation、email、基金、致谢、MSC 或期刊模板。
- 受保护的数学名称已在 bib title 中适当分组（Hodge、Gromov–Witten、Weil–Petersson、Masur–Veech、Dubrovin–Zhang、ILW、Kähler 等）。现有 alpha 不打印每个 doi/eprint/url 是样式选择，不等于字段不存在；固定版本需要的 note/howpublished 必须在最终内嵌书目中保留。
- 正式文章归属清楚区分：Mumford/FP 的 GRR，ABCDGLW 的一般图公式，MZ 固定标记输入，LX/W 的常数和 profiles，HMT 的量化一致余项，Mirzakhani 与 SW 的不同界，KMZ/MaZ 的经典 inverse，Buryak 的 ILW，FO 的方法。本文的全图/全树尾、自由能常数、统一复域和双奇点推导仍由文内论证负责。
- 高阶 supplementary Remarks 省略计算细节是用户授权的陈述范围；不因此升级主定理精度。S8 仍为固定 h 的 relative o(1)，背景比较 O_h(g^-1) 另列，末尾 h=1 refinement 为数值支持的猜想。书目更新不改变这些地位。
- 论文不依赖内部程序、Markdown、数据选择文件或执行说明补足证明。公开数据的规范信用应保留；工程材料不作为投稿附件。本记录不承诺已完成新的整体三审、编译或最终单 Tex 隔离运行。

在线限制的实际记录：AMS Mir07 页面及 AIF MaZ00 页面本次为 403，二者出版身份另由本次成功的 Crossref 和已读正式 PDF 核实；FP03 的 Crossref 首次为 429，官方 Annals 页及固定 arXiv v3 均成功；GitHub 固定提交页面为 Cache miss，按上文如实使用本地原始证据。不存在需要凭猜测补齐的科学引文。

后续由协调者统一实施共享条目和获授权的文字修改，再按真实冻结快照交原角色逐节审核；这份准备记录不能替代该签署。
