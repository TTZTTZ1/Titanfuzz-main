import torch

# Prepare valid input data
values = [torch.randn(5), torch.randn(3)]

# Call the API
result = torch.nn.ParameterList(values)