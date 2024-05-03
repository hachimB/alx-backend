#!/usr/bin/env python3
"""Module documentation"""
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """index_range"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
