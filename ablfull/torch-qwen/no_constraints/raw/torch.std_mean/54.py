import torch

# Prepare valid input data
data = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# Call the API torch.std_mean
std, mean = torch.std_mean(data)