import torch

values = [torch.randn(3), torch.randn(4)]
parameter_list = torch.nn.ParameterList(values)