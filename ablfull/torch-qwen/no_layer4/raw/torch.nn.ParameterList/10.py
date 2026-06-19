import torch

# Prepare valid input data
values = [torch.tensor([0.1, 0.2]), torch.tensor([0.3, 0.4])]

# Call the API
result = torch.nn.ParameterList(values)