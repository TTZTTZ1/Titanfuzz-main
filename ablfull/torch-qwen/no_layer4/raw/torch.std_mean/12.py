import torch

# Prepare valid input data
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0])

# Call the API
result = torch.std_mean(input_data, dim=0)