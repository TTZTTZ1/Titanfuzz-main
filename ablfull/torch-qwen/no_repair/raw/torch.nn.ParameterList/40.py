import torch

# Generate input data
parameters = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])]

# Call the API
param_list = torch.nn.ParameterList(parameters)