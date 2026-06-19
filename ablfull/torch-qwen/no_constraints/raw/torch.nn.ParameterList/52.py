import torch

# Task 2: Generate input data
values = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])]

# Task 3: Call the API
parameter_list = torch.nn.ParameterList(values)