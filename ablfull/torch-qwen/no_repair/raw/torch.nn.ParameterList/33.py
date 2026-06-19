import torch

# Prepare valid input data
parameters = [torch.randn(3), torch.randn(4)]

# Call the API
param_list = torch.nn.ParameterList(parameters)