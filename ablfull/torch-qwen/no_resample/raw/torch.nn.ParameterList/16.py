import torch

# Prepare valid input data
values = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])]

# Call the API
params = torch.nn.ParameterList(values)