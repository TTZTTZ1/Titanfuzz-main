import torch

# Prepare valid input data
values = [torch.tensor([1.0]), torch.tensor([2.0])]

# Call the API
result = torch.nn.ParameterList(values)