import torch
from torch.nn import Linear
model = torch.nn.Sequential(Linear(10, 5), Linear(5, 3))
input_data = torch.randn(1, 10)
output = torch.utils.checkpoint.checkpoint_sequential(model, 1, input_data)