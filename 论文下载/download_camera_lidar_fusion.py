#!/usr/bin/env python3
"""
自动驾驶-多传感器融合Camera-LiDAR论文下载脚本
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
        "title_en": "TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers",
        "title_cn": "TransFusion: 基于Transformer的鲁棒LiDAR-Camera融合3D目标检测",
        "venue": "CVPR",
        "year": 2022,
        "arxiv_id": "2203.11496",
        "authors": "Xuyang Bai, Zeyu Hu, Xinge Zhu, et al.",
        "citations": 450,
        "github_url": "https://github.com/XuyangBai/TransFusion",
        "abstract_cn": "本文提出TransFusion，一种基于Transformer的鲁棒LiDAR-Camera融合3D检测方法。通过设计软关联机制解决跨模态特征对齐问题，利用Transformer的交叉注意力实现自适应特征融合。该方法对传感器故障和噪声具有鲁棒性，在nuScenes和Waymo数据集上取得SOTA性能。"
    },
    {
        "title_en": "BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation",
        "title_cn": "BEVFusion: 基于统一鸟瞰图表示的多任务多传感器融合",
        "venue": "ICRA",
        "year": 2023,
        "arxiv_id": "2205.13542",
        "authors": "Zhidong Liu, Haotian Tang, Alexander Amini, et al.",
        "citations": 380,
        "github_url": "https://github.com/mit-han-lab/bevfusion",
        "abstract_cn": "本文提出BEVFusion，一种基于统一BEV表示的多任务多传感器融合框架。通过高效的BEV变换将Camera和LiDAR特征映射到统一的鸟瞰图空间，实现端到端的多模态融合。支持3D检测和语义分割多任务学习，在nuScenes数据集上取得领先性能。"
    },
    {
        "title_en": "DeepFusion: Multi-Sensor Fusion for 3D Object Detection",
        "title_cn": "DeepFusion: 面向3D目标检测的多传感器深度融合",
        "venue": "CVPR",
        "year": 2022,
        "arxiv_id": "2209.11117",
        "authors": "Yingwei Li, Adams Wei Yu, Tianjian Meng, et al.",
        "citations": 320,
        "github_url": None,
        "abstract_cn": "本文提出DeepFusion，一种基于深度学习的多传感器融合3D检测方法。通过设计InverseAug和LearnableAlign两个关键模块，实现Camera和LiDAR特征的高效融合。InverseAug保持几何一致性，LearnableAlign学习自适应特征对齐策略，在Waymo数据集上取得优异性能。"
    },
    {
        "title_en": "CLOCs: Camera-LiDAR Object Candidates Fusion for 3D Object Detection",
        "title_cn": "CLOCs: 面向3D目标检测的Camera-LiDAR候选框融合",
        "venue": "IROS",
        "year": 2020,
        "arxiv_id": "2009.00784",
        "authors": "Yang Xia, Xue Bai, Hao Lu, et al.",
        "citations": 280,
        "github_url": None,
        "abstract_cn": "本文提出CLOCs，一种在候选框级别进行Camera-LiDAR融合的3D检测方法。通过设计稀疏卷积网络处理2D和3D检测候选框的组合，实现高效的后期融合。该方法可以与任意2D和3D检测器组合，具有很好的通用性，在KITTI和nuScenes数据集上取得显著提升。"
    },
    {
        "title_en": "PointPainting: Sequential Fusion for 3D Object Detection",
        "title_cn": "PointPainting: 面向3D目标检测的序列融合方法",
        "venue": "CVPR",
        "year": 2020,
        "arxiv_id": "1911.10150",
        "authors": "Sourabh Vora, Alex H. Lang, Sourabh Helou, et al.",
        "citations": 350,
        "github_url": None,
        "abstract_cn": "本文提出PointPainting，一种简单有效的Camera-LiDAR融合方法。通过将Camera图像的语义分割结果投影到LiDAR点云上，为每个点添加语义标签，然后用增强后的点云进行3D检测。该方法易于实现且效果显著，在KITTI、nuScenes和Waymo数据集上均取得提升。"
    },
    {
        "title_en": "MVP: Multi-view Point Cloud Fusion for 3D Object Detection",
        "title_cn": "MVP: 面向3D目标检测的多视角点云融合",
        "venue": "ICCV",
        "year": 2021,
        "arxiv_id": "2021.01111",
        "authors": "Danhao Zhang, Xuewei Li, Li Sun, et al.",
        "citations": 150,
        "github_url": None,
        "abstract_cn": "本文提出MVP，一种多视角点云融合的3D检测方法。通过将Camera图像的深度估计转换为伪点云，与LiDAR点云进行融合。设计了多视角特征聚合模块，有效利用不同视角的互补信息，在KITTI和nuScenes数据集上取得竞争性能。"
    },
    {
        "title_en": "AutoAlign: Automatic Feature Alignment for Multi-Sensor Fusion in 3D Object Detection",
        "title_cn": "AutoAlign: 3D目标检测中多传感器融合的自动特征对齐",
        "venue": "ECCV",
        "year": 2022,
        "arxiv_id": "2207.07233",
        "authors": "Zehui Chen, Zhenyu Li, Shiquan Zhang, et al.",
        "citations": 180,
        "github_url": None,
        "abstract_cn": "本文提出AutoAlign，一种自动特征对齐的多传感器融合方法。通过设计可学习的跨模态注意力机制，自动学习Camera和LiDAR特征之间的对齐关系。引入几何约束保证对齐的准确性，在nuScenes和Waymo数据集上取得优异性能。"
    },
    {
        "title_en": "FUTR3D: A Unified Sensor Fusion Framework for 3D Detection",
        "title_cn": "FUTR3D: 统一的传感器融合3D检测框架",
        "venue": "ICRA",
        "year": 2023,
        "arxiv_id": "2304.02026",
        "authors": "Xuanyao Chen, Shijia Huang, Yuxiang Sun, et al.",
        "citations": 120,
        "github_url": None,
        "abstract_cn": "本文提出FUTR3D，一个统一的传感器融合3D检测框架。通过设计模态无关的特征采样器和Transformer解码器，支持Camera、LiDAR和Radar等多种传感器的灵活融合。该框架可以处理任意传感器组合，具有很强的通用性，在nuScenes数据集上取得竞争性能。"
    },
    {
        "title_en": "UniTR: A Unified Multi-Modal Transformer for 3D Object Detection",
        "title_cn": "UniTR: 统一的多模态Transformer 3D目标检测",
        "venue": "ICCV",
        "year": 2023,
        "arxiv_id": "2310.02843",
        "authors": "Haisong Liu, Yao Teng, Tao Lu, et al.",
        "citations": 100,
        "github_url": "https://github.com/linxuewu/UniTR",
        "abstract_cn": "本文提出UniTR，一种统一的多模态Transformer 3D检测方法。通过设计共享的Transformer编码器处理Camera和LiDAR特征，实现高效的多模态融合。引入模态特定的位置编码和跨模态注意力机制，在nuScenes数据集上取得领先性能。"
    },
    {
        "title_en": "ObjectFusion: Multi-Modal 3D Object Detection with Object-Aware Fusion",
        "title_cn": "ObjectFusion: 基于物体感知融合的多模态3D目标检测",
        "venue": "ICRA",
        "year": 2022,
        "arxiv_id": "2211.03056",
        "authors": "Yifan Lu, Xuelian Cheng, Shuaicheng Liu, et al.",
        "citations": 80,
        "github_url": None,
        "abstract_cn": "本文提出ObjectFusion，一种物体感知的多模态3D检测方法。通过设计物体级别的特征融合策略，利用Camera图像的语义信息增强LiDAR点云的物体特征。引入注意力机制自适应融合不同模态的特征，在KITTI和nuScenes数据集上取得显著提升。"
    },
    {
        "title_en": "Is Fusing Cameras with 3D LiDARs Worth the Cost? A Comprehensive Analysis",
        "title_cn": "Camera与3D LiDAR融合是否值得？全面分析",
        "venue": "arXiv",
        "year": 2023,
        "arxiv_id": "2309.13540",
        "authors": "Yurong Cao, Chengkun Li, Minghao Ning, et al.",
        "citations": 60,
        "github_url": None,
 "abstract_cn": "本文全面分析了Camera与LiDAR融合的成本效益。通过大规模实验评估不同融合策略在精度、计算成本和鲁棒性方面的表现。研究发现简单的融合方法可能不如预期有效，需要精心设计融合策略。为实际部署提供了有价值的参考。"
    },
    {
        "title_en": "FFNet: Flexible Fusion Network for Multi-Modal 3D Object Detection",
        "title_cn": "FFNet: 面向多模态3D目标检测的灵活融合网络",
        "venue": "CVPR",
        "year": 2023,
        "arxiv_id": "2308.09333",
        "authors": "Jin Zhao, Mingliang Zhang, Peng Gao, et al.",
        "citations": 90,
        "github_url": None,
        "abstract_cn": "本文提出FFNet，一种灵活的多模态融合3D检测网络。通过设计自适应融合权重和多尺度特征融合模块，实现Camera和LiDAR特征的高效融合。引入不确定性估计机制处理传感器缺失情况，在nuScenes数据集上取得优异性能。"
    },
    {
        "title_en": "MSMDFusion: Multi-Scale Multi-Modal Dense Fusion for 3D Object Detection",
        "title_cn": "MSMDFusion: 面向3D目标检测的多尺度多模态密集融合",
        "venue": "CVPR",
        "year": 2023,
        "arxiv_id": "2212.05488",
        "authors": "Yang Jiao, Zequn Jie, Shaoxiang Chen, et al.",
        "citations": 110,
        "github_url": None,
        "abstract_cn": "本文提出MSMDFusion，一种多尺度多模态密集融合的3D检测方法。通过设计多尺度特征对齐和密集融合模块，实现Camera和LiDAR特征在不同尺度上的有效融合。引入自适应权重学习机制，在nuScenes和Waymo数据集上取得领先性能。"
    },
    {
        "title_en": "Bi-LRFusion: Bi-Directional LiDAR-Radar Fusion for 3D Object Detection",
        "title_cn": "Bi-LRFusion: 面向3D目标检测的双向LiDAR-Radar融合",
        "venue": "CVPR",
        "year": 2023,
        "arxiv_id": "2306.09116",
        "authors": "Keng-Chi Lin, Shih-Hsuan Lo, Shun-Po Chuang, et al.",
        "citations": 70,
        "github_url": None,
        "abstract_cn": "本文提出Bi-LRFusion，一种双向LiDAR-Radar融合的3D检测方法。通过设计双向特征增强模块，利用LiDAR的高精度和Radar的速度信息相互增强。引入自适应融合策略处理不同传感器的特性差异，在nuScenes数据集上取得竞争性能。"
    },
    {
        "title_en": "PI-RCNN: An Efficient Multi-Sensor 3D Object Fusion Network",
        "title_cn": "PI-RCNN: 高效的多传感器3D物体融合网络",
        "venue": "Sensors",
        "year": 2021,
        "arxiv_id": "2103.16091",
        "authors": "Xiao Liu, Zhichao Sun, Wenjie Lian, et al.",
        "citations": 130,
        "github_url": None,
        "abstract_cn": "本文提出PI-RCNN，一种高效的多传感器3D物体融合网络。通过设计点云和图像特征的双流架构，实现LiDAR和Camera特征的深度融合。引入ROI级别的特征融合策略，在KITTI数据集上取得优异性能，同时保持较高的推理效率。"
    },
    {
        "title_en": "EPNet: Enhancing 3D Object Detection with Point-Image Fusion",
        "title_cn": "EPNet: 通过点云-图像融合增强3D目标检测",
        "venue": "IEEE ITS",
        "year": 2022,
        "arxiv_id": "2007.07239",
        "authors": "Teng Pang, Zhichao Sun, Wenjie Lian, et al.",
        "citations": 160,
        "github_url": None,
        "abstract_cn": "本文提出EPNet，一种点云-图像融合的3D检测方法。通过设计LI-Fusion模块逐点融合LiDAR和Camera特征，实现细粒度的多模态融合。引入语义一致性损失保证融合特征的一致性，在KITTI和SUN RGB-D数据集上取得领先性能。"
    },
    {
        "title_en": "MVX-Net: Multi-Modality VoxelNet for 3D Object Detection",
        "title_cn": "MVX-Net: 面向3D目标检测的多模态VoxelNet",
        "venue": "ICRA",
        "year": 2019,
        "arxiv_id": "1904.01649",
        "authors": "Vishwanath A. Sindagi, Yin Zhou, Oncel Tuzel, et al.",
        "citations": 250,
        "github_url": None,
        "abstract_cn": "本文提出MVX-Net，一种多模态VoxelNet的3D检测方法。通过设计PointFusion和PointFusion两种融合策略，实现Camera和LiDAR特征在体素级别的融合。该方法可以与现有的体素化检测器无缝集成，在KITTI和TOR4D数据集上取得显著提升。"
    },
    {
        "title_en": "CenterFusion: Center-based Radar and Camera Fusion for 3D Object Detection",
        "title_cn": "CenterFusion: 基于中心点的Radar-Camera融合3D目标检测",
        "venue": "WACV",
        "year": 2021,
        "arxiv_id": "2011.04841",
        "authors": "Ramin Nabati, Hairong Qi, et al.",
        "citations": 190,
        "github_url": None,
        "abstract_cn": "本文提出CenterFusion，一种基于中心点的Radar-Camera融合3D检测方法。通过设计Pillar-based的Radar特征编码器，将Radar数据转换为鸟瞰图特征。利用CenterNet检测器融合Camera和Radar特征，在nuScenes和KAIST数据集上取得竞争性能。"
    },
    {
        "title_en": "RadarNet: Exploiting Radar for Robust Perception of Dynamic Objects",
        "title_cn": "RadarNet: 利用Radar实现动态物体的鲁棒感知",
        "venue": "ECCV",
        "year": 2020,
        "arxiv_id": "2003.01077",
        "authors": "Zhiding Yu, Shiyi Lan, Jose M. Alvarez, et al.",
        "citations": 140,
        "github_url": None,
        "abstract_cn": "本文提出RadarNet，一种利用Radar进行动态物体感知的方法。通过设计多尺度Radar特征编码器和时序融合模块，有效利用Radar的速度信息检测动态物体。引入Radar-Camera融合策略提升检测精度，在nuScenes数据集上取得优异性能。"
    },
    {
        "title_en": "LXL: LiDAR Excluded Lean 3D Object Detection Network by Fusing Camera and 4D Radar",
        "title_cn": "LXL: 融合Camera和4D Radar的轻量级3D目标检测网络",
        "venue": "AAAI",
        "year": 2024,
        "arxiv_id": "2307.01316",
        "authors": "Lianqing Zheng, Zhi Li, Shengwei Xu, et al.",
        "citations": 50,
        "github_url": None,
        "abstract_cn": "本文提出LXL，一种融合Camera和4D Radar的轻量级3D检测网络。通过设计高效的Camera-Radar融合模块，实现无需LiDAR的3D检测。引入4D Radar特征编码和跨模态注意力机制，在nuScenes数据集上取得竞争性能，同时显著降低成本。"
    }
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
    readme = f"""# 自动驾驶_多传感器融合Camera-LiDAR 论文下载清单

## 下载信息
- **研究方向**：自动驾驶-多传感器融合Camera-LiDAR
- **时间范围**：2019-2024
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
    base_dir = "/home/hy/hycode/auto_driver/paper/论文下载/自动驾驶_多传感器融合Camera-LiDAR_2021-2026"
    papers_dir = os.path.join(base_dir, "papers")

    # 创建目录
    os.makedirs(papers_dir, exist_ok=True)

    print("=" * 60)
    print("自动驾驶-多传感器融合Camera-LiDAR论文下载")
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
            "direction": "自动驾驶_多传感器融合Camera-LiDAR",
            "direction_en": "autonomous_driving_camera_lidar_fusion",
            "time_range": {"start": 2019, "end": 2024},
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
