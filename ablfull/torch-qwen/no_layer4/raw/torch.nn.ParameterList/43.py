import torch

# Generate input data
parameters = [torch.tensor([0.1, 0.2]), torch.tensor([0.3, 0.4])]

# Call the API
param_list = torch.nn.ParameterList(parameters)