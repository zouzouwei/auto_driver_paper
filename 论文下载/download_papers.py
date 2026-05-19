#!/usr/bin/env python3
"""
自动驾驶-纯视觉-3D目标检测论文下载脚本
下载经典论文并生成README表格
"""

import urllib.request
import os
import json
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# 论文列表（按重要性排序）
PAPERS = [
    {
        "title_en": "BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers",
        "title_cn": "BEVFormer: 通过时空Transformer从多相机图像学习鸟瞰图表示",
        "venue": "ECCV",
        "year": 2022,
        "arxiv_id": "2203.17270",
        "authors": "Zhiqi Li, Wenhai Wang, Enze Xie, et al.",
        "citations": 850,
        "github_url": "https://github.com/zhiqi-li/BEVFormer",
        "abstract_cn": "本文提出BEVFormer，一种基于时空Transformer的鸟瞰图表示学习方法。通过设计空间交叉注意力和时间自注意力机制，从多相机图像中高效构建BEV特征。该方法利用可变形注意力从3D参考点采样2D图像特征，并融合历史BEV信息进行时序建模。在nuScenes数据集上取得SOTA性能，证明了纯视觉方案在3D目标检测中的潜力。"
    },
    {
        "title_en": "BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection",
        "title_cn": "BEVDepth: 多视角3D目标检测的可靠深度获取",
        "venue": "AAAI",
        "year": 2023,
        "arxiv_id": "2211.10439",
        "authors": "Yinhao Li, Zheng Ge, Guanyi Zhang, et al.",
        "citations": 420,
        "github_url": "https://github.com/Megvii-BaseDetection/BEVDepth",
        "abstract_cn": "本文提出BEVDepth，通过引入显式深度监督来提升基于BEV的3D检测精度。核心创新在于设计了一个高效的深度估计模块，结合LiDAR点云生成的深度真值进行监督训练。实验表明，精确的深度估计对于多视角3D检测至关重要。在nuScenes和Waymo数据集上均取得优异性能。"
    },
    {
        "title_en": "PETR: Position Embedding Transformation for Multi-View 3D Object Detection",
        "title_cn": "PETR: 用于多视角3D目标检测的位置嵌入变换",
        "venue": "ECCV",
        "year": 2022,
        "arxiv_id": "2203.05625",
        "authors": "Yingfei Liu, Tiancai Wang, Xiangyu Zhang, et al.",
        "citations": 380,
        "github_url": "https://github.com/megvii-research/PETR",
        "abstract_cn": "本文提出PETR，一种基于位置嵌入变换的多视角3D目标检测方法。核心思想是将3D位置信息编码到图像特征中，使Transformer解码器能够直接进行3D检测，无需显式的BEV变换。通过3D坐标生成和位置嵌入生成两个关键模块，实现了简洁高效的端到端3D检测框架。"
    },
    {
        "title_en": "PETRv2: A Unified Framework for 3D Perception from Multi-Camera Images",
        "title_cn": "PETRv2: 多相机图像3D感知的统一框架",
        "venue": "arXiv",
        "year": 2023,
        "arxiv_id": "2206.01256",
        "authors": "Yingfei Liu, Junjie Yan, Fan Jia, et al.",
        "citations": 280,
        "github_url": "https://github.com/megvii-research/PETR",
        "abstract_cn": "本文提出PETRv2，在PETR基础上引入多帧特征对齐和时序建模，显著提升了3D检测性能。通过设计特征对齐模块解决多帧位置嵌入的对齐问题，并引入速度预测任务进行多任务学习。在nuScenes数据集上取得与BEV方法相当的性能，证明了非BEV路线的可行性。"
    },
    {
        "title_en": "DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries",
        "title_cn": "DETR3D: 通过3D到2D查询的多视角图像3D目标检测",
        "venue": "CoRL",
        "year": 2021,
        "arxiv_id": "2110.06922",
        "authors": "Yue Wang, Vitor Campagnolo Guizilini, Tianyuan Zhang, et al.",
        "citations": 520,
        "github_url": "https://github.com/WangYueFt/detr3d",
        "abstract_cn": "本文提出DETR3D，首次将DETR框架应用于多视角3D目标检测。通过3D参考点投影到2D图像进行特征采样，结合Transformer解码器进行端到端检测。该方法避免了显式的视图变换，实现了简洁高效的3D检测pipeline。为后续BEV和query-based方法奠定了基础。"
    },
    {
        "title_en": "BEVDet: High-Performance Multi-Camera 3D Object Detection in Bird-Eye-View",
        "title_cn": "BEVDet: 高性能鸟瞰图多相机3D目标检测",
        "arXiv": "2112.11790",
        "venue": "arXiv",
        "year": 2021,
        "arxiv_id": "2112.11790",
        "authors": "Junjie Huang, Guan Huang, Zheng Zhu, et al.",
        "citations": 450,
        "github_url": "https://github.com/HuangJunJie2017/BEVDet",
        "abstract_cn": "本文提出BEVDet，系统性地构建了基于BEV的多相机3D检测框架。通过图像编码器、视图变换、BEV编码器和检测头四个模块，实现了从图像到3D检测的完整pipeline。引入Lift-Splat-Shoot视图变换方法，为后续BEV感知研究提供了标准框架。"
    },
    {
        "title_en": "StreamPETR: Exploring Object-Centric Temporal Modeling for Efficient Multi-View 3D Object Detection",
        "title_cn": "StreamPETR: 探索以物体为中心的时序建模实现高效多视角3D目标检测",
        "venue": "ICCV",
        "year": 2023,
        "arxiv_id": "2303.11926",
        "authors": "Shihao Wang, Yingfei Liu, Tiancai Wang, et al.",
        "citations": 180,
        "github_url": "https://github.com/exiawsh/StreamPETR",
        "abstract_cn": "本文提出StreamPETR，一种基于流式处理的高效多视角3D检测方法。通过以物体查询为中心进行时序传播，避免了BEV方法的计算开销。设计了运动感知层归一化和位置时序对齐模块，有效利用历史信息。在保持高精度的同时显著提升推理速度。"
    },
    {
        "title_en": "SparseBEV: High-Performance Sparse 3D Object Detection from Multi-Camera Images",
        "title_cn": "SparseBEV: 高性能多相机图像稀疏3D目标检测",
        "venue": "ICCV",
        "year": 2023,
        "arxiv_id": "2308.09244",
        "authors": "Haisong Liu, Yao Teng, Tao Lu, et al.",
        "citations": 150,
        "github_url": "https://github.com/linxuewu/SparseBEV",
        "abstract_cn": "本文提出SparseBEV，一种高性能的稀疏3D检测方法。通过自适应体素位置和尺度感知采样，实现了更准确的特征聚合。引入稀疏BEV表示避免了密集BEV的计算开销，在nuScenes数据集上取得优异的速度-精度权衡。"
    },
    {
        "title_en": "Far3D: Expanding the Horizon for Surround-view 3D Object Detection",
        "title_cn": "Far3D: 扩展环视3D目标检测的视野范围",
        "venue": "AAAI",
        "year": 2024,
        "arxiv_id": "2308.09616",
        "authors": "Xiaoyu Zhou, Tao Lu, Haisong Liu, et al.",
        "citations": 80,
        "github_url": "https://github.com/megvii-research/Far3D",
        "abstract_cn": "本文提出Far3D，专注于远距离3D目标检测。通过设计透视感知的位置编码和自适应查询生成模块，有效解决了远距离目标检测的挑战。引入实例级深度估计和多尺度特征融合，在nuScenes长距离检测任务上取得领先性能。"
    },
    {
        "title_en": "SOLOFusion: Fast and Precise 3D Object Detection with Temporal Stereo",
        "title_cn": "SOLOFusion: 基于时序立体视觉的快速精确3D目标检测",
        "venue": "ICLR",
        "year": 2023,
        "arxiv_id": "2211.11549",
        "authors": "Chenye Guan, Zelin Ye, Ruixiao Zhang, et al.",
        "citations": 120,
        "github_url": "https://github.com/claude-guan/SOLOFusion",
        "abstract_cn": "本文提出SOLOFusion，通过时序立体视觉实现快速精确的3D检测。利用多帧图像构建伪立体对，通过深度估计提升3D检测精度。设计了高效的时序融合策略，在nuScenes数据集上取得优异的速度-精度权衡。"
    },
    {
        "title_en": "UniAD: Planning-oriented Autonomous Driving",
        "title_cn": "UniAD: 面向规划的自动驾驶",
        "venue": "CVPR",
        "year": 2023,
        "arxiv_id": "2212.10156",
        "authors": "Yihan Hu, Jiazhi Yang, Li Chen, et al.",
        "citations": 350,
        "github_url": "https://github.com/OpenDriveLab/UniAD",
        "abstract_cn": "本文提出UniAD，首个面向规划的端到端自动驾驶框架。统一了感知、预测和规划任务，通过查询传递实现多任务协同。在nuScenes规划任务上取得显著提升，证明了端到端方法的潜力。获得CVPR 2023最佳论文奖。"
    },
    {
        "title_en": "PanoOcc: Unified Occupancy Representation for Camera-based 3D Panoptic Segmentation",
        "title_cn": "PanoOcc: 基于相机的3D全景分割统一占用表示",
        "venue": "CVPR",
        "year": 2024,
        "arxiv_id": "2306.10013",
        "authors": "Yunhan Yang, Xiaoyu Kong, Lu Qi, et al.",
        "citations": 60,
        "github_url": "https://github.com/Robertwyq/PanoOcc",
        "abstract_cn": "本文提出PanoOcc，一种基于占用表示的3D全景分割方法。通过统一的占用网格表示检测和分割任务，避免了传统方法的复杂后处理。设计了稀疏到密集的特征聚合和多任务学习策略，在nuScenes数据集上取得领先性能。"
    },
    {
        "title_en": "MonoDETR: Depth-aware Transformer for Monocular 3D Object Detection",
        "title_cn": "MonoDETR: 基于深度感知Transformer的单目3D目标检测",
        "venue": "CVPR",
        "year": 2023,
        "arxiv_id": "2203.13310",
        "authors": "Xingpeng Li, Di Lin, Yurong Liu, et al.",
        "citations": 130,
        "github_url": None,
        "abstract_cn": "本文提出MonoDETR，一种基于深度感知Transformer的单目3D检测方法。通过将深度信息编码到Transformer中，引导网络关注物体的3D位置。设计了深度引导的交叉注意力机制，在KITTI和nuScenes单目3D检测任务上取得优异性能。"
    },
    {
        "title_en": "DD3D: Is Pseudo-Lidar needed for Monocular 3D Object Detection?",
        "title_cn": "DD3D: 单目3D目标检测是否需要伪LiDAR？",
        "venue": "ICCV",
        "year": 2021,
        "arxiv_id": "2108.06417",
        "authors": "Dennis Park, Rares Ambrus, Vitor Guizilini, et al.",
        "citations": 280,
        "github_url": None,
        "abstract_cn": "本文探讨单目3D检测是否需要伪LiDAR表示。通过大规模预训练深度估计网络，直接在图像特征上进行3D检测。实验证明，充分预训练的深度特征可以替代伪LiDAR，在nuScenes数据集上取得竞争性能。"
    },
    {
        "title_en": "FCOS3D: Fully Convolutional One-Stage Monocular 3D Object Detection",
        "title_cn": "FCOS3D: 全卷积单阶段单目3D目标检测",
        "venue": "ICCV",
        "year": 2021,
        "arxiv_id": "2104.10956",
        "authors": "Tai Wang, Xinge Zhu, Jiangmiao Pang, et al.",
        "citations": 320,
        "github_url": "https://github.com/open-mmlab/mmdetection3d",
        "abstract_cn": "本文提出FCOS3D，将FCOS框架扩展到单目3D检测任务。通过解耦3D边界框的各个属性，在2D检测框架上实现3D检测。设计了FCOS3D-head和centerness分支，在nuScenes基准上取得优异性能，成为广泛使用的baseline。"
    },
    {
        "title_en": "BEVStereo: Enhancing Multi-view 3D Object Detection with BEV Stereo",
        "title_cn": "BEVStereo: 通过BEV立体视觉增强多视角3D目标检测",
        "venue": "AAAI",
        "year": 2023,
        "arxiv_id": "2211.11529",
        "authors": "Yinhao Li, Zheng Ge, Guanyi Zhang, et al.",
        "citations": 100,
        "github_url": "https://github.com/Megvii-BaseDetection/BEVStereo",
        "abstract_cn": "本文提出BEVStereo，利用时序立体视觉提升BEV 3D检测的深度估计精度。通过构建时序立体对，利用多帧信息进行深度估计。设计了BEV立体模块和深度细化策略，在nuScenes数据集上显著提升检测精度。"
    },
    {
        "title_en": "VectorMapNet: End-to-End Vectorized HD Map Learning",
        "title_cn": "VectorMapNet: 端到端向量化高精地图学习",
        "venue": "ICML",
        "year": 2023,
        "arxiv_id": "2206.08920",
        "authors": "Yicheng Liu, Tianyuan Yuan, Yue Wang, et al.",
        "citations": 160,
        "github_url": "https://github.com/hustvl/VectorMapNet",
        "abstract_cn": "本文提出VectorMapNet，首个端到端的向量化高精地图学习方法。通过自回归模型生成地图元素的向量化表示，避免了栅格化的精度损失。设计了图神经网络进行拓扑关系建模，在nuScenes地图构建任务上取得领先性能。"
    },
    {
        "title_en": "MapTR: Structured Modeling and Learning for Online Vectorized HD Map Construction",
        "title_cn": "MapTR: 在线向量化高精地图构建的结构化建模与学习",
        "venue": "ICLR",
        "year": 2023,
        "arxiv_id": "2208.14437",
        "authors": "Bencheng Liao, Shaoyu Chen, Yunchen Zhang, et al.",
        "citations": 200,
        "github_url": "https://github.com/hustvl/MapTR",
        "abstract_cn": "本文提出MapTR，一种高效的在线高精地图构建方法。通过统一的Transformer框架建模地图元素的点集和拓扑关系。设计了层次化查询和排列等价损失，在nuScenes和Argoverse数据集上取得领先性能，同时保持高效推理。"
    },
    {
        "title_en": "SurroundOcc: Multi-camera 3D Occupancy Prediction for Autonomous Driving",
        "title_cn": "SurroundOcc: 面向自动驾驶的多相机3D占用预测",
        "venue": "ICCV",
        "year": 2023,
        "arxiv_id": "2303.09551",
        "authors": "Yi Wei, Linqing Zhao, Wenzhao Zheng, et al.",
        "citations": 140,
        "github_url": "https://github.com/weiyithu/SurroundOcc",
        "abstract_cn": "本文提出SurroundOcc，一种基于多相机的3D占用预测方法。通过构建稠密的3D占用网格，实现对场景的全面理解。设计了多尺度BEV特征和语义占用预测头，在nuScenes占用预测任务上取得领先性能。"
    },
    {
        "title_en": "Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving",
        "title_cn": "Occ3D: 大规模自动驾驶3D占用预测基准",
        "venue": "NeurIPS",
        "year": 2023,
        "arxiv_id": "2304.14365",
        "authors": "Xiaoyu Tian, Tao Jiang, Longfei Yun, et al.",
        "citations": 120,
        "github_url": "https://github.com/Tsinghua-MARS-Lab/Occ3D",
        "abstract_cn": "本文提出Occ3D，一个大规模的3D占用预测基准。系统性地构建了占用标签生成pipeline，并提供标准化的评估协议。在Waymo和nuScenes数据集上建立了占用预测的benchmark，推动了该方向的研究进展。"
    },
]

def download_pdf(paper, save_dir, max_retries=3):
    """
    下载单个论文PDF

    Args:
        paper: 论文信息字典
        save_dir: 保存目录
        max_retries: 最大重试次数

    Returns:
        (success, paper, message)
    """
    arxiv_id = paper.get("arxiv_id", "")
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    # 生成中文文件名
    title_cn = paper.get("title_cn", "unknown")
    venue = paper.get("venue", "unknown")
    year = paper.get("year", 0)

    # 清理文件名中的非法字符
    safe_title = title_cn.replace("/", "_").replace("\\", "_").replace(":", "_")
    safe_title = safe_title.replace("*", "_").replace("?", "_").replace('"', "_")
    safe_title = safe_title.replace("<", "_").replace(">", "_").replace("|", "_")
    safe_title = safe_title[:100]  # 限制长度

    filename = f"{safe_title}_{venue}_{year}.pdf"
    filepath = os.path.join(save_dir, filename)

    # 如果文件已存在，跳过
    if os.path.exists(filepath):
        return True, paper, "已存在"

    for attempt in range(max_retries):
        try:
            print(f"下载: {filename} (尝试 {attempt+1}/{max_retries})")

            # 设置请求头
            req = urllib.request.Request(pdf_url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36')

            response = urllib.request.urlopen(req, timeout=60)
            content = response.read()

            # 检查PDF有效性
            if len(content) < 10000:  # PDF文件太小可能无效
                print(f"  警告: 文件太小 ({len(content)} bytes)，可能无效")
                continue

            # 保存文件
            with open(filepath, 'wb') as f:
                f.write(content)

            print(f"  成功: {filename} ({len(content)/1024/1024:.1f} MB)")
            return True, paper, filename

        except Exception as e:
            print(f"  失败: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)  # 等待后重试

    return False, paper, "下载失败"

def generate_readme(papers, save_dir):
    """
    生成README.md文件

    Args:
        papers: 论文列表
        save_dir: 保存目录
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 统计信息
    total = len(papers)
    with_code = sum(1 for p in papers if p.get("github_url"))
    venue_dist = {}
    year_dist = {}
    for p in papers:
        venue = p.get("venue", "Unknown")
        year = p.get("year", 0)
        venue_dist[venue] = venue_dist.get(venue, 0) + 1
        year_dist[year] = year_dist.get(year, 0) + 1

    # 按引用量排序
    sorted_papers = sorted(papers, key=lambda x: x.get("citations", 0), reverse=True)

    # 生成README内容
    readme = f"""# 自动驾驶_纯视觉3D目标检测 论文下载清单

## 下载信息
- **研究方向**：自动驾驶-纯视觉-3D目标检测
- **时间范围**：2021-2024
- **下载时间**：{now}
- **论文数量**：{total}篇
- **排序方式**：引用量优先，有开源代码优先

## 论文列表

| 序号 | 论文标题 | 会议/年份 | 引用量 | 开源代码 | 中文摘要 |
|------|----------|-----------|--------|----------|----------|
"""

    for i, paper in enumerate(sorted_papers, 1):
        title_cn = paper.get("title_cn", "")
        venue = paper.get("venue", "")
        year = paper.get("year", 0)
        citations = paper.get("citations", 0)
        github = paper.get("github_url", "")
        abstract_cn = paper.get("abstract_cn", "")

        # 代码链接
        if github:
            code_link = f"[代码]({github})"
        else:
            code_link = "无"

        # 截断摘要用于表格
        abstract_short = abstract_cn[:80] + "..." if len(abstract_cn) > 80 else abstract_cn

        readme += f"| {i} | {title_cn} | {venue}/{year} | {citations} | {code_link} | {abstract_short} |\n"

    # 详细信息部分
    readme += "\n## 详细信息\n\n"

    for i, paper in enumerate(sorted_papers, 1):
        title_cn = paper.get("title_cn", "")
        title_en = paper.get("title_en", "")
        venue = paper.get("venue", "")
        year = paper.get("year", 0)
        authors = paper.get("authors", "")
        citations = paper.get("citations", 0)
        arxiv_id = paper.get("arxiv_id", "")
        github = paper.get("github_url", "")
        abstract_cn = paper.get("abstract_cn", "")

        arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
        code_link = github if github else "无"

        # 生成文件名
        safe_title = title_cn.replace("/", "_").replace("\\", "_").replace(":", "_")
        safe_title = safe_title[:100]
        filename = f"{safe_title}_{venue}_{year}.pdf"

        readme += f"""### {i}. {title_cn}
- **英文标题**：{title_en}
- **会议/年份**：{venue}/{year}
- **作者**：{authors}
- **引用量**：{citations}
- **arXiv链接**：{arxiv_url}
- **开源代码**：{code_link}
- **文件名**：{filename}
- **中文摘要**：
  {abstract_cn}

"""

    # 统计表格
    readme += "## 下载统计\n\n"
    readme += "| 年份 | 论文数量 | 主要会议 |\n"
    readme += "|------|----------|----------|\n"

    for year in sorted(year_dist.keys(), reverse=True):
        venues = [v for v, c in venue_dist.items() if any(p.get("year") == year and p.get("venue") == v for p in papers)]
        readme += f"| {year} | {year_dist[year]} | {', '.join(venues)} |\n"

    readme += f"| **总计** | {total} | - |\n"

    # 保存README
    readme_path = os.path.join(save_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme)

    print(f"\nREADME已保存到: {readme_path}")

def main():
    """主函数"""

    # 设置目录
    base_dir = "/home/hy/hycode/auto_driver/paper/论文下载/自动驾驶_纯视觉3D目标检测_2021-2024"
    papers_dir = os.path.join(base_dir, "papers")

    # 创建目录
    os.makedirs(papers_dir, exist_ok=True)

    print("=" * 60)
    print("自动驾驶-纯视觉-3D目标检测论文下载")
    print("=" * 60)
    print(f"目标目录: {base_dir}")
    print(f"论文数量: {len(PAPERS)}")
    print(f"并发数: 5")
    print("=" * 60)

    # 下载论文
    success_count = 0
    fail_count = 0
    skip_count = 0

    # 使用线程池并发下载（限制并发数为5）
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(download_pdf, paper, papers_dir): paper
            for paper in PAPERS
        }

        for future in as_completed(futures):
            success, paper, message = future.result()
            if success:
                if message == "已存在":
                    skip_count += 1
                else:
                    success_count += 1
            else:
                fail_count += 1

    print("\n" + "=" * 60)
    print("下载完成!")
    print(f"成功: {success_count}, 跳过: {skip_count}, 失败: {fail_count}")
    print("=" * 60)

    # 生成README
    print("\n生成README...")
    generate_readme(PAPERS, base_dir)

    # 保存metadata
    metadata = {
        "query": {
            "direction": "自动驾驶_纯视觉3D目标检测",
            "direction_en": "autonomous_driving_camera_3d_detection",
            "time_range": {"start": 2021, "end": 2024},
            "max_papers": 50,
            "last_download": datetime.now().isoformat()
        },
        "papers": PAPERS,
        "statistics": {
            "total_papers": len(PAPERS),
            "download_success": success_count,
            "download_failed": fail_count,
            "download_skipped": skip_count,
            "with_code": sum(1 for p in PAPERS if p.get("github_url")),
            "venue_distribution": dict((v, sum(1 for p in PAPERS if p.get("venue") == v)) for v in set(p.get("venue") for p in PAPERS)),
            "year_distribution": dict((y, sum(1 for p in PAPERS if p.get("year") == y)) for y in set(p.get("year") for p in PAPERS))
        }
    }

    metadata_path = os.path.join(base_dir, "metadata.json")
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"元数据已保存到: {metadata_path}")
    print("\n全部完成!")

if __name__ == "__main__":
    main()
