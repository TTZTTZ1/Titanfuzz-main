import torch

# Prepare valid input data
input_data = [torch.randn(3), torch.randn(4)]

# Call the target API
params_list = torch.nn.ParameterList(input_data)