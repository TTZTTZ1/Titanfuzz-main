import torch
parameters = [torch.randn(3), torch.tensor([1.0, 2.0, 3.0])]
torch.nn.ParameterList(parameters)