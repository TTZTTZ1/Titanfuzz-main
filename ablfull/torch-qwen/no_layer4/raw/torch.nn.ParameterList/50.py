import torch

parameters = [torch.randn(3), torch.randn(4)]
torch.nn.ParameterList(parameters)