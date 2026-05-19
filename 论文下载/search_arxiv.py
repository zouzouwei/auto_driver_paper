#!/usr/bin/env python3
"""
arXiv论文搜索脚本
用于搜索自动驾驶-纯视觉-3D目标检测相关论文
"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time
from datetime import datetime

def search_arxiv(query, max_results=60):
    """
    搜索arXiv论文

    Args:
        query: 搜索查询
        max_results: 最大结果数

    Returns:
        论文列表
    """
    base_url = "http://export.arxiv.org/api/query?"

    # 构建搜索参数
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }

    url = base_url + urllib.parse.urlencode(params)
    print(f"搜索URL: {url}")

    try:
        response = urllib.request.urlopen(url, timeout=30)
        content = response.read().decode('utf-8')
        return parse_arxiv_response(content)
    except Exception as e:
        print(f"搜索失败: {e}")
        return []

def parse_arxiv_response(xml_content):
    """
    解析arXiv API响应

    Args:
        xml_content: XML内容

    Returns:
        论文列表
    """
    papers = []

    # 定义命名空间
    namespaces = {
        'atom': 'http://www.w3.org/2005/Atom',
        'arxiv': 'http://arxiv.org/schemas/atom'
    }

    root = ET.fromstring(xml_content)

    for entry in root.findall('atom:entry', namespaces):
        paper = {}

        # 标题
        title_elem = entry.find('atom:title', namespaces)
        paper['title'] = title_elem.text.strip().replace('\n', ' ') if title_elem is not None else ""

        # 摘要
        summary_elem = entry.find('atom:summary', namespaces)
        paper['abstract'] = summary_elem.text.strip().replace('\n', ' ') if summary_elem is not None else ""

        # 作者
        authors = []
        for author in entry.findall('atom:author', namespaces):
            name_elem = author.find('atom:name', namespaces)
            if name_elem is not None:
                authors.append(name_elem.text.strip())
        paper['authors'] = authors

        # arXiv ID
        id_elem = entry.find('atom:id', namespaces)
        if id_elem is not None:
            arxiv_url = id_elem.text.strip()
            paper['arxiv_id'] = arxiv_url.split('/')[-1]
            paper['arxiv_url'] = arxiv_url
            paper['pdf_url'] = arxiv_url.replace('abs', 'pdf') + '.pdf'

        # 发布日期
        published_elem = entry.find('atom:published', namespaces)
        if published_elem is not None:
            paper['published'] = published_elem.text.strip()
            paper['year'] = int(published_elem.text.strip()[:4])

        # 更新日期
        updated_elem = entry.find('atom:updated', namespaces)
        if updated_elem is not None:
            paper['updated'] = updated_elem.text.strip()

        # 类别
        categories = []
        for category in entry.findall('atom:category', namespaces):
            term = category.get('term', '')
            if term:
                categories.append(term)
        paper['categories'] = categories

        # 主要类别
        primary_category = entry.find('arxiv:primary_category', namespaces)
        if primary_category is not None:
            paper['primary_category'] = primary_category.get('term', '')

        # PDF链接
        for link in entry.findall('atom:link', namespaces):
            if link.get('title') == 'pdf':
                paper['pdf_url'] = link.get('href', '')
                break

        papers.append(paper)

    return papers

def filter_papers(papers, year_start=2022, year_end=2026):
    """
    过滤论文

    Args:
        papers: 论文列表
        year_start: 起始年份
        year_end: 结束年份

    Returns:
        过滤后的论文列表
    """
    filtered = []

    for paper in papers:
        year = paper.get('year', 0)

        # 时间范围过滤
        if year < year_start or year > year_end:
            continue

        # 关键词过滤（确保与3D检测和自动驾驶相关）
        title_lower = paper.get('title', '').lower()
        abstract_lower = paper.get('abstract', '').lower()
        combined = title_lower + ' ' + abstract_lower

        # 必须包含的关键词
        required_keywords = ['3d', 'detection', 'object']
        if not any(kw in combined for kw in required_keywords):
            continue

        # 排除纯LiDAR/点云方法
        exclude_keywords = ['lidar-only', 'point cloud only', 'lidar based']
        if any(kw in combined for kw in exclude_keywords):
            continue

        filtered.append(paper)

    return filtered

def main():
    """主函数"""

    # 搜索查询
    queries = [
        # 查询1: 纯视觉3D检测
        '(all:"3D object detection" OR all:"3D detection") AND (all:"camera" OR all:"monocular" OR all:"multi-view" OR all:"multi-camera" OR all:"vision") AND (all:"autonomous driving" OR all:"self-driving")',
        # 查询2: BEV感知
        '(all:"BEV" OR all:"bird\'s eye view") AND (all:"3D detection" OR all:"object detection") AND all:"autonomous driving"',
        # 查询3: 纯视觉方法
        '(all:"3D object detection" OR all:"3D detection") AND (all:"image-only" OR all:"camera-only" OR all:"pure vision" OR all:"vision-only")',
    ]

    all_papers = []

    # 执行多个查询
    for i, query in enumerate(queries):
        print(f"\n执行查询 {i+1}/{len(queries)}...")
        papers = search_arxiv(query, max_results=50)
        print(f"找到 {len(papers)} 篇论文")
        all_papers.extend(papers)
        time.sleep(3)  # arXiv API限制

    # 去重
    seen_ids = set()
    unique_papers = []
    for paper in all_papers:
        arxiv_id = paper.get('arxiv_id', '')
        if arxiv_id and arxiv_id not in seen_ids:
            seen_ids.add(arxiv_id)
            unique_papers.append(paper)

    print(f"\n去重后共 {len(unique_papers)} 篇论文")

    # 过滤
    filtered_papers = filter_papers(unique_papers, year_start=2022, year_end=2026)
    print(f"过滤后共 {len(filtered_papers)} 篇论文")

    # 保存结果
    output_file = "/home/hy/hycode/auto_driver/paper/论文下载/arxiv_search_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_papers, f, ensure_ascii=False, indent=2)

    print(f"\n搜索结果已保存到: {output_file}")

    # 打印前10篇论文
    print("\n前10篇论文:")
    for i, paper in enumerate(filtered_papers[:10]):
        print(f"{i+1}. {paper.get('title', 'N/A')}")
        print(f"   arXiv ID: {paper.get('arxiv_id', 'N/A')}")
        print(f"   年份: {paper.get('year', 'N/A')}")
        print()

    return filtered_papers

if __name__ == "__main__":
    main()
