import torch
from torch.utils.data import TensorDataset
data = [torch.randn(3) for _ in range(10)]
tensor_data = torch.stack(data)
dataset = TensorDataset(tensor_data)