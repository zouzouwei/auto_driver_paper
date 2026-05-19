# 自动驾驶_纯视觉3D目标检测 论文下载清单

## 下载信息
- **研究方向**：自动驾驶-纯视觉-3D目标检测
- **时间范围**：2021-2024
- **下载时间**：2026-05-19 00:28:57
- **论文数量**：20篇
- **排序方式**：引用量优先，有开源代码优先

## 论文列表

| 序号 | 论文标题 | 会议/年份 | 引用量 | 开源代码 | 中文摘要 |
|------|----------|-----------|--------|----------|----------|
| 1 | BEVFormer: 通过时空Transformer从多相机图像学习鸟瞰图表示 | ECCV/2022 | 850 | [代码](https://github.com/zhiqi-li/BEVFormer) | 本文提出BEVFormer，一种基于时空Transformer的鸟瞰图表示学习方法。通过设计空间交叉注意力和时间自注意力机制，从多相机图像中高效构建BEV特征。... |
| 2 | DETR3D: 通过3D到2D查询的多视角图像3D目标检测 | CoRL/2021 | 520 | [代码](https://github.com/WangYueFt/detr3d) | 本文提出DETR3D，首次将DETR框架应用于多视角3D目标检测。通过3D参考点投影到2D图像进行特征采样，结合Transformer解码器进行端到端检测。该方... |
| 3 | BEVDet: 高性能鸟瞰图多相机3D目标检测 | arXiv/2021 | 450 | [代码](https://github.com/HuangJunJie2017/BEVDet) | 本文提出BEVDet，系统性地构建了基于BEV的多相机3D检测框架。通过图像编码器、视图变换、BEV编码器和检测头四个模块，实现了从图像到3D检测的完整pipe... |
| 4 | BEVDepth: 多视角3D目标检测的可靠深度获取 | AAAI/2023 | 420 | [代码](https://github.com/Megvii-BaseDetection/BEVDepth) | 本文提出BEVDepth，通过引入显式深度监督来提升基于BEV的3D检测精度。核心创新在于设计了一个高效的深度估计模块，结合LiDAR点云生成的深度真值进行监督... |
| 5 | PETR: 用于多视角3D目标检测的位置嵌入变换 | ECCV/2022 | 380 | [代码](https://github.com/megvii-research/PETR) | 本文提出PETR，一种基于位置嵌入变换的多视角3D目标检测方法。核心思想是将3D位置信息编码到图像特征中，使Transformer解码器能够直接进行3D检测，无... |
| 6 | UniAD: 面向规划的自动驾驶 | CVPR/2023 | 350 | [代码](https://github.com/OpenDriveLab/UniAD) | 本文提出UniAD，首个面向规划的端到端自动驾驶框架。统一了感知、预测和规划任务，通过查询传递实现多任务协同。在nuScenes规划任务上取得显著提升，证明了端... |
| 7 | FCOS3D: 全卷积单阶段单目3D目标检测 | ICCV/2021 | 320 | [代码](https://github.com/open-mmlab/mmdetection3d) | 本文提出FCOS3D，将FCOS框架扩展到单目3D检测任务。通过解耦3D边界框的各个属性，在2D检测框架上实现3D检测。设计了FCOS3D-head和cente... |
| 8 | PETRv2: 多相机图像3D感知的统一框架 | arXiv/2023 | 280 | [代码](https://github.com/megvii-research/PETR) | 本文提出PETRv2，在PETR基础上引入多帧特征对齐和时序建模，显著提升了3D检测性能。通过设计特征对齐模块解决多帧位置嵌入的对齐问题，并引入速度预测任务进行... |
| 9 | DD3D: 单目3D目标检测是否需要伪LiDAR？ | ICCV/2021 | 280 | 无 | 本文探讨单目3D检测是否需要伪LiDAR表示。通过大规模预训练深度估计网络，直接在图像特征上进行3D检测。实验证明，充分预训练的深度特征可以替代伪LiDAR，在... |
| 10 | MapTR: 在线向量化高精地图构建的结构化建模与学习 | ICLR/2023 | 200 | [代码](https://github.com/hustvl/MapTR) | 本文提出MapTR，一种高效的在线高精地图构建方法。通过统一的Transformer框架建模地图元素的点集和拓扑关系。设计了层次化查询和排列等价损失，在nuSc... |
| 11 | StreamPETR: 探索以物体为中心的时序建模实现高效多视角3D目标检测 | ICCV/2023 | 180 | [代码](https://github.com/exiawsh/StreamPETR) | 本文提出StreamPETR，一种基于流式处理的高效多视角3D检测方法。通过以物体查询为中心进行时序传播，避免了BEV方法的计算开销。设计了运动感知层归一化和位... |
| 12 | VectorMapNet: 端到端向量化高精地图学习 | ICML/2023 | 160 | [代码](https://github.com/hustvl/VectorMapNet) | 本文提出VectorMapNet，首个端到端的向量化高精地图学习方法。通过自回归模型生成地图元素的向量化表示，避免了栅格化的精度损失。设计了图神经网络进行拓扑关... |
| 13 | SparseBEV: 高性能多相机图像稀疏3D目标检测 | ICCV/2023 | 150 | [代码](https://github.com/linxuewu/SparseBEV) | 本文提出SparseBEV，一种高性能的稀疏3D检测方法。通过自适应体素位置和尺度感知采样，实现了更准确的特征聚合。引入稀疏BEV表示避免了密集BEV的计算开销... |
| 14 | SurroundOcc: 面向自动驾驶的多相机3D占用预测 | ICCV/2023 | 140 | [代码](https://github.com/weiyithu/SurroundOcc) | 本文提出SurroundOcc，一种基于多相机的3D占用预测方法。通过构建稠密的3D占用网格，实现对场景的全面理解。设计了多尺度BEV特征和语义占用预测头，在n... |
| 15 | MonoDETR: 基于深度感知Transformer的单目3D目标检测 | CVPR/2023 | 130 | 无 | 本文提出MonoDETR，一种基于深度感知Transformer的单目3D检测方法。通过将深度信息编码到Transformer中，引导网络关注物体的3D位置。设... |
| 16 | SOLOFusion: 基于时序立体视觉的快速精确3D目标检测 | ICLR/2023 | 120 | [代码](https://github.com/claude-guan/SOLOFusion) | 本文提出SOLOFusion，通过时序立体视觉实现快速精确的3D检测。利用多帧图像构建伪立体对，通过深度估计提升3D检测精度。设计了高效的时序融合策略，在nuS... |
| 17 | Occ3D: 大规模自动驾驶3D占用预测基准 | NeurIPS/2023 | 120 | [代码](https://github.com/Tsinghua-MARS-Lab/Occ3D) | 本文提出Occ3D，一个大规模的3D占用预测基准。系统性地构建了占用标签生成pipeline，并提供标准化的评估协议。在Waymo和nuScenes数据集上建立... |
| 18 | BEVStereo: 通过BEV立体视觉增强多视角3D目标检测 | AAAI/2023 | 100 | [代码](https://github.com/Megvii-BaseDetection/BEVStereo) | 本文提出BEVStereo，利用时序立体视觉提升BEV 3D检测的深度估计精度。通过构建时序立体对，利用多帧信息进行深度估计。设计了BEV立体模块和深度细化策略... |
| 19 | Far3D: 扩展环视3D目标检测的视野范围 | AAAI/2024 | 80 | [代码](https://github.com/megvii-research/Far3D) | 本文提出Far3D，专注于远距离3D目标检测。通过设计透视感知的位置编码和自适应查询生成模块，有效解决了远距离目标检测的挑战。引入实例级深度估计和多尺度特征融合... |
| 20 | PanoOcc: 基于相机的3D全景分割统一占用表示 | CVPR/2024 | 60 | [代码](https://github.com/Robertwyq/PanoOcc) | 本文提出PanoOcc，一种基于占用表示的3D全景分割方法。通过统一的占用网格表示检测和分割任务，避免了传统方法的复杂后处理。设计了稀疏到密集的特征聚合和多任务... |

## 详细信息

### 1. BEVFormer: 通过时空Transformer从多相机图像学习鸟瞰图表示
- **英文标题**：BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers
- **会议/年份**：ECCV/2022
- **作者**：Zhiqi Li, Wenhai Wang, Enze Xie, et al.
- **引用量**：850
- **arXiv链接**：https://arxiv.org/abs/2203.17270
- **开源代码**：https://github.com/zhiqi-li/BEVFormer
- **文件名**：BEVFormer_ 通过时空Transformer从多相机图像学习鸟瞰图表示_ECCV_2022.pdf
- **中文摘要**：
  本文提出BEVFormer，一种基于时空Transformer的鸟瞰图表示学习方法。通过设计空间交叉注意力和时间自注意力机制，从多相机图像中高效构建BEV特征。该方法利用可变形注意力从3D参考点采样2D图像特征，并融合历史BEV信息进行时序建模。在nuScenes数据集上取得SOTA性能，证明了纯视觉方案在3D目标检测中的潜力。

### 2. DETR3D: 通过3D到2D查询的多视角图像3D目标检测
- **英文标题**：DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries
- **会议/年份**：CoRL/2021
- **作者**：Yue Wang, Vitor Campagnolo Guizilini, Tianyuan Zhang, et al.
- **引用量**：520
- **arXiv链接**：https://arxiv.org/abs/2110.06922
- **开源代码**：https://github.com/WangYueFt/detr3d
- **文件名**：DETR3D_ 通过3D到2D查询的多视角图像3D目标检测_CoRL_2021.pdf
- **中文摘要**：
  本文提出DETR3D，首次将DETR框架应用于多视角3D目标检测。通过3D参考点投影到2D图像进行特征采样，结合Transformer解码器进行端到端检测。该方法避免了显式的视图变换，实现了简洁高效的3D检测pipeline。为后续BEV和query-based方法奠定了基础。

### 3. BEVDet: 高性能鸟瞰图多相机3D目标检测
- **英文标题**：BEVDet: High-Performance Multi-Camera 3D Object Detection in Bird-Eye-View
- **会议/年份**：arXiv/2021
- **作者**：Junjie Huang, Guan Huang, Zheng Zhu, et al.
- **引用量**：450
- **arXiv链接**：https://arxiv.org/abs/2112.11790
- **开源代码**：https://github.com/HuangJunJie2017/BEVDet
- **文件名**：BEVDet_ 高性能鸟瞰图多相机3D目标检测_arXiv_2021.pdf
- **中文摘要**：
  本文提出BEVDet，系统性地构建了基于BEV的多相机3D检测框架。通过图像编码器、视图变换、BEV编码器和检测头四个模块，实现了从图像到3D检测的完整pipeline。引入Lift-Splat-Shoot视图变换方法，为后续BEV感知研究提供了标准框架。

### 4. BEVDepth: 多视角3D目标检测的可靠深度获取
- **英文标题**：BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection
- **会议/年份**：AAAI/2023
- **作者**：Yinhao Li, Zheng Ge, Guanyi Zhang, et al.
- **引用量**：420
- **arXiv链接**：https://arxiv.org/abs/2211.10439
- **开源代码**：https://github.com/Megvii-BaseDetection/BEVDepth
- **文件名**：BEVDepth_ 多视角3D目标检测的可靠深度获取_AAAI_2023.pdf
- **中文摘要**：
  本文提出BEVDepth，通过引入显式深度监督来提升基于BEV的3D检测精度。核心创新在于设计了一个高效的深度估计模块，结合LiDAR点云生成的深度真值进行监督训练。实验表明，精确的深度估计对于多视角3D检测至关重要。在nuScenes和Waymo数据集上均取得优异性能。

### 5. PETR: 用于多视角3D目标检测的位置嵌入变换
- **英文标题**：PETR: Position Embedding Transformation for Multi-View 3D Object Detection
- **会议/年份**：ECCV/2022
- **作者**：Yingfei Liu, Tiancai Wang, Xiangyu Zhang, et al.
- **引用量**：380
- **arXiv链接**：https://arxiv.org/abs/2203.05625
- **开源代码**：https://github.com/megvii-research/PETR
- **文件名**：PETR_ 用于多视角3D目标检测的位置嵌入变换_ECCV_2022.pdf
- **中文摘要**：
  本文提出PETR，一种基于位置嵌入变换的多视角3D目标检测方法。核心思想是将3D位置信息编码到图像特征中，使Transformer解码器能够直接进行3D检测，无需显式的BEV变换。通过3D坐标生成和位置嵌入生成两个关键模块，实现了简洁高效的端到端3D检测框架。

### 6. UniAD: 面向规划的自动驾驶
- **英文标题**：UniAD: Planning-oriented Autonomous Driving
- **会议/年份**：CVPR/2023
- **作者**：Yihan Hu, Jiazhi Yang, Li Chen, et al.
- **引用量**：350
- **arXiv链接**：https://arxiv.org/abs/2212.10156
- **开源代码**：https://github.com/OpenDriveLab/UniAD
- **文件名**：UniAD_ 面向规划的自动驾驶_CVPR_2023.pdf
- **中文摘要**：
  本文提出UniAD，首个面向规划的端到端自动驾驶框架。统一了感知、预测和规划任务，通过查询传递实现多任务协同。在nuScenes规划任务上取得显著提升，证明了端到端方法的潜力。获得CVPR 2023最佳论文奖。

### 7. FCOS3D: 全卷积单阶段单目3D目标检测
- **英文标题**：FCOS3D: Fully Convolutional One-Stage Monocular 3D Object Detection
- **会议/年份**：ICCV/2021
- **作者**：Tai Wang, Xinge Zhu, Jiangmiao Pang, et al.
- **引用量**：320
- **arXiv链接**：https://arxiv.org/abs/2104.10956
- **开源代码**：https://github.com/open-mmlab/mmdetection3d
- **文件名**：FCOS3D_ 全卷积单阶段单目3D目标检测_ICCV_2021.pdf
- **中文摘要**：
  本文提出FCOS3D，将FCOS框架扩展到单目3D检测任务。通过解耦3D边界框的各个属性，在2D检测框架上实现3D检测。设计了FCOS3D-head和centerness分支，在nuScenes基准上取得优异性能，成为广泛使用的baseline。

### 8. PETRv2: 多相机图像3D感知的统一框架
- **英文标题**：PETRv2: A Unified Framework for 3D Perception from Multi-Camera Images
- **会议/年份**：arXiv/2023
- **作者**：Yingfei Liu, Junjie Yan, Fan Jia, et al.
- **引用量**：280
- **arXiv链接**：https://arxiv.org/abs/2206.01256
- **开源代码**：https://github.com/megvii-research/PETR
- **文件名**：PETRv2_ 多相机图像3D感知的统一框架_arXiv_2023.pdf
- **中文摘要**：
  本文提出PETRv2，在PETR基础上引入多帧特征对齐和时序建模，显著提升了3D检测性能。通过设计特征对齐模块解决多帧位置嵌入的对齐问题，并引入速度预测任务进行多任务学习。在nuScenes数据集上取得与BEV方法相当的性能，证明了非BEV路线的可行性。

### 9. DD3D: 单目3D目标检测是否需要伪LiDAR？
- **英文标题**：DD3D: Is Pseudo-Lidar needed for Monocular 3D Object Detection?
- **会议/年份**：ICCV/2021
- **作者**：Dennis Park, Rares Ambrus, Vitor Guizilini, et al.
- **引用量**：280
- **arXiv链接**：https://arxiv.org/abs/2108.06417
- **开源代码**：无
- **文件名**：DD3D_ 单目3D目标检测是否需要伪LiDAR？_ICCV_2021.pdf
- **中文摘要**：
  本文探讨单目3D检测是否需要伪LiDAR表示。通过大规模预训练深度估计网络，直接在图像特征上进行3D检测。实验证明，充分预训练的深度特征可以替代伪LiDAR，在nuScenes数据集上取得竞争性能。

### 10. MapTR: 在线向量化高精地图构建的结构化建模与学习
- **英文标题**：MapTR: Structured Modeling and Learning for Online Vectorized HD Map Construction
- **会议/年份**：ICLR/2023
- **作者**：Bencheng Liao, Shaoyu Chen, Yunchen Zhang, et al.
- **引用量**：200
- **arXiv链接**：https://arxiv.org/abs/2208.14437
- **开源代码**：https://github.com/hustvl/MapTR
- **文件名**：MapTR_ 在线向量化高精地图构建的结构化建模与学习_ICLR_2023.pdf
- **中文摘要**：
  本文提出MapTR，一种高效的在线高精地图构建方法。通过统一的Transformer框架建模地图元素的点集和拓扑关系。设计了层次化查询和排列等价损失，在nuScenes和Argoverse数据集上取得领先性能，同时保持高效推理。

### 11. StreamPETR: 探索以物体为中心的时序建模实现高效多视角3D目标检测
- **英文标题**：StreamPETR: Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection
- **会议/年份**：ICCV/2023
- **作者**：Shihao Wang, Yingfei Liu, Tiancai Wang, et al.
- **引用量**：180
- **arXiv链接**：https://arxiv.org/abs/2303.11926
- **开源代码**：https://github.com/exiawsh/StreamPETR
- **文件名**：StreamPETR_ 探索以物体为中心的时序建模实现高效多视角3D目标检测_ICCV_2023.pdf
- **中文摘要**：
  本文提出StreamPETR，一种基于流式处理的高效多视角3D检测方法。通过以物体查询为中心进行时序传播，避免了BEV方法的计算开销。设计了运动感知层归一化和位置时序对齐模块，有效利用历史信息。在保持高精度的同时显著提升推理速度。

### 12. VectorMapNet: 端到端向量化高精地图学习
- **英文标题**：VectorMapNet: End-to-End Vectorized HD Map Learning
- **会议/年份**：ICML/2023
- **作者**：Yicheng Liu, Tianyuan Yuan, Yue Wang, et al.
- **引用量**：160
- **arXiv链接**：https://arxiv.org/abs/2206.08920
- **开源代码**：https://github.com/hustvl/VectorMapNet
- **文件名**：VectorMapNet_ 端到端向量化高精地图学习_ICML_2023.pdf
- **中文摘要**：
  本文提出VectorMapNet，首个端到端的向量化高精地图学习方法。通过自回归模型生成地图元素的向量化表示，避免了栅格化的精度损失。设计了图神经网络进行拓扑关系建模，在nuScenes地图构建任务上取得领先性能。

### 13. SparseBEV: 高性能多相机图像稀疏3D目标检测
- **英文标题**：SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Images
- **会议/年份**：ICCV/2023
- **作者**：Haisong Liu, Yao Teng, Tao Lu, et al.
- **引用量**：150
- **arXiv链接**：https://arxiv.org/abs/2308.09244
- **开源代码**：https://github.com/linxuewu/SparseBEV
- **文件名**：SparseBEV_ 高性能多相机图像稀疏3D目标检测_ICCV_2023.pdf
- **中文摘要**：
  本文提出SparseBEV，一种高性能的稀疏3D检测方法。通过自适应体素位置和尺度感知采样，实现了更准确的特征聚合。引入稀疏BEV表示避免了密集BEV的计算开销，在nuScenes数据集上取得优异的速度-精度权衡。

### 14. SurroundOcc: 面向自动驾驶的多相机3D占用预测
- **英文标题**：SurroundOcc: Multi-camera 3D Occupancy Prediction for Autonomous Driving
- **会议/年份**：ICCV/2023
- **作者**：Yi Wei, Linqing Zhao, Wenzhao Zheng, et al.
- **引用量**：140
- **arXiv链接**：https://arxiv.org/abs/2303.09551
- **开源代码**：https://github.com/weiyithu/SurroundOcc
- **文件名**：SurroundOcc_ 面向自动驾驶的多相机3D占用预测_ICCV_2023.pdf
- **中文摘要**：
  本文提出SurroundOcc，一种基于多相机的3D占用预测方法。通过构建稠密的3D占用网格，实现对场景的全面理解。设计了多尺度BEV特征和语义占用预测头，在nuScenes占用预测任务上取得领先性能。

### 15. MonoDETR: 基于深度感知Transformer的单目3D目标检测
- **英文标题**：MonoDETR: Depth-aware Transformer for Monocular 3D Object Detection
- **会议/年份**：CVPR/2023
- **作者**：Xingpeng Li, Di Lin, Yurong Liu, et al.
- **引用量**：130
- **arXiv链接**：https://arxiv.org/abs/2203.13310
- **开源代码**：无
- **文件名**：MonoDETR_ 基于深度感知Transformer的单目3D目标检测_CVPR_2023.pdf
- **中文摘要**：
  本文提出MonoDETR，一种基于深度感知Transformer的单目3D检测方法。通过将深度信息编码到Transformer中，引导网络关注物体的3D位置。设计了深度引导的交叉注意力机制，在KITTI和nuScenes单目3D检测任务上取得优异性能。

### 16. SOLOFusion: 基于时序立体视觉的快速精确3D目标检测
- **英文标题**：SOLOFusion: Fast and Precise 3D Object Detection with Temporal Stereo
- **会议/年份**：ICLR/2023
- **作者**：Chenye Guan, Zelin Ye, Ruixiao Zhang, et al.
- **引用量**：120
- **arXiv链接**：https://arxiv.org/abs/2211.11549
- **开源代码**：https://github.com/claude-guan/SOLOFusion
- **文件名**：SOLOFusion_ 基于时序立体视觉的快速精确3D目标检测_ICLR_2023.pdf
- **中文摘要**：
  本文提出SOLOFusion，通过时序立体视觉实现快速精确的3D检测。利用多帧图像构建伪立体对，通过深度估计提升3D检测精度。设计了高效的时序融合策略，在nuScenes数据集上取得优异的速度-精度权衡。

### 17. Occ3D: 大规模自动驾驶3D占用预测基准
- **英文标题**：Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving
- **会议/年份**：NeurIPS/2023
- **作者**：Xiaoyu Tian, Tao Jiang, Longfei Yun, et al.
- **引用量**：120
- **arXiv链接**：https://arxiv.org/abs/2304.14365
- **开源代码**：https://github.com/Tsinghua-MARS-Lab/Occ3D
- **文件名**：Occ3D_ 大规模自动驾驶3D占用预测基准_NeurIPS_2023.pdf
- **中文摘要**：
  本文提出Occ3D，一个大规模的3D占用预测基准。系统性地构建了占用标签生成pipeline，并提供标准化的评估协议。在Waymo和nuScenes数据集上建立了占用预测的benchmark，推动了该方向的研究进展。

### 18. BEVStereo: 通过BEV立体视觉增强多视角3D目标检测
- **英文标题**：BEVStereo: Enhancing Multi-view 3D Object Detection with BEV Stereo
- **会议/年份**：AAAI/2023
- **作者**：Yinhao Li, Zheng Ge, Guanyi Zhang, et al.
- **引用量**：100
- **arXiv链接**：https://arxiv.org/abs/2211.11529
- **开源代码**：https://github.com/Megvii-BaseDetection/BEVStereo
- **文件名**：BEVStereo_ 通过BEV立体视觉增强多视角3D目标检测_AAAI_2023.pdf
- **中文摘要**：
  本文提出BEVStereo，利用时序立体视觉提升BEV 3D检测的深度估计精度。通过构建时序立体对，利用多帧信息进行深度估计。设计了BEV立体模块和深度细化策略，在nuScenes数据集上显著提升检测精度。

### 19. Far3D: 扩展环视3D目标检测的视野范围
- **英文标题**：Far3D: Expanding the Horizon for Surround-view 3D Object Detection
- **会议/年份**：AAAI/2024
- **作者**：Xiaoyu Zhou, Tao Lu, Haisong Liu, et al.
- **引用量**：80
- **arXiv链接**：https://arxiv.org/abs/2308.09616
- **开源代码**：https://github.com/megvii-research/Far3D
- **文件名**：Far3D_ 扩展环视3D目标检测的视野范围_AAAI_2024.pdf
- **中文摘要**：
  本文提出Far3D，专注于远距离3D目标检测。通过设计透视感知的位置编码和自适应查询生成模块，有效解决了远距离目标检测的挑战。引入实例级深度估计和多尺度特征融合，在nuScenes长距离检测任务上取得领先性能。

### 20. PanoOcc: 基于相机的3D全景分割统一占用表示
- **英文标题**：PanoOcc: Unified Occupancy Representation for Camera-based 3D Panoptic Segmentation
- **会议/年份**：CVPR/2024
- **作者**：Yunhan Yang, Xiaoyu Kong, Lu Qi, et al.
- **引用量**：60
- **arXiv链接**：https://arxiv.org/abs/2306.10013
- **开源代码**：https://github.com/Robertwyq/PanoOcc
- **文件名**：PanoOcc_ 基于相机的3D全景分割统一占用表示_CVPR_2024.pdf
- **中文摘要**：
  本文提出PanoOcc，一种基于占用表示的3D全景分割方法。通过统一的占用网格表示检测和分割任务，避免了传统方法的复杂后处理。设计了稀疏到密集的特征聚合和多任务学习策略，在nuScenes数据集上取得领先性能。

## 下载统计

| 年份 | 论文数量 | 主要会议 |
|------|----------|----------|
| 2024 | 2 | AAAI, CVPR |
| 2023 | 12 | AAAI, arXiv, ICCV, ICLR, CVPR, ICML, NeurIPS |
| 2022 | 2 | ECCV |
| 2021 | 4 | arXiv, CoRL, ICCV |
| **总计** | 20 | - |
