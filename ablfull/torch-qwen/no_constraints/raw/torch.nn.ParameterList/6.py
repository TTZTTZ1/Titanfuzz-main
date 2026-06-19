import torch

# Task 2: Generate input data
values = [torch.randn(3), torch.randn(4)]

# Task 3: Call the API
parameter_list = torch.nn.ParameterList(values)