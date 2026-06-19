import torch
from torch.nn.modules.module import Module

class DummyModule(Module):
    def __call__(self, x):
        return x * 2

functions = [DummyModule(), DummyModule()]
segments = 2
input_data = torch.randn(10)

result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_data)