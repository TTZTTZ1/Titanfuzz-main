import torch
values = [torch.tensor([0.1, 0.2]), torch.tensor([0.3, 0.4])]
result = torch.nn.ParameterList(values)