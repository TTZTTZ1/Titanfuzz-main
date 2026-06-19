import torch

# Prepare valid input data
values = [torch.randn(3), torch.randn(4)]

# Call the API
params = torch.nn.ParameterList(values)