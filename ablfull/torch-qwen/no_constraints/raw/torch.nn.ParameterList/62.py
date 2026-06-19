import torch

# Task 2: Generate input data
values = [torch.randn(3), torch.tensor([1.0, 2.0])]

# Task 3: Call the API
parameter_list = torch.nn.ParameterList(values)