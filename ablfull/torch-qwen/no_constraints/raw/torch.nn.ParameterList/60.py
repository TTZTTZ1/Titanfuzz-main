import torch

# Task 2: Generate input data
values = [torch.randn(10), torch.randn(20)]

# Task 3: Call the API
param_list = torch.nn.ParameterList(values)