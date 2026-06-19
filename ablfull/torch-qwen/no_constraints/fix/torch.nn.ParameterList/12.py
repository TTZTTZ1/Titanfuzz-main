import torch
values = [torch.randn(3), torch.tensor([1.0, 2.0])]
parameter_list = torch.nn.ParameterList(values)