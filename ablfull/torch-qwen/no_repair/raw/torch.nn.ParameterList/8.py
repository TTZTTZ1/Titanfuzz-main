import torch

# Prepare valid input data
values = [torch.randn(3), torch.randn(4)]

# Call the API
param_list = torch.nn.ParameterList(values)