# FDE Knowledge Base · 前沿部署工程师知识库

> 一个系统化沉淀 **Forward Deployed Engineer（FDE，前沿部署工程师）**优质资源的开源知识库。
> 覆盖概念认知、学习路线、开源教程、课程认证、面试准备、薪资报告、招聘公司、咨询机构、工具生态与实战案例。

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Resources](https://img.shields.io/badge/Resources-92-blue.svg)](#资源索引)
[![Last Update](https://img.shields.io/badge/Updated-2026--10-orange.svg)](CHANGELOG.md)

---

## 什么是 FDE

FDE（Forward Deployed Engineer，前沿部署工程师）由 **Palantir** 在 2000 年代中期开创，
2025–2026 年因 AI 落地潮被 OpenAI、Anthropic、Google Cloud、Scale AI 等公司重新推上风口。

一句话定义（来自多个权威来源的共识表述）：

> **FDE 是驻扎在客户现场、亲手写生产代码并对业务结果负责的工程师。**
> 他们既做顾问的工作（找到真问题），也做工程师的工作（把系统建起来），并且一直负责到系统被真正用起来。

Palantir 官方给出的区分最为凝练：

| 角色 | 面对的对象 | 交付物 |
|------|-----------|--------|
| 产品工程师 | 一个能力 | 多个客户 |
| FDE | 一个客户 | 多个能力 |

**为什么现在火？** 核心矛盾不是模型不够强，而是「模型能力 → 业务可用系统」之间存在巨大的工程与整合落差。
MIT NANDA 2025 年研究（被广泛引用）称：**95% 的企业 AI 试点因缺少人工部署支持而未能产生可衡量的业务影响**。

---

## 资源索引

### 🧭 认知入门 —— 先搞清楚这个岗位到底是什么

| 资源 | 说明 |
|------|------|
| [The New Stack · Why OpenAI and Anthropic are hiring FDE teams](https://thenewstack.io/forward-deployed-engineers-ai/) | ⭐ 媒体深度解读：为什么 AI 比传统软件更需要 FDE，解释了「概率性系统风险」这一关键论点 |
| [Palantir 官方 · A Day in the Life of a Forward Deployed Software Engineer](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1) | ⭐ 一手资料：Palantir 官方博客 2020 年文章，岗位的「原教旨」版本 |
| [The Pragmatic Engineer · The Pulse: FDE heats up again](https://www.worldprogramming.org/posts/the-pulse-forward-deployed-engineering-heats-up-again-fwutf0) | ⭐ Gergely Orosz 解读 Google/OpenAI/Anthropic 三家的 FDE 招聘动向，附 OpenAI Deployment Company 背景 |
| [explainx.ai · Forward Deployed vs Frontier Deployed vs Applied AI Engineer](https://explainx.ai/blog/what-is-a-frontier-deployed-engineer-forward-deployed-engineer-explained-2026) | 把 FDE / Frontier DE / Applied AI Engineer / CE / SA 的命名差异讲得最清楚的一篇 |
| [theforwarddeployed.io · The Job, Week to Week](https://www.theforwarddeployed.io/the-job) | 罕见的「诚实拆解」：出差比例、一周时间分配、各来源数据互相矛盾之处都摊开讲 |
| [Determinant Studios · What Is a Forward Deployed Engineer](https://determinantstudios.com/blogs/what-is-a-forward-deployed-engineer) | 面向商业决策者，FDE vs 顾问 vs 外包开发对比表清晰，附衡量指标 |
| [Dexity · Forward Deployed Engineer — The Complete 2026 Guide](https://dexity.com/intel/forward-deployed-engineer-2026) | 数据最全的一篇：187 份 JD 扫描、技能需求百分比、薪资、面试三轮结构、适合/不适合谁 |
| [beyondelevation · FDE for Startups](https://beyondelevation.com/insights/forward-deployed-engineer-for-startups) | 从创业公司视角看 FDE，并直指「顾问换皮」的质疑，给出辨别方法 |

📄 更多：[完整认知入门清单](docs/01-认知入门.md)

---

### 🗺️ 学习路线 —— 从零到能接活的系统路径

| 资源 | 语言 | 说明 |
|------|------|------|
| [xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer](https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer) | 🇨🇳 中文 | ⭐⭐ 5k+ star，从零入门指南，借用了《增长黑客》的叙事框架，中文圈最火 |
| [pierpaolo28/Awesome-FDE-Roadmap](https://github.com/pierpaolo28/Awesome-FDE-Roadmap) | 🇬🇧 英文 | ⭐⭐ 1.3k star，史上最完整的 FDE 路线图，含 GCP/VPC-SC/ATO/IL5/ITAR 等「离线与涉密部署」硬核内容 |
| [RichardXu001/the-fde-handbook](https://github.com/RichardXu001/the-fde-handbook) | 🇨🇳 中英 | ⭐《FDE：企业 AI 落地实战手册》开源手册，中英双语，偏实操 |
| [feigaobox10/fde-reader](https://github.com/feigaobox10/fde-reader) | 🇨🇳 中文 | 《FDE 入门到精通》开源电子书，八堂课讲透如何把 AI 送进客户现场 |
| [VanGong1999/FDE](https://github.com/VanGong1999/FDE) | 🇨🇳 中文 | 收集 FDE 全部相关内容，AI Agent / RAG / 推理优化 / vLLM·SGLang 部署全覆盖 |
| [lunar-arun/Forward-Deployed-Engineer](https://github.com/lunar-arun/Forward-Deployed-Engineer) | 🇬🇧 英文 | 完整学习路线：AI agents → MCP → RAG → eval |
| [yeasy/forward_deployed_engineering_guide](https://github.com/yeasy/forward_deployed_engineering_guide) | 🇨🇳 中文 | 前线部署工程最佳实践指南，yeasy（Docker Compose 作者）出品 |
| [thecoder8890/forward-deployed-engineer-roadmap](https://github.com/thecoder8890/forward-deployed-engineer-roadmap) | 🇬🇧 英文 | 从编码、系统设计到客户问题的实践路线 |
| [wmc837911722-del/fde-learning](https://github.com/wmc837911722-del/fde-learning) | 🇨🇳 中文 | 24 周成长手册，贯通商业决策→一线问题发现→RAG/MCP 交付→运营交接 |
| [360digitaltransformation · FDE Roadmap 2026](https://www.360digitaltransformation.com/pages/forward-deployed-engineer-roadmap) | 🇬🇧 英文 | 7 阶段路线图，每阶段标注周数与「此阶段真正要解决的问题」 |
| [cloudsoftsol · FDE Engineer Roadmap](https://cloudsoftsol.com/blog/fde-engineer-roadmap) | 🇬🇧 英文 | 7 阶段技能路线，每阶段含里程碑项目 + 验收清单 + 常见陷阱 |

📄 更多：[完整学习路线清单](docs/02-学习路线.md)

---

### 📚 开源教程与手册 —— 可精读的系统性材料

| 资源 | 说明 |
|------|------|
| [global-fde/awesome-fde-resources](https://github.com/global-fde/awesome-fde-resources) | ⭐ 298★ 社区维护的精选合集：工具、实践、案例与机会 |
| [calmrocks/ai-engineer-notebooks](https://github.com/calmrocks/ai-engineer-notebooks) | ⭐⭐ 698★ 无框架依赖的 Colab 笔记本，FDE 技能集的动手练习 |
| [liuhuanyong/FDEGreenBook](https://github.com/liuhuanyong/FDEGreenBook) | ⭐ 自包含交互式网站：教程 + 游戏 + 画像测试三合一，中文社区活跃 |
| [FDEInfra/FDEBook](https://github.com/FDEInfra/FDEBook) | OpenFDE 开放知识库与社区（open-fde.com） |
| [goday-org/FDE-Handbook](https://github.com/goday-org/FDE-Handbook) | 生产就绪手册：企业 landing zone、VPC 服务边界等 |
| [dawei008/fde-book](https://github.com/dawei008/fde-book) | OpenBook Vol II · AI 应用的落地工程学，核心公式 `Outcome = Harness × Customer` |
| [anjor/fde-advisory-materials](https://github.com/anjor/fde-advisory-materials) | FDE 咨询顾问的开放方法论材料（Platypus Technologies） |
| [mchittineni/ultimate-ai-engineering-guide](https://github.com/mchittineni/ultimate-ai-engineering-guide) | 100+ AI/LLM/Agentic AI/FDE 综合指南 |
| [jiji262/fde-guide](https://github.com/jiji262/fde-guide) | 《从零到 FDE：AI 时代前线部署工程师转型实战课》 |
| [JayceHuang/fde-handbook](https://github.com/JayceHuang/fde-handbook) | FDE 现场工程手册 |

📄 更多：[完整教程清单](docs/03-开源教程与手册.md)

---

### 🎓 课程与认证 —— 付费但成体系的学习路径

| 平台 | 说明 |
|------|------|
| [FDE Academy (Futurense)](https://www.fde.academy/) | ⭐ 32 周 / 8 个月 PGP，双轨（技术 + 咨询）+ IIT 认证环节，约 80 席限额，录取平均 8.8 年经验 |
| [Scaler · AI Forward Deployed Engineer](https://www.scaler.com/) | 12 个月课程，含 FDE Lab 客户模拟 + 公开作品集路径，2 万+ 校友 |
| [Platypus Technologies · FDE Academy](https://platypustech.xyz/) | 面向咨询与技术服务公司的 **FDE 能力建设**：课程设计 + 人才招聘体系 + 运营模式咨询 |
| [Ultralab · Scaler vs FDE Academy 横评](https://www.appliedaicourse.com/blog/scaler-vs-fde-academy-comparison-for-the-forward-deployed-engineer-role) | 第三方中立对比，两条路线的取舍写得很实在 |

> ⚠️ **重要提醒**：目前市面上的 FDE 课程多为 2026 年新入场者，**几乎都没有真实的毕业成果数据**（薪资多为预测值）。
> 付费前务必核查：真实学员就业率、可验证的学员作品集、导师是否真的是一线 FDE。
> 参见 [Global-FDE 教学质量红旗清单](https://platypustech.xyz/)。

📄 更多：[完整课程认证清单](docs/04-课程与认证.md)

---

### 🎤 面试准备 —— FDE 面试的独特考察点

| 资源 | 说明 |
|------|------|
| [YagyanshB/google-fde-interview-guide](https://github.com/YagyanshB/google-fde-interview-guide) | ⭐ 380★ Google FDE 面试指南 |
| [dataPro-lgtm/fde-interview-fieldbook](https://github.com/dataPro-lgtm/fde-interview-fieldbook) | ⭐ 一手资料支撑的生产导向面试战手册，含案例、评分卡与岗位研究 |
| [vivianaranha/fde-interview-mastery](https://github.com/vivianaranha/fde-interview-mastery) | 面试精通系列 |
| [cma0232/forward-deployed-engineer-interview-guide](https://github.com/cma0232/forward-deployed-engineer-interview-guide) | FDE 面试类型、轮次与准备策略 |
| [pingananth/fde-decomp-interview-guide](https://github.com/pingananth/fde-decomp-interview-guide) | 专攻「分解式面试」与客户场景模拟 |
| [bicced/ai-engineer-interview-handbook](https://github.com/bicced/ai-engineer-interview-handbook) | Applied AI Engineer / FDE 面试题与手册 |
| [cma0232/genai-architecture-guide](https://github.com/cma0232/genai-architecture-guide) | 生产级 GenAI 架构设计，直接对应 FDE 系统设计轮 |
| [rishabhsaini282/forward-deployed-ai-engineer-data](https://github.com/rishabhsaini282/forward-deployed-ai-engineer-data) | 90 天转型计划 + 50 道面试题与答题框架 |
| [Evan-Marsh/fde-coding-interview](https://github.com/Evan-Marsh/fde-coding-interview) | 《AI FDE 编程面试》配套验证代码 |

**三轮结构共识**（来自 Dexity 187 份 JD 分析）：
1. **行为与姿态筛查**（45–60 分钟）—— 测你在范围模糊下的Ownership，不是文化匹配
2. **技术深挖**（2 轮 × 60–75 分钟）—— 现场 API 编排、云 IAM、数据解析、系统设计；**基本不考 LeetCode**
3. **分解案例 + 客户模拟** —— 给一个模糊的企业问题，现场演示如何拆解

📄 更多：[完整面试资源清单](docs/05-面试准备.md)

---

### 💰 薪资与市场报告 —— 数据源与结论

| 资源 | 关键数据 |
|------|---------|
| [Perspective AI · 2026 FDE 薪酬报告（1,200 人样本）](https://getperspective.ai/blog/2026-forward-deployed-engineering-compensation-report-1200-fdes) | ⭐ 样本最全：Palantir FDSE 中位数 $215K → Anthropic principal $1.2M+，分四档 |
| [Aced（原 Exponent）· 18 家公司 FDE 薪资](https://www.aced.io/jobs/fde/salary) | ⭐ 135 份在招 JD 分析：美国中位 base 约 $190K，多数落在 $160K–$220K |
| [forwarddeployedhq · OpenAI vs Anthropic vs Palantir](https://forwarddeployedhq.com/blog/forward-deployed-engineer-salary-in-2026-openai-vs-anthropic-vs-palantir) | 把 base / total comp / 股权占比三层拆开讲，纠正了很多混淆 |
| [fdenest · FDE Salary 2026](https://fdenest.com/guides/forward-deployed-engineer-salary) | 按级别 + 公司 + 城市三重维度；纽约已超旧金山成为第一招聘地 |
| [fde-engineers.com · FDE Salary Guide 2026](https://fde-engineers.com/articles/fde-salary-guide-2026) | 交叉校验版，附带谈 offer 的实操建议 |
| [Dexity · FDE 2026 报告](https://dexity.com/intel/forward-deployed-engineer-2026) | 191 个在招岗位扫描，33% 披露薪资带，中位 $146K–$240K |

**核心结论**：这个岗位的**分差几乎全部来自股权**，不是 base。
前沿实验室股权占总包 60–70%，Palantir 40–55%，财富 500 强企业 AI 团队仅 15–25%。

📄 更多：[完整薪资报告清单](docs/06-薪资与市场.md)

---

### 🏢 招聘公司与岗位 — 谁在招 FDE

**第一梯队（定义了这个岗位）**
- **Palantir** — 岗位 originator，内部称 "Deltas"，至今最大的 FDE 组织

**前沿实验室**
- **OpenAI** — 2025 年组建 FDE 团队，Colin Jarvis 负责；2026 年 5 月成立 The OpenAI Deployment Company（40 亿美元私募，估值 140 亿），收购英国 Tomoro（约 150 名 FDE）
- **Anthropic** — "Forward Deployed Engineer, Applied AI"；2026 年 7 月成立 FDE 咨询业务（投资方含 Blackstone、Hellman & Friedman、Goldman Sachs）
- **Google Cloud** — 2026 年单年招聘 59 名 FDE，隶属新设 AI 专精 GTM 组织，面试从 4–6 轮压缩到 2 天内 2 轮

**规模化应用 AI 阵营**
- Scale AI、Databricks、Ramp（约 15 人 pod 制）、Salesforce、AWS、Microsoft、Snowflake、Cohere、C3.ai

**前沿应用 AI 创业公司**
- Sierra、Perplexity、Cursor、Mistral、Commure、Gecko Robotics、Lindy

**咨询与传统 IT 服务商（已开始贴标签）**
- Deloitte（专设 FDE 服务页，19 个在招岗位）、Fujitsu（FDE + 顾问打包销售）、McKinsey QuantumBlack、Accenture AI

> 📌 **实时岗位跟踪**：[landedjobs/forward-deployed-engineer-jobs](https://github.com/landedjobs/forward-deployed-engineer-jobs)（每 2 天自动刷新）
> 📌 **中国区名录**：[shike/fde.dropleap.cn](https://github.com/shike/fde.dropleap.cn)

---

### 🧩 咨询与服务商 — 找 FDE 服务时看这里

| 机构 | 定位 |
|------|------|
| [Platypus Technologies](https://platypustech.xyz/) | ⭐ FDE 运营模式咨询 + 招聘体系设计 + FDE Academy 课程设计；Anjor Kaneker 的 Palantir FDE 复盘被 The Pragmatic Engineer 专文报道 |
| [FDE Academy](https://www.fde.academy/) | 人才输送 + 企业内训双线；与 AIM Research 联合调研：95% 机构有 FDE 需求，仅 45% 能获得匹配人才 |
| [Beyond Elevation](https://beyondelevation.com/) | 面向创业公司的 FDE 高管 fractional 运营者；提供 2 周 AI 审计（$3,000）到完整项目（$30,000+） |
| [Deloitte FDE 服务](https://www2.deloitte.com/) | 传统咨询巨头已正式设立 FDE 服务线 |
| [Mirage Metrics](https://miragemetrics.com/blog/what-is-forward-deployed-engineering) | 工业领域 FDE 服务商（法国、西班牙、摩洛哥等），其工程流程记录写得非常透明 |
| [Determinant Studios](https://determinantstudios.com/) | 提供 FDE 式交付的定制开发 |

📄 更多：[完整咨询机构清单](docs/07-咨询与服务商.md)

---

### 🛠️ 工具、Agent Skills 与工程实践

**FDE 专用 Harness / 工作台**

| 工具 | 说明 |
|------|------|
| [suboss87/FDEOps](https://github.com/suboss87/FDEOps) | ⭐ 962★ 面向 AI 编码 Agent 的 FDE 技能包，生态最成熟 |
| [AgnesAI-Labs/agnes-harness](https://github.com/AgnesAI-Labs/agnes-harness) | ⭐ 430★ 可插拔 FDE Agent Harness，核心是「为信任而生」 |
| [rpraharaj/forward-deployed-engineer](https://github.com/rpraharaj/forward-deployed-engineer) | 43 个 Claude Code 技能：落地陌生代码库、从需求带到上线 |
| [Dan-Cleary/fdestack](https://github.com/Dan-Cleary/fdestack) | Claude Code 技能包：客户上下文 → discovery → scope → 价值论证 → POC |
| [anjor / fde-advisory-materials](https://github.com/anjor/fde-advisory-materials) | 顾问视角的开源方法论与模板 |
| [frank666199/Frank-FDE-Skills](https://github.com/frank666199/Frank-FDE-Skills) | 🇨🇳 70 个实战技能覆盖 10 大维度，Echo 业务向 + Delta 技术向双轨模型 |
| [gxfde/fde-workbench](https://github.com/gxfde/fde-workbench) | 开源 FDE 项目工作台：调研、机会识别、交付、团队协作 |
| [mollyretter/forward-deployed-engineer-toolkit](https://github.com/mollyretter/forward-deployed-engineer-toolkit) | 有主见的 AI 落地工具集 |

**实战模拟与训练环境**

| 工具 | 说明 |
|------|------|
| [deeplethe/fde-gym](https://github.com/deeplethe/fde-gym) | ⭐ 92★ LLM 时代的在线判题器：每个案例都是一次真实客户交付，配合编码 Agent 完成 |
| [kalyvask/fde-simulation](https://github.com/kalyvask/fde-simulation) | FDE 角色模拟：为一个企业项目定范围、构建、交付 |
| [Organized-AI/fde-training-lab](https://github.com/Organized-AI/fde-training-lab) | 实战课程与 CLI |
| [vivianaranha/Forward-Deployed-Engineer](https://github.com/vivianaranha/Forward-Deployed-Engineer) | 100 个可用于作品集的项目 |

📄 更多：[完整工具与 Skills 清单](docs/08-工具与工程实践.md)

---

### 📂 实战案例与作品集 — 最有说服力的证据

| 资源 | 说明 |
|------|------|
| [guminghao-avi/FDE-case-library](https://github.com/guminghao-avi/FDE-case-library) | FDE 案例库 |
| [rickeyhuanghub/ForwardDeployedEngeering](https://github.com/RickeyHuangHub/ForwardDeployedEngeering) | 面向实体制造业的落地体系，收录中英文官方白皮书 |
| [Dgannon/Forward-Deployed-AI-Engineer-Playbook](https://github.com/dgannon/Forward-Deployed-AI-Engineer-Playbook) | FDE 的全套「打法」手册 |
| [cmangun/field-deployed-engineer](https://github.com/cmangun/field-deployed-engineer) | 受监管环境中的生产 AI 系统作品集 |
| [anix-lynch/healthcare-forward-deployed-engineer](https://github.com/anix-lynch/healthcare-forward-deployed-engineer) | 医院 VPC/本地部署的 ER 分诊助手，含完整 discovery 流程 |
| [atulkapor/fde-framework](https://github.com/atulkapoor/fde-framework) | AI 建设之前的决策框架：证据进、带凭据的架构出 |

**作品集标准结构**（源自 alphalab.site 的实践总结，中文社区已广泛采用）：

```
fde-case-study/
├── discovery-brief.md        # 用户、触发事件、输入输出、人工复核、不可碰的边界
├── architecture.md           # 架构与取舍
├── acceptance-criteria.md    # 什么算通过、什么必须回退人工
├── evals/
│   ├── golden-set.jsonl
│   └── results.json          # 基准、版本变更、错误分类
├── app/
│   └── runbook.md            # 运维手册
├── incident-postmortem.md    # 事故复盘
└── case-study.md             # 使用者、原流程、痛点、基准值、非目标
```

---

## 🔍 快速导航：按你的目的选

| 我想…… | 建议路径 |
|---------|---------|
| **搞懂 FDE 是什么** | [The New Stack](https://thenewstack.io/forward-deployed-engineers-ai/) → [Palantir 官方](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1) → [theforwarddeployed.io](https://www.theforwarddeployed.io/the-job) |
| **系统学习转行** | [Awesome-FDE-Roadmap](https://github.com/pierpaolo28/Awesome-FDE-Roadmap) → [the-fde-handbook](https://github.com/RichardXu001/the-fde-handbook) → [ai-engineer-notebooks](https://github.com/calmrocks/ai-engineer-notebooks) 动手 |
| **找中文入门资料** | [FDE 从零入门指南](https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer) → [FDE 入门到精通](https://github.com/feigaobox10/fde-reader) → [FDEGreenBook](https://github.com/liuhuanyong/FDEGreenBook) |
| **准备面试** | [dataPro 面试战手册](https://github.com/dataPro-lgtm/fde-interview-fieldbook) → [fde-gym 实战](https://github.com/deeplethe/fde-gym) → [GenAI 架构设计](https://github.com/cma0232/genai-architecture-guide) |
| **了解薪资行情** | [Perspective 1200 人报告](https://getperspective.ai/blog/2026-forward-deployed-engineering-compensation-report-1200-fdes) → [Aced 18 公司对比](https://www.aced.io/jobs/fde/salary) |
| **企业要落地 AI** | [Platypus 方法论](https://platypustech.xyz/) → [the-fde-handbook](https://github.com/RichardXu001/the-fde-handbook) → [Mirage Metrics 工业实践](https://miragemetrics.com/blog/what-is-forward-deployed-engineering) |
| **给 Agent 装 FDE 能力** | [FDEOps](https://github.com/suboss87/FDEOps) → [agnes-harness](https://github.com/AgnesAI-Labs/agnes-harness) → [43 个 Claude Code 技能](https://github.com/rpraharaj/forward-deployed-engineer) |

---

## 🧭 本库的核心观点

这些是我们在筛选资源过程中反复验证、值得单独拎出来的判断：

**1. FDE 的核心矛盾是「模糊」，不是「技术难度」**
OpenAI FDE 负责人 Colin Jarvis 的原话：*"FDEs work in a ton of ambiguity, and often what the customer describes in scoping doesn't match the data/system reality on the ground."*
所以 FDE 面试真正考的是：范围模糊时的拆解能力、客户管理、对自己作品的负责程度。

**2. AI 项目失败几乎不发生在 Demo 阶段**
[MIT NANDA 研究](https://explainer>>)称 95% 企业 AI 试点无可衡量影响。失败发生在**集成、可靠性、安全审查、采纳**这四个环节 —— 而传统交付模式（内部团队做完就撤、顾问按合同结束）恰好在这四个环节上放弃所有权。

**3. 「FDE 是不是顾问换皮」是个严肃质疑**
HN 上「Rise of the Forward Deployed Engineer」讨论中最高赞批评称其为「企业软件史上最大的 rebranding」。
**辨别方法**：问一句「谁登录我们的系统、哪一周交付第一个可用版本」。答案有名有姓有日期 = 部署；答案是分阶段方案 = 换皮咨询。

**4. 时间分配现实与招聘广告不符**
职位广告常写「70–90% 写代码」，但把 Google 岗位描述逐条解码后的估算、以及从业者的一手记录都指向**编码仅占约 25–50%**，其余是集成、管道、对客沟通。
规划职业路径时应按低值预期。

**5. 作品集 > 简历**
这个岗位是「按证据招聘」的。Anthropic L4 的年股权 vest 约值 $445K —— 但前提是估值站得住。
更有说服力的是：你能说清一个真实部署在什么环境跑、为什么这么设计、什么时候坏的。

---

## 📁 仓库结构

```
fde-knowledge-base/
├── README.md                    # 主索引（本文件）
├── CHANGELOG.md                 # 更新记录
├── CONTRIBUTING.md              # 收录标准与贡献指南
├── LICENSE                      # CC BY 4.0
├── docs/                        # 分类资源清单
│   ├── 01-认知入门.md
│   ├── 02-学习路线.md
│   ├── 03-开源教程与手册.md
│   ├── 04-课程与认证.md
│   ├── 05-面试准备.md
│   ├── 06-薪资与市场.md
│   ├── 07-咨询与服务商.md
│   └── 08-工具与工程实践.md
├── data/
│   └── resources.json           # 结构化数据，便于二次检索
└── scripts/                     # 抓取与清洗脚本（可复现）
    ├── fetch_github.py
    ├── filter_repos.py
    └── clean_repos.py
```

---

## 🤝 贡献

欢迎补充资源，但请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 的收录标准 —— 我们**宁缺毋滥**，不接受营销软文。

**一条原则**：能进这个库的资源，必须满足「有实质内容 / 有可验证产出 / 作者是一线实践者」三者之一。

---

## 📌 数据说明

- 数据采集时间：**2026 年 10 月**
- Star 数为采集时快照，会随时间变化
- 薪资数据来自公开自陈（Glassdoor/Levels.fyi）与强制披露 JD，受地区与时间影响，**请作为区间参考而非精确报价**
- 本库仅做资源聚合与观点索引，**不对任何课程/服务做背书**

## 📄 License

内容采用 [CC BY 4.0](LICENSE) 协议。代码脚本采用 MIT 协议。