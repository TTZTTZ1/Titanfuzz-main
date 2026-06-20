# TensorGuard 作品赛演示脚本

## 作品定位

TensorGuard 是面向深度学习框架的 LLM 辅助模糊测试与缺陷证据管理工作台。它不承诺实时扫描整个框架；现场演示聚焦一个 API 的完整自动化链路，以及已确认问题在当前环境中的可复现证据。

## 演示前检查

1. 在比赛服务器启动网页：

```bash
python3 webapp/server.py --host 0.0.0.0 --port <Cloud Studio 开放端口>
```

2. 打开“运行环境”，确认页面显示的是当前 Python、PyTorch/TensorFlow、GPU 型号、驱动和显存。出现采集警告时先处理，不使用口头补充的示例配置代替真实数据。
3. 预先确认 Qwen 与 InCoder 权重可用，并选择一个已验证能在演示时间内完成的 API。
4. 已确认 Bug 的复现报告只生成一次；需要重新采集时创建新的复现记录。

## 现场流程

### 1. 系统总览

- 展示 API 总覆盖：`data/torch_apis.txt` 与 `data/tf_apis.txt` 的实际行数。
- 展示 PyTorch、TensorFlow 分布和已确认 Bug 数量。
- 用检测链路解释过程：约束加载 → 种子生成 → 变异测试 → 差异检测 → 复现归档。
- 强调已确认表只包含结构化归档的证据，不把所有异常或 trace catch 当成 Bug。

### 2. 单 API 运行

1. 从 API 清单选择框架与 API，不手工输入一个清单外目标。
2. 选择运行模式和当前环境实际存在的 GPU。
3. 启动后依次展示：
   - Qwen：候选种子与有效种子变化；
   - InCoder：valid、exception、crash、hangs 等 Results 数量变化；
   - Driver：CPU/加速器差异检测阶段与 trace 输出。
4. 展开 GPU 监控，说明曲线来自任务运行时 `nvidia-smi` 采样；无采样时页面不会补零。
5. 在 Results 审查区打开具体 `.py` 文件。系统建议仅代表命中高信号规则，点击“加入候选”后仍需人工最小化和复现。

页面显示的模型名称来自当前 Job 的实际参数；不要把 1B、6B 或任何 GPU 型号写进固定讲稿。

### 3. Bug 复现

1. 在“已确认”列表选择一个问题。
2. 对照“预期行为”和“已知观测”解释为什么它被收录。
3. 查看最小复现代码，选择隐藏 CUDA 或指定 GPU 可见的执行配置。
4. 运行后查看返回码、POSIX 信号、观测类型和实际设备字段。
5. 生成证据报告，展示环境快照、代码、输出摘录与附件 SHA-256；需要 PDF 时使用“打印 / PDF”。

“候选”页只用于审查单 API 运行产生的精确文件。网页不会把候选直接提升为已确认 Bug。

## 建议表述

可以说：

- “这是当前环境下可重复获得的进程级证据。”
- “系统使用 CPU/加速器差异和崩溃信号定位高价值候选。”
- “约束库离线准备，现场链路从约束加载开始自动执行。”
- “自动规则描述观测，不替代框架维护者的根因确认。”

不要说：

- “每个异常都是框架 Bug。”
- “网页一键确认了漏洞或安全等级。”
- “只要 GPU 可见，程序就一定在 GPU 上执行。”
- “系统能实时完成全部 4608 个 API。”

## CLI 备用流程

网页无法访问时，可执行同一单 API 编排脚本：

```bash
bash scripts/run_one_api_demo.sh \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --out demo_runs/conv1d_demo \
  --mode demo
```

CLI 与网页共用 `scripts/run_one_api_demo.py`，输出仍保存在对应 Job 目录，并在成功后发布该 API 的最新结果到 `Results/<lib>`。
