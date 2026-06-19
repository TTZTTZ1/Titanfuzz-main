import torch

# Generate input data
values = [torch.tensor([1.0]), torch.tensor([2.0])]

# Call the API
params = torch.nn.ParameterList(values)