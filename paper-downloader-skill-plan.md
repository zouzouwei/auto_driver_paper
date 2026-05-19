# 论文下载器Skill设计Plan

## 1. Skill概述

**Skill名称**: `paper-downloader`

**核心功能**: 根据用户指定的研究方向、时间范围、关键词自动下载论文，创建对应文件夹结构，并组织存储。

**支持领域**:
- 自动驾驶（纯视觉3D检测、BEV感知、车道线检测等）
- 具身智能（机器人感知、抓取、导航等）
- 计算机视觉（目标检测、分割、跟踪等）
- 其他AI领域

---

## 2. 触发条件设计

### 2.1 主要触发场景

```
- 用户要求下载特定领域的论文
- 用户指定时间范围和关键词
- 用户要求批量下载论文
- 用户要求创建论文文件夹结构
```

### 2.2 关键词触发

```
中文: "下载论文"、"论文下载"、"批量下载"、"收集论文"
      "创建论文文件夹"、"论文整理"
英文: "download papers", "fetch papers", "collect papers"
```

### 2.3 使用示例

```
"帮我下载最近2022-2026年自动驾驶-纯视觉-3D目标检测相关的论文"
"下载2023-2025年BEV感知方向的论文"
"收集具身智能-机器人抓取相关的最新论文"
"下载CVPR 2024关于occupancy prediction的论文"
```

---

## 3. 核心工作流程设计

### Step 1: 解析用户需求

```
输入解析:
├── 研究方向: 自动驾驶-纯视觉-3D目标检测
├── 时间范围: 2022-2026
├── 关键词提取: 纯视觉, 3D检测, camera-only, monocular
└── 会议/期刊偏好: CVPR, ICCV, ECCV, NeurIPS等
```

### Step 2: 论文检索

```
检索来源:
├── arXiv (主要来源)
│   ├── cs.CV (计算机视觉)
│   ├── cs.RO (机器人)
│   └── cs.AI (人工智能)
├── Semantic Scholar API
├── Google Scholar (如可访问)
└── OpenReview (顶会论文)

检索策略:
├── 关键词组合搜索
├── 时间范围过滤
├── 引用数排序
└── 去重处理
```

### Step 3: 创建文件夹结构

```
文件夹命名规则:
paper_downloads/
└── {研究方向}_{时间范围}/
    ├── README.md              # 论文清单和摘要
    ├── papers/                # PDF文件
    │   ├── paper1_title.pdf
    │   ├── paper2_title.pdf
    │   └── ...
    └── metadata.json          # 论文元数据

示例:
paper_downloads/
└── autonomous_driving_camera_3d_detection_2022-2026/
    ├── README.md
    ├── papers/
    │   ├── BEVFormer_ECCV2022.pdf
    │   ├── BEVDepth_AAAI2023.pdf
    │   └── ...
    └── metadata.json
```

### Step 4: 下载论文

```
下载流程:
├── 从arXiv下载PDF
├── 验证PDF完整性
├── 命名规范化: {Title}_{Venue}_{Year}.pdf
├── 保存元数据信息
└── 生成README论文清单
```

### Step 5: 生成报告

```
输出内容:
├── 论文数量统计
├── 会议/年份分布
├── 下载成功/失败列表
└── README论文清单（含摘要）
```

---

## 4. 输出格式设计

### 4.1 README.md模板

```markdown
# {研究方向} 论文下载清单

## 下载信息
- **研究方向**：{方向描述}
- **时间范围**：{起始年份}-{结束年份}
- **下载时间**：{日期}
- **论文数量**：{N}篇

## 论文列表

### 2024年
| 序号 | 标题 | 会议 | 第一作者 | 关键词 | 文件名 |
|------|------|------|----------|--------|--------|
| 1 | {标题} | {会议} | {作者} | {关键词} | {文件名} |
| 2 | ... | ... | ... | ... | ... |

### 2023年
| 序号 | 标题 | 会议 | 第一作者 | 关键词 | 文件名 |
|------|------|------|----------|--------|--------|
| 1 | {标题} | {会议} | {作者} | {关键词} | {文件名} |

### 2022年
...

## 论文摘要

### Paper 1: {标题}
- **会议/年份**：{会议}/{年份}
- **作者**：{作者列表}
- **摘要**：{摘要内容}
- **核心贡献**：{贡献总结}
- **关键词**：{关键词列表}

### Paper 2: {标题}
...

## 下载统计
| 年份 | 论文数量 | 主要会议 |
|------|----------|----------|
| 2024 | {数量} | {会议列表} |
| 2023 | {数量} | {会议列表} |
| 2022 | {数量} | {会议列表} |
```

### 4.2 metadata.json格式

```json
{
  "query": {
    "direction": "autonomous_driving_camera_3d_detection",
    "time_range": "2022-2026",
    "keywords": ["camera-only", "3D detection", "monocular", "BEV"],
    "download_date": "2025-01-15"
  },
  "papers": [
    {
      "id": 1,
      "title": "BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers",
      "authors": ["Zhiqi Li", "Wenhai Wang", "Hongyang Li", "..."],
      "venue": "ECCV",
      "year": 2022,
      "arxiv_id": "2203.17270",
      "url": "https://arxiv.org/abs/2203.17270",
      "pdf_url": "https://arxiv.org/pdf/2203.17270",
      "abstract": "...",
      "keywords": ["BEV", "transformer", "multi-camera", "3D detection"],
      "file_name": "BEVFormer_ECCV2022.pdf",
      "download_status": "success"
    },
    ...
  ],
  "statistics": {
    "total_papers": 50,
    "download_success": 48,
    "download_failed": 2,
    "venue_distribution": {
      "CVPR": 15,
      "ICCV": 10,
      "ECCV": 8,
      "NeurIPS": 5,
      "arXiv": 10
    },
    "year_distribution": {
      "2024": 20,
      "2023": 18,
      "2022": 12
    }
  }
}
```

---

## 5. 支持的研究方向

### 5.1 自动驾驶

```
感知方向:
├── 纯视觉3D目标检测 (camera-only 3D detection)
├── BEV感知 (BEV perception)
├── 多模态融合 (multi-modal fusion)
├── 车道线检测 (lane detection)
├── 地图构建 (HD map construction)
├── 占用预测 (occupancy prediction)
├── 3D语义分割 (3D semantic segmentation)
└── 多目标跟踪 (multi-object tracking)

预测方向:
├── 运动预测 (motion prediction)
├── 轨迹预测 (trajectory prediction)
└── 行为预测 (behavior prediction)

规划控制:
├── 路径规划 (path planning)
├── 运动规划 (motion planning)
└── 决策制定 (decision making)
```

### 5.2 具身智能

```
感知方向:
├── 机器人视觉 (robot vision)
├── 3D场景理解 (3D scene understanding)
├── 物体识别 (object recognition)
└── 场景重建 (scene reconstruction)

操作方向:
├── 抓取规划 (grasp planning)
├── 操作策略 (manipulation policy)
└── 工具使用 (tool use)

导航方向:
├── 视觉导航 (visual navigation)
├── 自主探索 (autonomous exploration)
└── 避障 (obstacle avoidance)

学习方向:
├── 模仿学习 (imitation learning)
├── 强化学习 (reinforcement learning)
└── sim-to-real (simulation to real)
```

### 5.3 计算机视觉

```
检测方向:
├── 2D目标检测 (2D object detection)
├── 3D目标检测 (3D object detection)
├── 实例分割 (instance segmentation)
└── 关键点检测 (keypoint detection)

分割方向:
├── 语义分割 (semantic segmentation)
├── 全景分割 (panoptic segmentation)
└── 视频分割 (video segmentation)

生成方向:
├── 图像生成 (image generation)
├── 视频生成 (video generation)
└── 3D生成 (3D generation)
```

---

## 6. 技术实现细节

### 6.1 论文检索API

```
主要数据源:
├── arXiv API
│   ├── 优点: 免费、稳定、覆盖面广
│   ├── 限制: 无引用数、无会议信息
│   └── 使用: 搜索和下载PDF
│
├── Semantic Scholar API
│   ├── 优点: 有引用数、有会议信息
│   ├── 限制: 有请求频率限制
│   └── 使用: 获取元数据和引用信息
│
└── OpenReview API
    ├── 优点: 有顶会论文、有评审信息
    ├── 限制: 仅限部分会议
    └── 使用: 获取顶会论文
```

### 6.2 搜索策略

```
关键词组合:
├── 基础关键词: "3D object detection", "autonomous driving"
├── 限定关键词: "camera-only", "monocular", "multi-view"
├── 技术关键词: "BEV", "transformer", "attention"
└── 排除关键词: "LiDAR", "point cloud" (如需纯视觉)

搜索语法示例:
arXiv: all:"3D detection" AND all:"autonomous driving" AND all:"camera"
Semantic Scholar: 3D object detection autonomous driving camera-only
```

### 6.3 下载策略

```
下载流程:
├── 1. 获取论文列表
├── 2. 过滤时间范围
├── 3. 去重处理
├── 4. 按引用数排序
├── 5. 下载PDF文件
├── 6. 验证PDF完整性
├── 7. 命名规范化
└── 8. 保存元数据

错误处理:
├── 网络超时: 重试3次
├── PDF损坏: 重新下载
├── 访问限制: 记录失败，继续下载其他
└── 存储空间: 检查可用空间
```

---

## 7. 质量检查清单

### 7.1 检索质量

```
□ 关键词覆盖全面
□ 时间范围准确
□ 无遗漏重要论文
□ 无重复论文
□ 排序合理（按引用数/时间）
```

### 7.2 下载质量

```
□ PDF文件完整可读
□ 文件命名规范
□ 文件夹结构清晰
□ 元数据准确
□ README信息完整
```

### 7.3 用户体验

```
□ 下载进度显示
□ 错误信息清晰
□ 支持断点续传
□ 支持增量更新
□ 输出报告详细
```

---

## 8. 使用示例

### 示例1: 自动驾驶论文下载

```
用户: "帮我下载最近2022-2026年自动驾驶-纯视觉-3D目标检测相关的论文"

Skill执行:
1. 解析需求: 方向=自动驾驶-纯视觉-3D检测, 时间=2022-2026
2. 生成关键词: "3D object detection", "autonomous driving", "camera-only", "monocular"
3. 创建文件夹: paper_downloads/autonomous_driving_camera_3d_detection_2022-2026/
4. 检索论文: arXiv + Semantic Scholar
5. 下载PDF: 按年份和会议组织
6. 生成报告: README.md + metadata.json

输出:
paper_downloads/
└── autonomous_driving_camera_3d_detection_2022-2026/
    ├── README.md
    ├── papers/
    │   ├── BEVFormer_ECCV2022.pdf
    │   ├── BEVDepth_AAAI2023.pdf
    │   ├── PETR_ECCV2022.pdf
    │   └── ...
    └── metadata.json
```

### 示例2: 具身智能论文下载

```
用户: "下载2023-2025年具身智能-机器人抓取相关的最新论文"

Skill执行:
1. 解析需求: 方向=具身智能-机器人抓取, 时间=2023-2025
2. 生成关键词: "grasp planning", "robot manipulation", "embodied AI"
3. 创建文件夹: paper_downloads/embodied_ai_grasp_2023-2025/
4. 检索和下载
5. 生成报告
```

### 示例3: 指定会议下载

```
用户: "下载CVPR 2024关于occupancy prediction的论文"

Skill执行:
1. 解析需求: 会议=CVPR, 年份=2024, 方向=occupancy prediction
2. 生成关键词: "occupancy prediction", "3D occupancy"
3. 创建文件夹: paper_downloads/CVPR2024_occupancy_prediction/
4. 从OpenReview检索CVPR 2024论文
5. 过滤occupancy相关论文
6. 下载并组织
```

---

## 9. 实施步骤

### Step 1: 创建skill目录结构

```
/home/hy/.claude/skills/paper-downloader/
├── SKILL.md                    # 主要skill定义
├── evals/                      # 测试用例
│   └── evals.json
└── references/                 # 参考资料
    ├── search-strategies.md    # 搜索策略
    └── direction-keywords.md   # 各方向关键词库
```

### Step 2: 编写SKILL.md

- 触发条件
- 工作流程
- 输出格式
- 领域知识

### Step 3: 创建关键词库

- 自动驾驶关键词
- 具身智能关键词
- 计算机视觉关键词
- 会议/期刊列表

### Step 4: 测试验证

- 测试论文检索
- 测试下载功能
- 测试文件组织

---

## 已确认需求

✅ **下载来源**：主要从arXiv下载

✅ **论文数量限制**：每个方向最多50篇

✅ **排序方式**：按引用量、是否有开源代码排序

✅ **命名规范**：中文命名（文件夹和PDF文件）

✅ **增量更新**：支持，通过metadata.json记录已下载论文

✅ **下载并发**：限制并发数为5

✅ **摘要表格**：需要，子文件夹包含README.md，表格形式，每个论文有中文摘要

✅ **更新机制**：更新论文时，README.md表格也要同步更新

---

## 实施完成状态

### ✅ 已完成的工作

1. **创建skill目录结构**
   ```
   /home/hy/.claude/skills/paper-downloader/
   ├── SKILL.md                    # 主要skill定义
   ├── evals/                      # 测试用例
   │   └── evals.json
   └── references/                 # 参考资料
       └── direction-keywords.md   # 各方向关键词库
   ```

2. **编写SKILL.md核心内容**
   - 触发条件：支持"下载论文"、"收集论文"等场景
   - 工作流程：解析需求 → 检索arXiv → 创建文件夹 → 下载PDF → 生成报告
   - 输出格式：中文命名、README表格、metadata.json
   - 增量更新：通过metadata.json检测已下载论文

3. **创建关键词库**
   - 自动驾驶：10个子方向（纯视觉3D检测、BEV感知、车道线等）
   - 具身智能：5个子方向（机器人抓取、视觉导航、模仿学习等）
   - 计算机视觉：4个子方向（2D检测、语义分割、图像生成等）
   - 每个方向包含：主要关键词、次要关键词、排除关键词、相关方法

4. **配置测试用例**
   - 6个典型使用场景的测试用例
   - 覆盖单方向下载、多方向对比、增量更新等场景

### Skill核心特点

✅ **arXiv为主**：主要从arXiv下载，稳定可靠

✅ **50篇限制**：每个方向最多下载50篇精选论文

✅ **智能排序**：按引用量和是否有开源代码排序

✅ **中文命名**：文件夹和PDF都使用中文命名，方便查看

✅ **增量更新**：支持只下载新论文，自动更新README表格

✅ **并发控制**：限制并发下载数为5，避免触发限制

✅ **摘要表格**：README.md包含完整论文表格和中文摘要

### 使用方式

skill已创建完成并自动注册，可以通过以下方式使用：

1. **下载自动驾驶论文**：
   ```
   "帮我下载最近2022-2026年自动驾驶-纯视觉-3D目标检测相关的论文"
   ```

2. **下载具身智能论文**：
   ```
   "下载2023-2025年具身智能-机器人抓取相关的最新论文"
   ```

3. **按会议下载**：
   ```
   "下载CVPR 2024关于occupancy prediction的论文"
   ```

4. **更新已有论文集**：
   ```
   "帮我更新一下自动驾驶3D检测的论文"
   ```

### 输出结构示例

```
论文下载/
└── 自动驾驶_纯视觉3D目标检测_2022-2026/
    ├── README.md                              # 论文清单表格（含中文摘要）
    ├── papers/                                # PDF文件夹
    │   ├── BEVFormer_通过时空Transformer学习鸟瞰图表示_ECCV_2022.pdf
    │   ├── BEVDepth_多视角3D目标检测的可靠深度获取_AAAI_2023.pdf
    │   └── ...
    └── metadata.json                          # 元数据（用于增量更新）
```

**Paper Downloader Skill已准备就绪，可以开始使用！**
