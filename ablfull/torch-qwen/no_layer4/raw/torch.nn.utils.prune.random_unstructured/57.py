import torch
import torch.nn as nn
from torch.nn.utils.prune import random_unstructured

class MyModule(nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

model = MyModule()
random_unstructured(model.conv.weight, name="weight", amount=0.5)