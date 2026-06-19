import torch
parameters = [torch.tensor([0.1, 0.2]), torch.tensor([0.3, 0.4])]
param_list = torch.nn.ParameterList(parameters)