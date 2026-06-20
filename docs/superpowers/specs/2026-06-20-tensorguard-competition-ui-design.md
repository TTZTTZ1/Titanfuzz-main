# TensorGuard 作品赛演示界面设计

## 1. 设计目标

TensorGuard 的展示对象是信息安全作品赛评委。界面需要在短时间内同时证明：

1. 项目有明确的 API 支持范围和已确认缺陷证据。
2. 单 API 测试是真实运行的自动化流程，不是静态 PPT。
3. 已确认 Bug 可以在当前服务器环境中独立复现并形成证据报告。
4. 界面不把普通异常、候选问题或未经评估的崩溃直接宣称为安全漏洞。

## 2. 参考产品与可迁移方法

- [ClusterFuzz](https://google.github.io/clusterfuzz/using-clusterfuzz/ui-overview/)：测试用例、崩溃统计、复现可靠性和证据页是产品核心。TensorGuard 借鉴“具体触发程序 + 运行证据 + 复现结论”的组织方式。
- [GitHub Security Overview](https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-overview)：总览先给聚合事实，再下钻到具体问题。TensorGuard 不伪造历史趋势，但保留“概览→证据”的层级。
- [Semgrep Dashboard](https://semgrep.dev/docs/semgrep-appsec-platform/dashboard)：总览数据和优先发现可进一步筛选、导出。TensorGuard 借鉴结果筛选与报告出口。
- [SonarQube Issues](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving)：左侧筛选列表和右侧问题详情的主从式布局适合高密度审查。
- [Sentry Issue Details](https://docs.sentry.io/product/issues/issue-details/)：详情页首先显示错误摘要和影响，再展开技术证据。TensorGuard 的 Bug 页也应结论优先。

## 3. 选定的设计方向

### 3.1 信息结构

采用“成果表达 + 真实工作台”的混合式结构：

- 总览：静态事实与已确认证据。
- 单 API 运行：实时流程、图表和任务产物。
- Bug 复现：已确认 Bug、候选审查、当前环境证据和报告。

不新增独立的实验产物页、Prompt 库页、清理页或管理后台。

### 3.2 视觉语言

采用 `Graphite + Signal`：

- 石墨黑导航外壳，冷白工作区。
- 青绿表示正常流程与已复现证据。
- 琳珀表示运行中、超时或待审查。
- 红色表示进程崩溃、致命信号或失败。
- 不使用大面积渐变、发光元素、黑客大屏装饰或重复卡片堆叠。
- 主文字使用系统无衬线字体，代码和返回码使用等宽字体。
- 常规圆角 6px，边框和间距建立层级，阴影仅用于浮层。

## 4. 全局布局

- 桌面端左侧固定导航，仅显示总览、单 API 运行、Bug 复现。
- 导航底部显示当前环境是否就绪，不展开内部文件路径。
- 主工作区优先适配 16:9 现场演示屏，同时保证 1280px 桌面宽度可用。
- 窄屏时导航收缩为顶部栏，图表和代码证据转为上下布局。
- 所有运行按钮都有禁用、运行中、成功、失败和超时状态。

## 5. 总览页

总览只展示静态、可验证的项目事实，不画没有数据基础的时间曲线。

### 5.1 首屏内容

- API 支持范围：4,608。
- PyTorch API：1,568。
- TensorFlow API：3,040。
- 已确认 Bug：从已确认索引实时统计。
- 两个主操作：运行单 API、Bug 复现。

### 5.2 静态图表

- API 框架分布条。
- 已确认缺陷现象分布：进程/内存崩溃、Fatal Check/Assert、CPU/GPU 后端差异等。
- 自动化流程带：API 约束→Qwen 种子→InCoder 变异→CPU/GPU Oracle→复现证据。

### 5.3 证据表

列为 `ID | API | 失效类型 | 当前环境复现 | 证据状态`。

不展示未经评分方法支持的 High/Medium 安全严重度。严重度只能在后续完成威胁建模、输入合法性和可利用性分析后添加。

## 6. 单 API 运行页

### 6.1 选择与运行信息

- API 必须从 `data/torch_apis.txt` 或 `data/tf_apis.txt` 搜索选择，不接受任意 API 文本。
- 运行信息拆分为静态配置与动态状态。
- 静态配置：框架、API、Qwen/InCoder 模型、GPU 编号、模式和关键预算。
- 动态状态：已运行时间、当前阶段、进度、结束原因和错误。

### 6.2 三阶段主分析区

核心运算展示为三个可切换标签：

1. Qwen 种子生成。
2. InCoder 变异与验证。
3. Driver CPU/GPU 差异检测。

标签状态规则：

- `pending`：置灰并禁止点击。
- `running`：自动选中并实时更新。
- `success`：可点击回看完整数据。
- `failed`：可查看失败前数据和错误证据。
- `skipped`：置灰并说明未执行原因。

用户回看已完成阶段时，后台继续运行，界面不强制切回。提供“返回实时阶段”操作。

### 6.3 图表设计

不将所有数据塞进一张图，也不为每个字段单独建图。每个阶段使用一个主视图和必要的辅助组件：

- Qwen：每轮生成数、验证通过数、修复成功数。
- InCoder：累计生成、去重、可执行数的实时折线；Results 类型使用堆叠条。
- Driver：已检查程序进度、CPU/GPU 一致数、差异 Catch 数和证据列表。以进度条和结果组成为主，不强行使用折线。

GPU 利用率、显存占用和峰值显存贯穿整个 Job 采集，放入默认折叠的“系统监控”区。

### 6.4 Results 语义

所有分类数量都显示，但不都宣称为 Bug：

- `seed`：初始可用种子。
- `valid`：正常执行的变异程序。
- `exception`：可捕获异常，默认不是 Bug。
- `crash`：清洁子进程中仍复现的崩溃，强候选。
- `hangs`：超时或疑似卡死。
- `flaky`：二次验证不稳定。
- `notarget`：变异后目标 API 丢失。

### 6.5 实时数据

新增每个 Job 的 `metrics.jsonl`。任务在轮次、分类数或阶段变化时追加结构化事件。前端轮询增量数据，不从终端文本猜数值。

最小事件字段包括：`timestamp, stage, round, generated, duplicated, valid, exception, crash, hangs, flaky, notarget, generation_seconds, validation_seconds`。GPU 采集记录 `utilization, memory_used, memory_total`。

## 7. 任务与 Results 存储

单 API 网页运行保持两层结果：

1. `demo_runs/api_jobs/<job_id>/Results/<lib>/`：运行中产物、实时图表、日志和完整历史。
2. `Results/<lib>/`：Job 成功后发布的每个 API 最新正式结果。

重跑同一 API 时，只替换顶层 Results 中该 API 的旧文件，不影响其他 API。运行中和失败 Job 不污染正式 Results。

作品赛演示不会频繁运行，因此保留全部 Job，不实现自动清理页或后台清理策略。

## 8. 候选问题审查

### 8.1 边界

网页不允许将一次异常直接标记为“已确认 Bug”，也不实现自动最小化。

主流程为：

`Results 原始结果→系统推荐候选→用户加入审查队列→独立复现与人工判断→仓库录入已确认 Bug`。

### 8.2 推荐规则

自动建议但不自动加入：

- 清洁进程仍复现的 crash。
- 稳定 hang。
- INTERNAL ASSERT 或 Fatal Check。
- CPU/GPU 输出或异常不一致。

普通 exception、notarget 和 flaky 默认不推荐，但允许用户手动选择具体程序。

### 8.3 候选索引

候选标记对象是具体 Job 中的具体 `.py` 文件，不是整个 API。候选索引保存：

- Candidate ID、Job ID、框架和 API。
- 原始分类和 Job Results 内不可覆盖的文件路径。
- 源码 SHA-256、初始错误类型、创建时间和审查状态。

为减少重复文件，候选阶段不复制源码，直接引用保留的 Job Results。相同源码哈希不重复创建。

状态为 `pending_review, reproduced, needs_review, rejected, promoted`。网页只允许排除/归档，不提供物理删除和直接确认 Bug。

## 9. Bug 复现页

### 9.1 页面结构

- 左侧为已确认 Bug/候选审查标签、搜索和筛选列表。
- 右侧首先显示当前环境复现结论。
- 结论下方显示“合理行为 vs 实际行为”，解释为什么值得视为框架缺陷证据。
- 最小复现代码和当前运行输出并排展示。
- 将信号、返回码、超时和子进程崩溃翻译为人可理解的证据。
- 已有报告时操作显示为“查看报告”。

### 9.2 实际设备判定

`CUDA_VISIBLE_DEVICES=0` 只代表 GPU 可见，不代表目标 API 在 GPU 执行。复现结论必须记录实际 Tensor/device 路径。无法确定时显示 `unknown`，不根据 GPU 可见性猜测。

## 10. 报告

### 10.1 生成与保留

- `report.md` 是唯一正式源文件，每个 Repro Job 只生成一次。
- 已存在时接口直接返回原报告，不覆盖。
- 网页渲染 Markdown，并支持浏览器打印/导出 PDF。
- 重新复现会创建新 Repro Job 和新报告，历史证据不覆盖。
- Job ID 只保存在内部状态和附件关联中，不出现在正文。

### 10.2 报告内容

1. 报告 ID、Bug/Candidate ID、API、类型和生成时间。
2. 当前环境复现结论和命中次数。
3. 合理行为与实际行为。
4. 每个执行配置的实际设备、返回码、信号、耗时和判定。
5. 最小复现源码与输出摘要。
6. Python、操作系统、框架、CUDA Runtime 和 GPU 环境。
7. 适用范围、未确定根因、未评估安全影响等限制。
8. 源码与日志 SHA-256、原始附件路径。

### 10.3 结论规则

大模型不参与证据结论。报告采用：

`结构化证据提取→确定性规则分类→模板表达→未知类型回退人工审核`。

自动类型包括正常退出、操作系统信号、allocator/memory corruption、Internal Assert/Fatal Check、CUDA device-side assert、CPU/GPU 输出或异常不一致、超时、OOM、普通异常和未知非零返回码。

模板只描述可观测现象，不推断源码根因、可利用性、修复方案或安全严重度。候选报告的结论必须说明“已复现异常，是否属于框架缺陷仍需人工审查”。

## 11. 错误处理

- 模型、Prompt、种子或 GPU 环境不可用时，当前阶段失败，后续阶段标记为 skipped。
- 图表缺少数据时显示具体空状态，不生成示意曲线。
- 日志无法解析时保留原文，结论进入 needs_review。
- 候选引用的 Job 文件不存在时显示证据缺失，不静默跳过。
- 报告已存在时只读返回，不重新计算或覆盖。

## 12. 可访问性与验证

- 状态不只依赖颜色，同时显示文字和图标。
- 所有标签、图例和返回码在 1280px 以上无截断。
- 支持键盘选择 API、切换阶段和浏览 Bug 列表。
- 实时图表尊重 `prefers-reduced-motion`。
- 使用浏览器完整验证总览、单 API 运行、阶段回看、候选加入、Bug 复现、报告幂等和 PDF 打印流程。

## 13. 明确不做

- 不允许网页用户直接将候选标记为已确认 Bug。
- 不实现自动最小化、自动源码根因定位或自动修复。
- 不使用大模型生成证据结论。
- 不输出无依据的 CVSS、High/Medium 安全严重度。
- 不实现多用户、角色权限、硬删除、自动磁盘清理和后台任务调度管理。
- 不在总览展示虚构趋势或将少量演示运行冒充为全量实验结果。

## 14. 验收标准

1. 评委在总览首屏可看到真实 API 支持范围、已确认 Bug 数和直接演示入口。
2. 单 API 任务启动后，三阶段状态、实时指标、GPU 监控和日志与实际进程一致。
3. 未运行阶段无法打开空图，已完成阶段可回看。
4. Results 七类数据语义清晰，不将异常数量直接表述为 Bug 数。
5. 具体生成程序可加入候选队列，重跑同一 API 不破坏旧候选引用。
6. Bug 复现页能解释返回码、信号、实际设备和判定原因。
7. 同一 Repro Job 的报告重复请求不覆盖原报告，新复现 Job 可生成新报告。
8. 未知异常被明确标记为需人工审核，系统不猜测根因或安全影响。
