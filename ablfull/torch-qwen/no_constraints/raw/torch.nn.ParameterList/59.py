import torch

# Task 2: Generate input data
input_data = [torch.randn(3), torch.randn(3)]

# Task 3: Call the API
parameter_list = torch.nn.ParameterList(input_data)