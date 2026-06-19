import torch
from torch.utils.data import TensorDataset
data = [torch.randn(3) for _ in range(10)]
dataset = TensorDataset(*data)