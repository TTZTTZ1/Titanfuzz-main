import torch

# Prepare valid input data
parameters = [torch.randn(3), torch.tensor([1.0, 2.0, 3.0])]

# Call the API
torch.nn.ParameterList(parameters)