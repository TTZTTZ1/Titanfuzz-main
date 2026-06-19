import torch

# Generate input data
parameters = [torch.randn(3), torch.randn(4)]

# Call the API
result = torch.nn.ParameterList(parameters)