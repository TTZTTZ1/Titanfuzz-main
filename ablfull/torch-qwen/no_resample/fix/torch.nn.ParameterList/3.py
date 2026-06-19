import torch
values = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])]
result = torch.nn.ParameterList(values)