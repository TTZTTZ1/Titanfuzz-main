import torch

# Prepare valid input data
input_tensors = [torch.randn(3), torch.randn(4)]

# Call the API
params_list = torch.nn.ParameterList(input_tensors)