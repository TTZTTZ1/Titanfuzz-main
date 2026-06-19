import torch

# Task 2: Generate input data
values = [torch.randn(5), torch.randn(10)]

# Task 3: Call the API
parameter_list = torch.nn.ParameterList(values)