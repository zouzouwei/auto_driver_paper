# Auto Driver Paper - 自动驾驶论文下载与分析工具

一个用于自动下载、整理和分析自动驾驶领域学术论文的Python工具集。

## 功能特性

### 1. 智能论文搜索与下载
- 基于arXiv API的智能论文搜索
- 自动下载PDF文件（并发控制，最多5个）
- 中文命名，便于识别
- 按引用量和开源代码排序
- 支持增量更新

### 2. 多传感器融合论文库
- Camera-LiDAR融合3D目标检测
- 包含TransFusion、BEVFusion等经典方法
- 20篇核心论文，涵盖2019-2024年

### 3. 纯视觉3D目标检测论文库
- 基于Camera的3D目标检测方法
- 包含BEVFormer、PETR等BEV感知方法
- 20篇核心论文，涵盖2021-2024年

### 4. 论文对比分析
- 自动驾驶感知技术深度分析
- 纯视觉vs多传感器融合对比
- 技术发展趋势分析

## 项目结构

```
paper/
├── README.md                           # 项目说明
├── 论文下载/                            # 论文下载目录
│   ├── download_camera_lidar_fusion.py # Camera-LiDAR融合论文下载脚本
│   ├── download_papers.py              # 纯视觉3D检测论文下载脚本
│   ├── search_arxiv.py                 # arXiv搜索脚本
│   ├── 自动驾驶_多传感器融合Camera-LiDAR_2021-2026/
│   │   ├── README.md                   # 论文清单（含中文摘要）
│   │   ├── papers/                     # PDF文件夹
│   │   └── metadata.json               # 论文元数据
│   └── 自动驾驶_纯视觉3D目标检测_2021-2024/
│       ├── README.md                   # 论文清单（含中文摘要）
│       ├── papers/                     # PDF文件夹
│       └── metadata.json               # 论文元数据
├── autonomous-driving-paper-skill-plan.md  # 论文下载技能设计文档
├── paper-downloader-skill-plan.md          # 论文下载器技能计划
└── 自动驾驶_纯视觉3D目标检测_对比分析.md    # 技术对比分析报告
```

## 使用方法

### 下载Camera-LiDAR融合论文

```bash
cd 论文下载
python3 download_camera_lidar_fusion.py
```

### 下载纯视觉3D检测论文

```bash
cd 论文下载
python3 download_papers.py
```

### 自定义论文搜索

```python
from search_arxiv import search_arxiv

# 搜索自动驾驶相关论文
papers = search_arxiv("autonomous driving 3D object detection", max_results=50)
```

## 论文库统计

### Camera-LiDAR融合论文库（20篇）
| 类别 | 数量 | 代表方法 |
|------|------|----------|
| 早期融合 | 3 | PointPainting, MVP, EPNet |
| 中期融合 | 5 | TransFusion, BEVFusion, DeepFusion |
| 后期融合 | 2 | CLOCs, CenterFusion |
| 统一框架 | 4 | FUTR3D, UniTR, FFNet |
| Radar融合 | 4 | CenterFusion, RadarNet, Bi-LRFusion |

### 纯视觉3D检测论文库（20篇）
| 类别 | 数量 | 代表方法 |
|------|------|----------|
| BEV方法 | 8 | BEVFormer, BEVDet, BEVDepth |
| Query-based | 5 | DETR3D, PETR, StreamPETR |
| 单目检测 | 4 | FCOS3D, MonoDETR, DD3D |
| 占用预测 | 3 | SurroundOcc, Occ3D, PanoOcc |

## 技术对比分析

### 纯视觉方案
**优势**：
- 成本低（无需LiDAR）
- 信息丰富（颜色、纹理）
- 量产友好

**劣势**：
- 深度估计不准确
- 受光照天气影响大
- 长距离检测困难

### 多传感器融合方案
**优势**：
- 检测精度高
- 鲁棒性强
- 适用场景广

**劣势**：
- 成本高
- 系统复杂
- 标定困难

## 发展趋势

1. **端到端学习**：从模块化到端到端
2. **多任务学习**：检测、分割、预测统一
3. **时序融合**：利用历史信息提升性能
4. **轻量化部署**：模型压缩和加速
5. **数据驱动**：大规模数据集和预训练

## 依赖环境

- Python 3.7+
- 标准库：urllib, xml, json, os, time, datetime
- 无需额外依赖

## 注意事项

1. 下载的论文仅用于学术研究，请遵守版权规定
2. 部分论文可能因网络原因下载失败，请重试
3. 论文元数据中的引用量为近似值，仅供参考
4. 建议在下载前检查磁盘空间（每个方向约100-200MB）

## 更新日志

### 2026-05-19
- 完成Camera-LiDAR融合论文库（20篇）
- 完成纯视觉3D检测论文库（20篇）
- 添加技术对比分析报告
- 支持增量更新功能

## 许可证

本项目仅供学术研究使用。论文版权归原作者所有。

## 联系方式

如有问题或建议，请提交Issue或Pull Request。
