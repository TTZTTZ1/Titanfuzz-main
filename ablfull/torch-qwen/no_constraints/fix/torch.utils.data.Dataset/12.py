import torch
from torch.utils.data import TensorDataset
data = [torch.randn(10) for _ in range(5)]
dataset = TensorDataset(*data)