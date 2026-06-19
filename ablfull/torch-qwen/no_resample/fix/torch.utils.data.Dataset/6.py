import torch
from torch.utils.data import TensorDataset
data = torch.tensor([1, 2, 3, 4, 5])
dataset = TensorDataset(data)