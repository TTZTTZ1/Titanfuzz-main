import torch

# Generate input data
values = [torch.randn(10), torch.randn(20)]

# Call the API
parameter_list = torch.nn.ParameterList(values)