import torch

# Prepare valid input data
values = [torch.tensor(0.5), torch.tensor(1.0)]

# Call the API
param_list = torch.nn.ParameterList(values)