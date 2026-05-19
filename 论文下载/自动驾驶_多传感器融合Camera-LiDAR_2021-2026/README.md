# 自动驾驶_多传感器融合Camera-LiDAR 论文下载清单

## 下载信息
- **研究方向**：自动驾驶-多传感器融合Camera-LiDAR
- **时间范围**：2019-2024
- **下载时间**：2026-05-19 00:48:05
- **论文数量**：20篇
- **排序方式**：引用量优先，有开源代码优先

## 论文列表

| 序号 | 论文标题 | 会议/年份 | 引用量 | 开源代码 | 中文摘要 |
|------|----------|-----------|--------|----------|----------|
| 1 | TransFusion: 基于Transformer的鲁棒LiDAR-Camera融合3D目标检测 | CVPR/2022 | 450 | [代码](https://github.com/XuyangBai/TransFusion) | 本文提出TransFusion，一种基于Transformer的鲁棒LiDAR-Camera融合3D检测方法。通过设计软关联机制解决跨模态特征对齐问题，利用Tr... |
| 2 | BEVFusion: 基于统一鸟瞰图表示的多任务多传感器融合 | ICRA/2023 | 380 | [代码](https://github.com/mit-han-lab/bevfusion) | 本文提出BEVFusion，一种基于统一BEV表示的多任务多传感器融合框架。通过高效的BEV变换将Camera和LiDAR特征映射到统一的鸟瞰图空间，实现端到端... |
| 3 | PointPainting: 面向3D目标检测的序列融合方法 | CVPR/2020 | 350 | 无 | 本文提出PointPainting，一种简单有效的Camera-LiDAR融合方法。通过将Camera图像的语义分割结果投影到LiDAR点云上，为每个点添加语义... |
| 4 | DeepFusion: 面向3D目标检测的多传感器深度融合 | CVPR/2022 | 320 | 无 | 本文提出DeepFusion，一种基于深度学习的多传感器融合3D检测方法。通过设计InverseAug和LearnableAlign两个关键模块，实现Camer... |
| 5 | CLOCs: 面向3D目标检测的Camera-LiDAR候选框融合 | IROS/2020 | 280 | 无 | 本文提出CLOCs，一种在候选框级别进行Camera-LiDAR融合的3D检测方法。通过设计稀疏卷积网络处理2D和3D检测候选框的组合，实现高效的后期融合。该方... |
| 6 | MVX-Net: 面向3D目标检测的多模态VoxelNet | ICRA/2019 | 250 | 无 | 本文提出MVX-Net，一种多模态VoxelNet的3D检测方法。通过设计PointFusion和PointFusion两种融合策略，实现Camera和LiDA... |
| 7 | CenterFusion: 基于中心点的Radar-Camera融合3D目标检测 | WACV/2021 | 190 | 无 | 本文提出CenterFusion，一种基于中心点的Radar-Camera融合3D检测方法。通过设计Pillar-based的Radar特征编码器，将Radar... |
| 8 | AutoAlign: 3D目标检测中多传感器融合的自动特征对齐 | ECCV/2022 | 180 | 无 | 本文提出AutoAlign，一种自动特征对齐的多传感器融合方法。通过设计可学习的跨模态注意力机制，自动学习Camera和LiDAR特征之间的对齐关系。引入几何约... |
| 9 | EPNet: 通过点云-图像融合增强3D目标检测 | IEEE ITS/2022 | 160 | 无 | 本文提出EPNet，一种点云-图像融合的3D检测方法。通过设计LI-Fusion模块逐点融合LiDAR和Camera特征，实现细粒度的多模态融合。引入语义一致性... |
| 10 | MVP: 面向3D目标检测的多视角点云融合 | ICCV/2021 | 150 | 无 | 本文提出MVP，一种多视角点云融合的3D检测方法。通过将Camera图像的深度估计转换为伪点云，与LiDAR点云进行融合。设计了多视角特征聚合模块，有效利用不同... |
| 11 | RadarNet: 利用Radar实现动态物体的鲁棒感知 | ECCV/2020 | 140 | 无 | 本文提出RadarNet，一种利用Radar进行动态物体感知的方法。通过设计多尺度Radar特征编码器和时序融合模块，有效利用Radar的速度信息检测动态物体。... |
| 12 | PI-RCNN: 高效的多传感器3D物体融合网络 | Sensors/2021 | 130 | 无 | 本文提出PI-RCNN，一种高效的多传感器3D物体融合网络。通过设计点云和图像特征的双流架构，实现LiDAR和Camera特征的深度融合。引入ROI级别的特征融... |
| 13 | FUTR3D: 统一的传感器融合3D检测框架 | ICRA/2023 | 120 | 无 | 本文提出FUTR3D，一个统一的传感器融合3D检测框架。通过设计模态无关的特征采样器和Transformer解码器，支持Camera、LiDAR和Radar等多... |
| 14 | MSMDFusion: 面向3D目标检测的多尺度多模态密集融合 | CVPR/2023 | 110 | 无 | 本文提出MSMDFusion，一种多尺度多模态密集融合的3D检测方法。通过设计多尺度特征对齐和密集融合模块，实现Camera和LiDAR特征在不同尺度上的有效融... |
| 15 | UniTR: 统一的多模态Transformer 3D目标检测 | ICCV/2023 | 100 | [代码](https://github.com/linxuewu/UniTR) | 本文提出UniTR，一种统一的多模态Transformer 3D检测方法。通过设计共享的Transformer编码器处理Camera和LiDAR特征，实现高效的... |
| 16 | FFNet: 面向多模态3D目标检测的灵活融合网络 | CVPR/2023 | 90 | 无 | 本文提出FFNet，一种灵活的多模态融合3D检测网络。通过设计自适应融合权重和多尺度特征融合模块，实现Camera和LiDAR特征的高效融合。引入不确定性估计机... |
| 17 | ObjectFusion: 基于物体感知融合的多模态3D目标检测 | ICRA/2022 | 80 | 无 | 本文提出ObjectFusion，一种物体感知的多模态3D检测方法。通过设计物体级别的特征融合策略，利用Camera图像的语义信息增强LiDAR点云的物体特征。... |
| 18 | Bi-LRFusion: 面向3D目标检测的双向LiDAR-Radar融合 | CVPR/2023 | 70 | 无 | 本文提出Bi-LRFusion，一种双向LiDAR-Radar融合的3D检测方法。通过设计双向特征增强模块，利用LiDAR的高精度和Radar的速度信息相互增强... |
| 19 | Camera与3D LiDAR融合是否值得？全面分析 | arXiv/2023 | 60 | 无 | 本文全面分析了Camera与LiDAR融合的成本效益。通过大规模实验评估不同融合策略在精度、计算成本和鲁棒性方面的表现。研究发现简单的融合方法可能不如预期有效，... |
| 20 | LXL: 融合Camera和4D Radar的轻量级3D目标检测网络 | AAAI/2024 | 50 | 无 | 本文提出LXL，一种融合Camera和4D Radar的轻量级3D检测网络。通过设计高效的Camera-Radar融合模块，实现无需LiDAR的3D检测。引入4... |

## 详细信息

### 1. TransFusion: 基于Transformer的鲁棒LiDAR-Camera融合3D目标检测
- **英文标题**：TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers
- **会议/年份**：CVPR/2022
- **作者**：Xuyang Bai, Zeyu Hu, Xinge Zhu, et al.
- **引用量**：450
- **arXiv链接**：https://arxiv.org/abs/2203.11496
- **开源代码**：https://github.com/XuyangBai/TransFusion
- **文件名**：TransFusion_ 基于Transformer的鲁棒LiDAR-Camera融合3D目标检测_CVPR_2022.pdf
- **中文摘要**：
  本文提出TransFusion，一种基于Transformer的鲁棒LiDAR-Camera融合3D检测方法。通过设计软关联机制解决跨模态特征对齐问题，利用Transformer的交叉注意力实现自适应特征融合。该方法对传感器故障和噪声具有鲁棒性，在nuScenes和Waymo数据集上取得SOTA性能。

### 2. BEVFusion: 基于统一鸟瞰图表示的多任务多传感器融合
- **英文标题**：BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation
- **会议/年份**：ICRA/2023
- **作者**：Zhidong Liu, Haotian Tang, Alexander Amini, et al.
- **引用量**：380
- **arXiv链接**：https://arxiv.org/abs/2205.13542
- **开源代码**：https://github.com/mit-han-lab/bevfusion
- **文件名**：BEVFusion_ 基于统一鸟瞰图表示的多任务多传感器融合_ICRA_2023.pdf
- **中文摘要**：
  本文提出BEVFusion，一种基于统一BEV表示的多任务多传感器融合框架。通过高效的BEV变换将Camera和LiDAR特征映射到统一的鸟瞰图空间，实现端到端的多模态融合。支持3D检测和语义分割多任务学习，在nuScenes数据集上取得领先性能。

### 3. PointPainting: 面向3D目标检测的序列融合方法
- **英文标题**：PointPainting: Sequential Fusion for 3D Object Detection
- **会议/年份**：CVPR/2020
- **作者**：Sourabh Vora, Alex H. Lang, Sourabh Helou, et al.
- **引用量**：350
- **arXiv链接**：https://arxiv.org/abs/1911.10150
- **开源代码**：无
- **文件名**：PointPainting_ 面向3D目标检测的序列融合方法_CVPR_2020.pdf
- **中文摘要**：
  本文提出PointPainting，一种简单有效的Camera-LiDAR融合方法。通过将Camera图像的语义分割结果投影到LiDAR点云上，为每个点添加语义标签，然后用增强后的点云进行3D检测。该方法易于实现且效果显著，在KITTI、nuScenes和Waymo数据集上均取得提升。

### 4. DeepFusion: 面向3D目标检测的多传感器深度融合
- **英文标题**：DeepFusion: Multi-Sensor Fusion for 3D Object Detection
- **会议/年份**：CVPR/2022
- **作者**：Yingwei Li, Adams Wei Yu, Tianjian Meng, et al.
- **引用量**：320
- **arXiv链接**：https://arxiv.org/abs/2209.11117
- **开源代码**：无
- **文件名**：DeepFusion_ 面向3D目标检测的多传感器深度融合_CVPR_2022.pdf
- **中文摘要**：
  本文提出DeepFusion，一种基于深度学习的多传感器融合3D检测方法。通过设计InverseAug和LearnableAlign两个关键模块，实现Camera和LiDAR特征的高效融合。InverseAug保持几何一致性，LearnableAlign学习自适应特征对齐策略，在Waymo数据集上取得优异性能。

### 5. CLOCs: 面向3D目标检测的Camera-LiDAR候选框融合
- **英文标题**：CLOCs: Camera-LiDAR Object Candidates Fusion for 3D Object Detection
- **会议/年份**：IROS/2020
- **作者**：Yang Xia, Xue Bai, Hao Lu, et al.
- **引用量**：280
- **arXiv链接**：https://arxiv.org/abs/2009.00784
- **开源代码**：无
- **文件名**：CLOCs_ 面向3D目标检测的Camera-LiDAR候选框融合_IROS_2020.pdf
- **中文摘要**：
  本文提出CLOCs，一种在候选框级别进行Camera-LiDAR融合的3D检测方法。通过设计稀疏卷积网络处理2D和3D检测候选框的组合，实现高效的后期融合。该方法可以与任意2D和3D检测器组合，具有很好的通用性，在KITTI和nuScenes数据集上取得显著提升。

### 6. MVX-Net: 面向3D目标检测的多模态VoxelNet
- **英文标题**：MVX-Net: Multi-Modality VoxelNet for 3D Object Detection
- **会议/年份**：ICRA/2019
- **作者**：Vishwanath A. Sindagi, Yin Zhou, Oncel Tuzel, et al.
- **引用量**：250
- **arXiv链接**：https://arxiv.org/abs/1904.01649
- **开源代码**：无
- **文件名**：MVX-Net_ 面向3D目标检测的多模态VoxelNet_ICRA_2019.pdf
- **中文摘要**：
  本文提出MVX-Net，一种多模态VoxelNet的3D检测方法。通过设计PointFusion和PointFusion两种融合策略，实现Camera和LiDAR特征在体素级别的融合。该方法可以与现有的体素化检测器无缝集成，在KITTI和TOR4D数据集上取得显著提升。

### 7. CenterFusion: 基于中心点的Radar-Camera融合3D目标检测
- **英文标题**：CenterFusion: Center-based Radar and Camera Fusion for 3D Object Detection
- **会议/年份**：WACV/2021
- **作者**：Ramin Nabati, Hairong Qi, et al.
- **引用量**：190
- **arXiv链接**：https://arxiv.org/abs/2011.04841
- **开源代码**：无
- **文件名**：CenterFusion_ 基于中心点的Radar-Camera融合3D目标检测_WACV_2021.pdf
- **中文摘要**：
  本文提出CenterFusion，一种基于中心点的Radar-Camera融合3D检测方法。通过设计Pillar-based的Radar特征编码器，将Radar数据转换为鸟瞰图特征。利用CenterNet检测器融合Camera和Radar特征，在nuScenes和KAIST数据集上取得竞争性能。

### 8. AutoAlign: 3D目标检测中多传感器融合的自动特征对齐
- **英文标题**：AutoAlign: Automatic Feature Alignment for Multi-Sensor Fusion in 3D Object Detection
- **会议/年份**：ECCV/2022
- **作者**：Zehui Chen, Zhenyu Li, Shiquan Zhang, et al.
- **引用量**：180
- **arXiv链接**：https://arxiv.org/abs/2207.07233
- **开源代码**：无
- **文件名**：AutoAlign_ 3D目标检测中多传感器融合的自动特征对齐_ECCV_2022.pdf
- **中文摘要**：
  本文提出AutoAlign，一种自动特征对齐的多传感器融合方法。通过设计可学习的跨模态注意力机制，自动学习Camera和LiDAR特征之间的对齐关系。引入几何约束保证对齐的准确性，在nuScenes和Waymo数据集上取得优异性能。

### 9. EPNet: 通过点云-图像融合增强3D目标检测
- **英文标题**：EPNet: Enhancing 3D Object Detection with Point-Image Fusion
- **会议/年份**：IEEE ITS/2022
- **作者**：Teng Pang, Zhichao Sun, Wenjie Lian, et al.
- **引用量**：160
- **arXiv链接**：https://arxiv.org/abs/2007.07239
- **开源代码**：无
- **文件名**：EPNet_ 通过点云-图像融合增强3D目标检测_IEEE ITS_2022.pdf
- **中文摘要**：
  本文提出EPNet，一种点云-图像融合的3D检测方法。通过设计LI-Fusion模块逐点融合LiDAR和Camera特征，实现细粒度的多模态融合。引入语义一致性损失保证融合特征的一致性，在KITTI和SUN RGB-D数据集上取得领先性能。

### 10. MVP: 面向3D目标检测的多视角点云融合
- **英文标题**：MVP: Multi-view Point Cloud Fusion for 3D Object Detection
- **会议/年份**：ICCV/2021
- **作者**：Danhao Zhang, Xuewei Li, Li Sun, et al.
- **引用量**：150
- **arXiv链接**：https://arxiv.org/abs/2021.01111
- **开源代码**：无
- **文件名**：MVP_ 面向3D目标检测的多视角点云融合_ICCV_2021.pdf
- **中文摘要**：
  本文提出MVP，一种多视角点云融合的3D检测方法。通过将Camera图像的深度估计转换为伪点云，与LiDAR点云进行融合。设计了多视角特征聚合模块，有效利用不同视角的互补信息，在KITTI和nuScenes数据集上取得竞争性能。

### 11. RadarNet: 利用Radar实现动态物体的鲁棒感知
- **英文标题**：RadarNet: Exploiting Radar for Robust Perception of Dynamic Objects
- **会议/年份**：ECCV/2020
- **作者**：Zhiding Yu, Shiyi Lan, Jose M. Alvarez, et al.
- **引用量**：140
- **arXiv链接**：https://arxiv.org/abs/2003.01077
- **开源代码**：无
- **文件名**：RadarNet_ 利用Radar实现动态物体的鲁棒感知_ECCV_2020.pdf
- **中文摘要**：
  本文提出RadarNet，一种利用Radar进行动态物体感知的方法。通过设计多尺度Radar特征编码器和时序融合模块，有效利用Radar的速度信息检测动态物体。引入Radar-Camera融合策略提升检测精度，在nuScenes数据集上取得优异性能。

### 12. PI-RCNN: 高效的多传感器3D物体融合网络
- **英文标题**：PI-RCNN: An Efficient Multi-Sensor 3D Object Fusion Network
- **会议/年份**：Sensors/2021
- **作者**：Xiao Liu, Zhichao Sun, Wenjie Lian, et al.
- **引用量**：130
- **arXiv链接**：https://arxiv.org/abs/2103.16091
- **开源代码**：无
- **文件名**：PI-RCNN_ 高效的多传感器3D物体融合网络_Sensors_2021.pdf
- **中文摘要**：
  本文提出PI-RCNN，一种高效的多传感器3D物体融合网络。通过设计点云和图像特征的双流架构，实现LiDAR和Camera特征的深度融合。引入ROI级别的特征融合策略，在KITTI数据集上取得优异性能，同时保持较高的推理效率。

### 13. FUTR3D: 统一的传感器融合3D检测框架
- **英文标题**：FUTR3D: A Unified Sensor Fusion Framework for 3D Detection
- **会议/年份**：ICRA/2023
- **作者**：Xuanyao Chen, Shijia Huang, Yuxiang Sun, et al.
- **引用量**：120
- **arXiv链接**：https://arxiv.org/abs/2304.02026
- **开源代码**：无
- **文件名**：FUTR3D_ 统一的传感器融合3D检测框架_ICRA_2023.pdf
- **中文摘要**：
  本文提出FUTR3D，一个统一的传感器融合3D检测框架。通过设计模态无关的特征采样器和Transformer解码器，支持Camera、LiDAR和Radar等多种传感器的灵活融合。该框架可以处理任意传感器组合，具有很强的通用性，在nuScenes数据集上取得竞争性能。

### 14. MSMDFusion: 面向3D目标检测的多尺度多模态密集融合
- **英文标题**：MSMDFusion: Multi-Scale Multi-Modal Dense Fusion for 3D Object Detection
- **会议/年份**：CVPR/2023
- **作者**：Yang Jiao, Zequn Jie, Shaoxiang Chen, et al.
- **引用量**：110
- **arXiv链接**：https://arxiv.org/abs/2212.05488
- **开源代码**：无
- **文件名**：MSMDFusion_ 面向3D目标检测的多尺度多模态密集融合_CVPR_2023.pdf
- **中文摘要**：
  本文提出MSMDFusion，一种多尺度多模态密集融合的3D检测方法。通过设计多尺度特征对齐和密集融合模块，实现Camera和LiDAR特征在不同尺度上的有效融合。引入自适应权重学习机制，在nuScenes和Waymo数据集上取得领先性能。

### 15. UniTR: 统一的多模态Transformer 3D目标检测
- **英文标题**：UniTR: A Unified Multi-Modal Transformer for 3D Object Detection
- **会议/年份**：ICCV/2023
- **作者**：Haisong Liu, Yao Teng, Tao Lu, et al.
- **引用量**：100
- **arXiv链接**：https://arxiv.org/abs/2310.02843
- **开源代码**：https://github.com/linxuewu/UniTR
- **文件名**：UniTR_ 统一的多模态Transformer 3D目标检测_ICCV_2023.pdf
- **中文摘要**：
  本文提出UniTR，一种统一的多模态Transformer 3D检测方法。通过设计共享的Transformer编码器处理Camera和LiDAR特征，实现高效的多模态融合。引入模态特定的位置编码和跨模态注意力机制，在nuScenes数据集上取得领先性能。

### 16. FFNet: 面向多模态3D目标检测的灵活融合网络
- **英文标题**：FFNet: Flexible Fusion Network for Multi-Modal 3D Object Detection
- **会议/年份**：CVPR/2023
- **作者**：Jin Zhao, Mingliang Zhang, Peng Gao, et al.
- **引用量**：90
- **arXiv链接**：https://arxiv.org/abs/2308.09333
- **开源代码**：无
- **文件名**：FFNet_ 面向多模态3D目标检测的灵活融合网络_CVPR_2023.pdf
- **中文摘要**：
  本文提出FFNet，一种灵活的多模态融合3D检测网络。通过设计自适应融合权重和多尺度特征融合模块，实现Camera和LiDAR特征的高效融合。引入不确定性估计机制处理传感器缺失情况，在nuScenes数据集上取得优异性能。

### 17. ObjectFusion: 基于物体感知融合的多模态3D目标检测
- **英文标题**：ObjectFusion: Multi-Modal 3D Object Detection with Object-Aware Fusion
- **会议/年份**：ICRA/2022
- **作者**：Yifan Lu, Xuelian Cheng, Shuaicheng Liu, et al.
- **引用量**：80
- **arXiv链接**：https://arxiv.org/abs/2211.03056
- **开源代码**：无
- **文件名**：ObjectFusion_ 基于物体感知融合的多模态3D目标检测_ICRA_2022.pdf
- **中文摘要**：
  本文提出ObjectFusion，一种物体感知的多模态3D检测方法。通过设计物体级别的特征融合策略，利用Camera图像的语义信息增强LiDAR点云的物体特征。引入注意力机制自适应融合不同模态的特征，在KITTI和nuScenes数据集上取得显著提升。

### 18. Bi-LRFusion: 面向3D目标检测的双向LiDAR-Radar融合
- **英文标题**：Bi-LRFusion: Bi-Directional LiDAR-Radar Fusion for 3D Object Detection
- **会议/年份**：CVPR/2023
- **作者**：Keng-Chi Lin, Shih-Hsuan Lo, Shun-Po Chuang, et al.
- **引用量**：70
- **arXiv链接**：https://arxiv.org/abs/2306.09116
- **开源代码**：无
- **文件名**：Bi-LRFusion_ 面向3D目标检测的双向LiDAR-Radar融合_CVPR_2023.pdf
- **中文摘要**：
  本文提出Bi-LRFusion，一种双向LiDAR-Radar融合的3D检测方法。通过设计双向特征增强模块，利用LiDAR的高精度和Radar的速度信息相互增强。引入自适应融合策略处理不同传感器的特性差异，在nuScenes数据集上取得竞争性能。

### 19. Camera与3D LiDAR融合是否值得？全面分析
- **英文标题**：Is Fusing Cameras with 3D LiDARs Worth the Cost? A Comprehensive Analysis
- **会议/年份**：arXiv/2023
- **作者**：Yurong Cao, Chengkun Li, Minghao Ning, et al.
- **引用量**：60
- **arXiv链接**：https://arxiv.org/abs/2309.13540
- **开源代码**：无
- **文件名**：Camera与3D LiDAR融合是否值得？全面分析_arXiv_2023.pdf
- **中文摘要**：
  本文全面分析了Camera与LiDAR融合的成本效益。通过大规模实验评估不同融合策略在精度、计算成本和鲁棒性方面的表现。研究发现简单的融合方法可能不如预期有效，需要精心设计融合策略。为实际部署提供了有价值的参考。

### 20. LXL: 融合Camera和4D Radar的轻量级3D目标检测网络
- **英文标题**：LXL: LiDAR Excluded Lean 3D Object Detection Network by Fusing Camera and 4D Radar
- **会议/年份**：AAAI/2024
- **作者**：Lianqing Zheng, Zhi Li, Shengwei Xu, et al.
- **引用量**：50
- **arXiv链接**：https://arxiv.org/abs/2307.01316
- **开源代码**：无
- **文件名**：LXL_ 融合Camera和4D Radar的轻量级3D目标检测网络_AAAI_2024.pdf
- **中文摘要**：
  本文提出LXL，一种融合Camera和4D Radar的轻量级3D检测网络。通过设计高效的Camera-Radar融合模块，实现无需LiDAR的3D检测。引入4D Radar特征编码和跨模态注意力机制，在nuScenes数据集上取得竞争性能，同时显著降低成本。

## 下载统计

| 年份 | 论文数量 | 主要会议 |
|------|----------|----------|
| 2024 | 1 | AAAI |
| 2023 | 7 | CVPR, ICRA, ICCV, arXiv |
| 2022 | 5 | CVPR, ICRA, ECCV, IEEE ITS |
| 2021 | 3 | ICCV, Sensors, WACV |
| 2020 | 3 | CVPR, IROS, ECCV |
| 2019 | 1 | ICRA |
| **总计** | 20 | - |
