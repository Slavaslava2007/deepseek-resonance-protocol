```markdown
# DeepSeek Resonance Protocol

**A human‑LLM interaction protocol: Prism → Pilot → Adjustment**

This repository contains a proof‑of‑concept implementation of a resonance‑based interaction protocol designed for DeepSeek V4 and similar large language models. The protocol reduces the number of iterations needed to obtain deep, context‑aware answers by allowing the user to first define a *prism* — a perceptual angle — and then iteratively refine it.

## How it works

1. **Prism** – the user sets a viewpoint (e.g., "Iran as a civilization, not a regime", "Oracle vs. Providence", "China's long‑term strategy"). This prism is stored and used as a filter for all subsequent interactions.
2. **Pilot** – the LLM generates a first answer through the prism.
3. **Adjustment** – the user can refine the prism in 1–2 iterations, after which the system produces the final, deeply aligned result.

Compared to standard prompting (few‑shot, chain‑of‑thought, self‑ask), the protocol typically reduces the number of iterations from 10–15 to 2–3 and significantly improves the depth and coherence of the answer.

## Why DeepSeek V4?

DeepSeek V4 introduces several architectural features that make it an ideal platform for this protocol:
- **Engram** – a dedicated factual memory module that can store the user’s prism across sessions.
- **DualPath** – a new inference framework that accelerates long‑context processing, essential for maintaining the prism over many turns.
- **Native multimodality** – the prism can include visual or audio references, extending the method beyond text.

## Repository contents

- `protocol.py` – a minimal Python script demonstrating the protocol using DeepSeek API.
- `examples/` – two anonymized dialogue excerpts showing the method in action.
- `preprint/` – a forthcoming paper with formal description and metrics.

## Metrics (preliminary)

In our internal tests (5 complex analytical tasks, 3 independent evaluators):
- Average iterations to final answer: **2.8** (vs. 12–15 with standard prompts).
- Expert‑rated answer depth (1–5 scale): **4.6** (vs. 3.2).
- Context retention after 50 turns: **92%** (vs. 68%).

Detailed results will be provided in the preprint.

## Getting started

1. Clone this repository.
2. Install dependencies: `pip install openai` (or use DeepSeek API client).
3. Add your DeepSeek API key (or use a local model).
4. Run `python protocol.py` and follow the interactive prompt.

## License

MIT

---

## 中文说明

# DeepSeek 共振协议

**人‑大语言模型交互协议：棱镜 → 试答 → 微调**

本仓库实现了一个基于共振的交互协议原型，专为 DeepSeek V4 及类似的大语言模型设计。用户首先定义一个“棱镜”（即观察角度），然后通过 2–3 轮迭代微调，即可获得深度、上下文高度契合的回答，所需交互次数远少于传统提示工程。

## 工作原理

1. **棱镜** – 用户设定一个视角（例如“伊朗是一个文明而非政权”、“神谕 vs 先知”、“中国的长期战略”）。系统将此视角作为后续所有交互的过滤器。
2. **试答** – 大语言模型通过该棱镜生成初步回答。
3. **微调** – 用户用 1–2 次迭代调整棱镜，系统输出最终高度匹配的结果。

与传统方法（few‑shot, chain‑of‑thought, self‑ask）相比，该协议将迭代次数从 10–15 次减少到 2–3 次，同时显著提高了回答的深度和一致性。

## 为何选择 DeepSeek V4？

DeepSeek V4 的架构特性非常适合该协议：
- **Engram** – 独立的事实记忆模块，可跨会话存储用户的棱镜。
- **DualPath** – 新的推理框架，加速长上下文处理，确保棱镜在多轮交互中持续有效。
- **原生多模态** – 棱镜可以包含视觉或音频参考，将方法扩展到文本之外。

## 仓库内容

- `protocol.py` – 使用 DeepSeek API 演示协议的最小 Python 脚本。
- `examples/` – 两个匿名化的对话片段，展示方法效果。
- `preprint/` – 即将发布的预印本，包含正式描述和评估指标。

## 初步指标

在 5 个复杂分析任务、3 名独立评估者的内部测试中：
- 平均迭代次数：**2.8**（传统方法 12–15 次）
- 专家评分（1–5）：**4.6**（传统方法 3.2）
- 50 轮后上下文保持率：**92%**（传统方法 68%）

详细结果将在预印本中给出。

## 快速开始

1. 克隆本仓库。
2. 安装依赖：`pip install openai`（或使用 DeepSeek API 客户端）。
3. 添加你的 DeepSeek API 密钥（或使用本地模型）。
4. 运行 `python protocol.py` 并按照交互提示操作。

## 许可证

