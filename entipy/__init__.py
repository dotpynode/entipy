# -*- coding: utf-8 -*-
"""
entipy
-------

A python ecs pattern

:copyright: (c) 2026 by dotpynode

"""

# compatibility
from __future__ import absolute_import, division, print_function

# get version
from .__version__ import __version__

# allow lazy loading
from .pattern import component, entity, manager, system
from .components import componentname