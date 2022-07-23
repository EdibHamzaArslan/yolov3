
import numpy as np



import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable



def parse_cfg(cfgfile):
    """
    Takes a configuration file
    :param cfgfile: path of cfg file
    :return: list of blocks. Dictionary in the list.
    """

    file = open(cfgfile, 'r')
    lines = file.read().split('\n')
    lines = [x for x in lines if len(x) > 0]
    lines = [x for x in lines if x[0] != '#']
    lines = [x.rstrip().lstrip() for x in lines]

    block = {}
    blocks = []

    for line in lines:
        if line[0] == "[":
            if len(block) != 0:
                blocks.append(block)
                block = {}
            block["type"] = line[1:-1].rstrip()
        else:
            key, value = line.split("=")
            block[key.rstrip()] = value.lstrip()
    blocks.append(block)
    return blocks

print(parse_cfg("cfg/yolov3.cfg"))