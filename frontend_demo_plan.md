# TitanFuzz-main 前端展示方案

更新日期：2026-06-16

## 1. 方案审查结论

上一版“深度学习框架缺陷检测工作台”方向总体合理，但需要做三处收敛：

1. 不应把系统包装成“实时一键确认 bug”的产品。TitanFuzz-main 的真实能力是自动生成测试程序、筛选异常候选、辅助人工最小化和确认 bug。
2. 不应在现场演示时依赖 DeepSeek 在线调用。DeepSeek 的作用应定位为离线构建 prompt/constraint library，运行阶段只查询本地库。
3. 不应让评委等待全量 fuzzing。现场只跑单 API 小闭环，真正的 bug 成果通过证据库和最小复现展示。

修改后的展示定位：

```text
面向深度学习框架的 LLM 辅助模糊测试与缺陷审查工作台。
```

它展示的不是普通网页说明，而是一个能承载完整实验链路的工作台：

```text
本地 prompt 库
→ Qwen seed generation
→ seed 修复与验证
→ InCoder-6B 演化变异
→ CPU/GPU differential oracle
→ trace 审查
→ bug 证据库与报告导出
```

## 2. TitanFuzz-main 的真实流程

本方案严格按照当前 `TitanFuzz-main` 的实现逻辑设计。

### 2.1 离线阶段：构建 prompt/constraint library

DeepSeek 不参与每次运行。它的合理定位是离线文档蒸馏模块：

```text
官方 API 文档 / API 签名
→ DeepSeek 蒸馏
→ experiment/<lib>/<api>/prompts/structured_info.txt
→ experiment/<lib>/<api>/prompts/greedy_prompt.txt
```

运行时直接读取本地 prompt 库，例如：

```text
experiment/torch/torch.nn.functional.conv1d/prompts/structured_info.txt
experiment/torch/torch.nn.functional.conv1d/prompts/greedy_prompt.txt
```

前端可以展示这些约束，但不建议现场动态调用 DeepSeek。

### 2.2 在线阶段：单 API 检测流程

给定一个 API，例如：

```text
torch.nn.functional.conv1d
```

系统执行：

1. 检查本地 prompt 库是否存在。
2. 调用 `qwen_seed.py` 生成 raw seed。
3. 通过四层修复管线得到可执行 fix seed。
4. 调用 `ev_generation.py`，使用 `facebook/incoder-6B` 进行演化变异。
5. 调用 `driver.py` 做 CPU/GPU 差分检测。
6. 生成 `trace.txt` 和摘要报告。

这条流程可以封装成一条命令：

```bash
bash scripts/run_one_api_demo.sh \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --constraints_dir experiment/torch \
  --qwen_model ../Qwen2.5-Coder-7B-Instruct \
  --mut_model facebook/incoder-6B \
  --out demo_runs/conv1d_demo
```

## 3. 前端产品形态

前端建议命名为：

```text
TensorGuard Workbench
```

或中文：

```text
深度学习框架缺陷检测工作台
```

不要做成营销落地页。第一屏应该直接进入工作台。

## 4. 页面设计

### 4.1 Dashboard：实验总览

用途：让评委快速理解系统规模和成果。

展示指标：

```text
prompt 库覆盖 API 数
已生成 seed 数
valid seed 数
演化生成程序数
trace catch 数
人工确认候选数
已最小化复现数
```

展示图表：

```text
候选类型分布：
- Crash / Internal Assert
- CPU-GPU inconsistency
- Exception mismatch
- Timeout / Hang
- Rejected noise

流程产物分布：
- raw
- fix
- valid
- exception
- crash
- notarget
- hangs
- flaky
```

注意：这里展示的是已有实验数据，不声称实时扫完整框架。

### 4.2 Single API Demo：单 API 演示

用途：展示系统不是纯 PPT，而是能实际跑通一个 API。

输入项：

```text
Library: torch / tf
API: torch.nn.functional.conv1d
Seed model: Qwen2.5-Coder
Mutation model: facebook/incoder-6B
Mode: demo / normal
```

点击运行后展示流程状态：

```text
Prompt Library Hit
→ Qwen Seed Generation
→ Seed Repair & Validation
→ InCoder-6B Mutation
→ CPU/GPU Oracle
→ Trace Generated
```

每一步显示：

```text
状态：pending / running / success / failed
耗时
输出文件位置
生成数量
错误摘要
```

推荐演示参数：

```text
qwen n_samples: 5-10
qwen min_valid: 2-5
ev_generation max_valid: 5-20
incoder batch_size: 1-2
per_api_budget: 300-600 秒
```

现场演示目标是跑通流程，不保证现场发现新 bug。

### 4.3 Prompt Library：约束库查看

用途：解释 DeepSeek 的作用，也是你们相对原始 TitanFuzz 的创新点之一。

选择 API 后展示：

```text
greedy_prompt.txt
structured_info.txt
API signature
参数类型
shape 约束
跨参数约束
```

例如 `torch.nn.functional.conv1d` 可以展示：

```text
input: 3D tensor
weight: 3D tensor
padding: valid / same
constraint: input.shape[1] % groups == 0
constraint: padding != 'same' or stride == 1
```

这里要明确说明：

```text
DeepSeek 用于离线蒸馏 API 文档，生成本地约束库；
运行阶段直接查询本地库，不依赖在线 DeepSeek 调用。
```

### 4.4 Bug Candidate Repository：候选问题库

用途：替代“PPT 上贴几个日志”的薄弱展示方式。

表格字段：

```text
ID
Framework
API
Bug Type
Version
Severity
Status
Minimized
Reproducible
Last Reviewed
```

状态建议：

```text
Raw Catch
Triaged
Minimized
Strong Candidate
Rejected
Reported
Confirmed Upstream
```

注意不要把 raw catch 数量当 bug 数量。前端文案应使用：

```text
候选问题
已复核候选
强 bug 候选
```

避免使用：

```text
已确认发现 N 个官方 bug
```

除非有上游 issue/maintainer 确认。

### 4.5 Bug Detail：证据详情页

用途：这是最重要的评委说服页面。

每个候选展示：

```text
问题标题
目标 API
框架版本
CUDA / GPU / Python 环境
问题类型
原始 trace 片段
最小复现代码
CPU 输出
GPU 输出
对照实验
为什么不是误报
当前状态
报告导出按钮
```

例如 `fractional_max_pool3d` 应展示：

```text
C=65535: CPU 成功，CUDA 成功
C=65536: CPU 成功，CUDA invalid argument
```

并解释：

```text
该问题已经脱离 TitanFuzz 独立复现；
不是生成代码错误；
不是 TF32 数值误差；
不是 out alias 未定义行为；
更像 CUDA backend 边界条件问题。
```

### 4.6 Report Export：报告导出

用途：体现落地性。

导出格式：

```text
Markdown report
GitHub issue draft
复现脚本 zip
日志 zip
```

导出内容：

```text
Title
Environment
Minimal Reproduction
Expected Behavior
Actual Behavior
CPU/GPU Logs
Triage Notes
```

这比纯展示更像真实安全审计工具。

## 5. 现场演示路径

推荐现场按以下顺序演示：

1. 打开 Dashboard，展示已有实验规模。
2. 进入 Prompt Library，点开一个 API，说明 DeepSeek 离线构建约束库。
3. 进入 Single API Demo，选择 `torch.nn.functional.conv1d`，启动单 API 小流程。
4. 观察流程时间线：Qwen seed、repair、InCoder mutation、driver oracle。
5. 切到 Bug Candidate Repository。
6. 打开一个强候选，例如 `fractional_max_pool3d`。
7. 展示最小复现、CPU/GPU 差异、对照实验和日志。
8. 点击 Export，展示报告导出能力。

这条演示路径的核心是：

```text
现场跑流程，成果看证据库。
```

不要让评委等全量 fuzzing，也不要把单 API demo 绑定到“必须现场发现 bug”。

## 6. 技术实现建议

### 6.1 MVP 版本

MVP 不需要复杂任务调度系统。

推荐实现：

```text
前端：展示页面 + 调用单 API demo
后端：一个白名单 wrapper 脚本
数据：读取 demo_runs/、reports/、experiment/ 目录
```

最小后端能力：

```text
GET /api/dashboard
GET /api/prompt-library?lib=torch&api=...
POST /api/run-demo
GET /api/demo-status/:id
GET /api/bug-candidates
GET /api/bug-candidates/:id
GET /api/export/:id
```

### 6.2 安全边界

不要允许前端传任意 shell 命令。

后端只允许：

```text
固定脚本：scripts/run_one_api_demo.sh
固定参数集合：lib、api、out、mode
API 必须来自白名单或本地 prompt 库
输出目录必须在 demo_runs/ 下
```

原因：这个系统会执行模型生成的 Python 程序，本质上有代码执行风险。比赛演示可以控制输入范围。

### 6.3 Demo 失败处理

单 API demo 可能失败。前端必须正常展示失败原因，而不是页面卡死。

失败状态包括：

```text
prompt 库缺失
Qwen 模型未找到
Qwen 未生成 valid seed
InCoder-6B OOM
driver.py 运行失败
trace 编码异常
```

每种失败都应显示：

```text
失败阶段
错误摘要
日志路径
建议处理
```

## 7. 不建议做的功能

短期不建议做：

```text
1. 在线调用 DeepSeek 动态构建 prompt 库
2. 让用户上传任意 Python 文件并执行
3. 承诺一键确认官方 bug
4. 做复杂 3D 图谱或过度装饰的可视化
5. 现场跑全量 API
6. 把 raw catch 数量包装成 bug 数量
```

这些功能要么不稳定，要么容易被评委追问，要么和当前真实能力不匹配。

## 8. 和 C++ 底层 bug 检测类作品的对应关系

C++ 底层 bug 检测类作品通常展示：

```text
导入目标项目
启动扫描任务
展示漏洞列表
展示源码定位
展示调用链/数据流证据
展示 PoC 或复现日志
导出报告
```

本项目对应为：

```text
选择目标 DL API
启动单 API fuzzing
展示候选问题列表
展示 trace 定位
展示 CPU/GPU 差异证据
展示最小复现代码
导出报告 / GitHub issue 草稿
```

所以你们不是“视频检测类实时 AI 应用”，而是更接近：

```text
框架级缺陷审查与证据管理系统。
```

## 9. 最终建议

最终前端方案应采用：

```text
单 API 可运行演示 + 已审核候选 bug 证据库 + prompt 约束库可视化
```

这是最符合 TitanFuzz-main 真实能力的展示方式。

对外表述：

```text
系统支持对单个深度学习 API 发起端到端 fuzzing 任务：
先查询本地 DeepSeek 蒸馏得到的结构化约束库，
再由 Qwen 生成可执行 seed，
经四层修复验证后交给 InCoder-6B 进行演化变异，
最后通过 CPU/GPU differential oracle 发现候选异常。
对于历史实验发现的强候选，系统提供最小复现、日志、对照实验和报告导出能力。
```

这比纯 PPT 更像作品，也比伪实时扫描更真实可靠。
