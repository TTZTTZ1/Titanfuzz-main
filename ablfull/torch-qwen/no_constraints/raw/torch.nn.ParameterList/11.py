import torch

# Generate input data
values = [torch.randn(3), torch.randn(4)]

# Call the API
parameter_list = torch.nn.ParameterList(values)