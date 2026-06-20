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
- 导航底部显示当前环境是否就绪和实时检测到的 GPU 型号，不展开内部文件路径。
- 点击环境状态打开“运行环境”抽屉，展示实时采集的操作系统、Python、PyTorch、TensorFlow、CUDA、GPU 型号、驱动和显存。
- 主工作区优先适配 16:9 现场演示屏，同时保证 1280px 桌面宽度可用。
- 窄屏时导航收缩为顶部栏，图表和代码证据转为上下布局。
- 所有运行按钮都有禁用、运行中、成功、失败和超时状态。

## 5. 展示数据真实性与环境采集

### 5.1 基本原则

- 产品名称、页面标题、流程阶段和状态说明可以是静态界面文案。
- API 数量、Bug 数量、Results 数量、模型名称、运行参数、框架版本、CUDA、GPU 型号、显存和任务状态不允许在前端写死。
- 缺少或采集失败的字段显示“未检测到”和失败原因，不用示例值填充。
- 每组环境与实时指标返回 `collected_at`，前端显示最后刷新时间；超过有效期时显示“数据可能过期”。
- 视觉草图中的 `PyTorch 2.11.0`、`CUDA 13.0`、`A800` 等只是版式示例，不得进入正式默认数据。

### 5.2 数据源审计表

| 展示项 | 真实数据源 | 刷新时机 | 失败回退 |
| --- | --- | --- | --- |
| PyTorch API 数 | `data/torch_apis.txt` 去除空行和注释后计数 | 总览请求或文件 mtime 变化 | `0` 并提示清单缺失 |
| TensorFlow API 数 | `data/tf_apis.txt` 去除空行和注释后计数 | 同上 | 同上 |
| API 总数 | 两个 API 清单实时计数求和 | 同上 | 不使用写死总数 |
| Prompt 就绪数 | `prompt_library_manifest.json` 与 `experiment/<lib>/<api>/prompts/structured_info.txt` | 总览请求或文件 mtime 变化 | 显示实际可检查数量 |
| 已确认 Bug 数与分布 | 已确认 Bug 索引及各目录 `meta.json` | 页面请求或目录 mtime 变化 | 无效条目不计数并返回警告 |
| Results 分类数 | 当前 Job 或顶层 `Results/<lib>/<category>/*.py` | 运行中 1 秒，静态页请求时 | 目录缺失显示 0 和未产生结果 |
| 阶段、模型和运行参数 | Job `status.json`、`summary.json` 和实际启动参数 | 运行中 1 秒 | 显示缺失字段，不回退到前端假定模型 |
| 实时生成指标 | Job `metrics.jsonl` | 运行中 1 秒增量读取 | 显示“尚无指标”，不生成示意曲线 |
| Python 与操作系统 | `sys.version_info`、`platform.system/release/machine` | 服务启动和手动刷新 | 显示可获取子集 |
| PyTorch/TensorFlow 安装版本 | Python package metadata；需要运行时信息则使用独立短命子进程 | 服务启动、手动刷新 | 显示未安装或检测失败 |
| CUDA 驱动、GPU 型号与总显存 | 带超时的 `nvidia-smi --query-gpu` 子进程 | 服务启动、手动刷新，缓存 30 秒 | GPU 不可用或 `nvidia-smi` 错误 |
| GPU 利用率与已用显存 | 运行中定时调用 `nvidia-smi` | 活跃 Job 期间 1 秒 | 断点显示为采集缺口，不补零 |
| 复现环境与实际设备 | Repro Job 启动时的环境快照与用例显式设备记录 | 每个 Repro Job 一次性快照 | 实际设备不能确定时记为 `unknown` |

### 5.3 环境接口与采集安全

新增 `GET /api/environment`，返回结构化数据：

```json
{
  "collected_at": "2026-06-20T14:32:00+08:00",
  "platform": {"system": "Linux", "release": "...", "machine": "x86_64"},
  "python": {"version": "..."},
  "frameworks": {
    "torch": {"installed": true, "version": "...", "cuda_runtime": "..."},
    "tensorflow": {"installed": true, "version": "..."}
  },
  "cuda": {"available": true, "driver_version": "..."},
  "gpus": [{"index": 0, "name": "...", "memory_total_mib": 81920}],
  "warnings": []
}
```

- Web 服务进程不直接长期 import PyTorch/TensorFlow 来查询 GPU，避免占用显存或污染后续子进程。
- 框架运行时检测与 `nvidia-smi` 都在带 3 秒超时的独立子进程中执行。
- 多卡服务器根据环境接口生成 GPU 选项，不在前端写死 `GPU 0` 或显卡名称。
- 环境采集失败不阻断 CPU 复现和静态证据浏览；仅禁用需要 GPU 的运行操作。
- 报告引用 Repro Job 创建时的环境快照，不在查看旧报告时改用当前环境。

### 5.4 前端数据检查

- API 总数必须等于两个 API 清单计数之和。
- Bug 索引条目只有在 `meta.json` 和复现源码存在时才进入已确认统计。
- 前端显示的模型名、运行模式和参数必须与 Job 实际命令一致。
- Results 计数必须可回溯到当前 Job 的具体文件，不与其他 API 或历史 Job 混合。
- 图表最后一个点必须与当前结果计数一致；不一致时显示数据检查警告。
- GPU 型号、驱动、总显存、利用率和已用显存不允许从前端常量或模拟数组读取。

### 5.5 当前实现审计

已经是真实数据的部分：

- `/api/overview` 通过 API 清单实时计算 PyTorch 1,568、TensorFlow 3,040 和总数 4,608。
- Prompt 就绪数通过 Manifest 和约束文件计算，当前为 4,608。
- Results 分类数量通过实际 `.py` 文件计数。
- 已确认 Bug 总数和框架分布从索引读取，当前为 14（PyTorch 5、TensorFlow 9）。

实现阶段必须替换的写死或缺失部分：

- `webapp/static/app.js` 仍使用 `facebook/incoder-1B` 作为阶段标题回退值。应改为读取 Job 实际 `mutation_model`；未启动 Job 时只显示“InCoder 变异”。
- `webapp/static/index.html` 仍将复现操作写为 `GPU0`。应根据 `/api/environment` 返回的 GPU 列表生成选项和型号。
- 当前没有 `/api/environment`，也没有 GPU 型号、驱动、显存、框架安装版本的统一结构化数据。
- 当前报告只记录 Python 和操作系统，未完整记录框架版本、CUDA、GPU 型号和实际执行设备。
- 当前没有 `metrics.jsonl` 和真实 GPU 时序采集，所有新图表在这两类数据完成前不得使用模拟数据。

## 6. 总览页

总览只展示静态、可验证的项目事实，不画没有数据基础的时间曲线。

### 6.1 首屏内容

- API 支持范围：从两个 API 清单实时求和（当前数据为 4,608）。
- PyTorch API：从 `data/torch_apis.txt` 实时计数（当前数据为 1,568）。
- TensorFlow API：从 `data/tf_apis.txt` 实时计数（当前数据为 3,040）。
- 已确认 Bug：从已确认索引实时统计。
- 两个主操作：运行单 API、Bug 复现。

### 6.2 静态图表

- API 框架分布条。
- 已确认缺陷现象分布：进程/内存崩溃、Fatal Check/Assert、CPU/GPU 后端差异等。
- 自动化流程带：API 约束→Qwen 种子→InCoder 变异→CPU/GPU Oracle→复现证据。

### 6.3 证据表

列为 `ID | API | 失效类型 | 当前环境复现 | 证据状态`。

不展示未经评分方法支持的 High/Medium 安全严重度。严重度只能在后续完成威胁建模、输入合法性和可利用性分析后添加。

## 7. 单 API 运行页

### 7.1 选择与运行信息

- API 必须从 `data/torch_apis.txt` 或 `data/tf_apis.txt` 搜索选择，不接受任意 API 文本。
- 运行信息拆分为静态配置与动态状态。
- 静态配置：框架、API、Qwen/InCoder 模型、GPU 编号、模式和关键预算。
- 动态状态：已运行时间、当前阶段、进度、结束原因和错误。

### 7.2 三阶段主分析区

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

### 7.3 图表设计

不将所有数据塞进一张图，也不为每个字段单独建图。每个阶段使用一个主视图和必要的辅助组件：

- Qwen：每轮生成数、验证通过数、修复成功数。
- InCoder：累计生成、去重、可执行数的实时折线；Results 类型使用堆叠条。
- Driver：已检查程序进度、CPU/GPU 一致数、差异 Catch 数和证据列表。以进度条和结果组成为主，不强行使用折线。

GPU 利用率、显存占用和峰值显存贯穿整个 Job 采集，放入默认折叠的“系统监控”区。

### 7.4 Results 语义

所有分类数量都显示，但不都宣称为 Bug：

- `seed`：初始可用种子。
- `valid`：正常执行的变异程序。
- `exception`：可捕获异常，默认不是 Bug。
- `crash`：清洁子进程中仍复现的崩溃，强候选。
- `hangs`：超时或疑似卡死。
- `flaky`：二次验证不稳定。
- `notarget`：变异后目标 API 丢失。

### 7.5 实时数据

新增每个 Job 的 `metrics.jsonl`。任务在轮次、分类数或阶段变化时追加结构化事件。前端轮询增量数据，不从终端文本猜数值。

最小事件字段包括：`timestamp, stage, round, generated, duplicated, valid, exception, crash, hangs, flaky, notarget, generation_seconds, validation_seconds`。GPU 采集记录 `utilization, memory_used, memory_total`。

## 8. 任务与 Results 存储

单 API 网页运行保持两层结果：

1. `demo_runs/api_jobs/<job_id>/Results/<lib>/`：运行中产物、实时图表、日志和完整历史。
2. `Results/<lib>/`：Job 成功后发布的每个 API 最新正式结果。

重跑同一 API 时，只替换顶层 Results 中该 API 的旧文件，不影响其他 API。运行中和失败 Job 不污染正式 Results。

作品赛演示不会频繁运行，因此保留全部 Job，不实现自动清理页或后台清理策略。

## 9. 候选问题审查

### 9.1 边界

网页不允许将一次异常直接标记为“已确认 Bug”，也不实现自动最小化。

主流程为：

`Results 原始结果→系统推荐候选→用户加入审查队列→独立复现与人工判断→仓库录入已确认 Bug`。

### 9.2 推荐规则

自动建议但不自动加入：

- 清洁进程仍复现的 crash。
- 稳定 hang。
- INTERNAL ASSERT 或 Fatal Check。
- CPU/GPU 输出或异常不一致。

普通 exception、notarget 和 flaky 默认不推荐，但允许用户手动选择具体程序。

### 9.3 候选索引

候选标记对象是具体 Job 中的具体 `.py` 文件，不是整个 API。候选索引保存：

- Candidate ID、Job ID、框架和 API。
- 原始分类和 Job Results 内不可覆盖的文件路径。
- 源码 SHA-256、初始错误类型、创建时间和审查状态。

为减少重复文件，候选阶段不复制源码，直接引用保留的 Job Results。相同源码哈希不重复创建。

状态为 `pending_review, reproduced, needs_review, rejected, promoted`。网页只允许排除/归档，不提供物理删除和直接确认 Bug。

## 10. Bug 复现页

### 10.1 页面结构

- 左侧为已确认 Bug/候选审查标签、搜索和筛选列表。
- 右侧首先显示当前环境复现结论。
- 结论下方显示“合理行为 vs 实际行为”，解释为什么值得视为框架缺陷证据。
- 最小复现代码和当前运行输出并排展示。
- 将信号、返回码、超时和子进程崩溃翻译为人可理解的证据。
- 已有报告时操作显示为“查看报告”。

### 10.2 实际设备判定

`CUDA_VISIBLE_DEVICES=0` 只代表 GPU 可见，不代表目标 API 在 GPU 执行。复现结论必须记录实际 Tensor/device 路径。无法确定时显示 `unknown`，不根据 GPU 可见性猜测。

## 11. 报告

### 11.1 生成与保留

- `report.md` 是唯一正式源文件，每个 Repro Job 只生成一次。
- 已存在时接口直接返回原报告，不覆盖。
- 网页渲染 Markdown，并支持浏览器打印/导出 PDF。
- 重新复现会创建新 Repro Job 和新报告，历史证据不覆盖。
- Job ID 只保存在内部状态和附件关联中，不出现在正文。

### 11.2 报告内容

1. 报告 ID、Bug/Candidate ID、API、类型和生成时间。
2. 当前环境复现结论和命中次数。
3. 合理行为与实际行为。
4. 每个执行配置的实际设备、返回码、信号、耗时和判定。
5. 最小复现源码与输出摘要。
6. Python、操作系统、框架、CUDA Runtime 和 GPU 环境。
7. 适用范围、未确定根因、未评估安全影响等限制。
8. 源码与日志 SHA-256、原始附件路径。

### 11.3 结论规则

大模型不参与证据结论。报告采用：

`结构化证据提取→确定性规则分类→模板表达→未知类型回退人工审核`。

自动类型包括正常退出、操作系统信号、allocator/memory corruption、Internal Assert/Fatal Check、CUDA device-side assert、CPU/GPU 输出或异常不一致、超时、OOM、普通异常和未知非零返回码。

模板只描述可观测现象，不推断源码根因、可利用性、修复方案或安全严重度。候选报告的结论必须说明“已复现异常，是否属于框架缺陷仍需人工审查”。

## 12. 错误处理

- 模型、Prompt、种子或 GPU 环境不可用时，当前阶段失败，后续阶段标记为 skipped。
- 图表缺少数据时显示具体空状态，不生成示意曲线。
- 日志无法解析时保留原文，结论进入 needs_review。
- 候选引用的 Job 文件不存在时显示证据缺失，不静默跳过。
- 报告已存在时只读返回，不重新计算或覆盖。

## 13. 可访问性与验证

- 状态不只依赖颜色，同时显示文字和图标。
- 所有标签、图例和返回码在 1280px 以上无截断。
- 支持键盘选择 API、切换阶段和浏览 Bug 列表。
- 实时图表尊重 `prefers-reduced-motion`。
- 使用浏览器完整验证总览、单 API 运行、阶段回看、候选加入、Bug 复现、报告幂等和 PDF 打印流程。

## 14. 明确不做

- 不允许网页用户直接将候选标记为已确认 Bug。
- 不实现自动最小化、自动源码根因定位或自动修复。
- 不使用大模型生成证据结论。
- 不输出无依据的 CVSS、High/Medium 安全严重度。
- 不实现多用户、角色权限、硬删除、自动磁盘清理和后台任务调度管理。
- 不在总览展示虚构趋势或将少量演示运行冒充为全量实验结果。

## 15. 验收标准

1. 评委在总览首屏可看到真实 API 支持范围、已确认 Bug 数和直接演示入口。
2. 单 API 任务启动后，三阶段状态、实时指标、GPU 监控和日志与实际进程一致。
3. 未运行阶段无法打开空图，已完成阶段可回看。
4. Results 七类数据语义清晰，不将异常数量直接表述为 Bug 数。
5. 具体生成程序可加入候选队列，重跑同一 API 不破坏旧候选引用。
6. Bug 复现页能解释返回码、信号、实际设备和判定原因。
7. 同一 Repro Job 的报告重复请求不覆盖原报告，新复现 Job 可生成新报告。
8. 未知异常被明确标记为需人工审核，系统不猜测根因或安全影响。
9. 在两台 GPU 型号或框架版本不同的环境中启动服务时，界面和 `/api/environment` 分别显示各自实际环境，无需改前端代码。
10. 关闭 `nvidia-smi` 或使 GPU 不可见时，界面显示真实的不可用状态，不显示上一次的 GPU 型号或模拟数据。
11. 总览指标、Job 配置、Results 计数和图表末点通过数据一致性检查；任一校验失败都在界面显示警告。
12. Repro 报告中的环境是该 Job 运行时快照，后续更换 GPU 或框架版本不会改写旧报告。
