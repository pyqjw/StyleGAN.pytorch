"""
-------------------------------------------------
   File Name:    config.py
   Author:       Zhonghao Huang
   Date:         2019/10/22
   Description:
-------------------------------------------------
"""

from yacs.config import CfgNode as CN

cfg = CN()

cfg.OUTPUT_DIR = ""
cfg.RESOLUTION = 128

# ---------------------------------------------------------------------------- #
# Options for scheduler
# ---------------------------------------------------------------------------- #
cfg.sched = CN()
cfg.sched.G_lrate_dict = {128: 0.0015, 256: 0.002, 512: 0.003, 1024: 0.003}
cfg.sched.D_lrate_dict = {128: 0.0015, 256: 0.002, 512: 0.003, 1024: 0.003}

# ---------------------------------------------------------------------------- #
# Options for Dataset
# ---------------------------------------------------------------------------- #
cfg.DATASET = CN()
cfg.DATASET.IMG_DIR = ""
cfg.DATASET.FOLDER = True

# ---------------------------------------------------------------------------- #
# Options for Generator
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
# Options for Discriminator
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Options for Generator Optimizer
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Options for Discriminator Optimizer
# ---------------------------------------------------------------------------- #