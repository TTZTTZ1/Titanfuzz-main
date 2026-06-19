import torch
from torch.utils.data import TensorDataset
data = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])]
dataset = TensorDataset(*data)