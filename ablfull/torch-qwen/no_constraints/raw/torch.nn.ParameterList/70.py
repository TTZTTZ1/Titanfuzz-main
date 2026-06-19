import torch

# Task 2: Prepare valid input data
input_data = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])]

# Task 3: Call the API
param_list = torch.nn.ParameterList(input_data)