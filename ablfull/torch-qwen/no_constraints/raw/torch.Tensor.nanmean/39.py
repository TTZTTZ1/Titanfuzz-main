import torch

# Prepare valid input data
data = torch.tensor([[1.0, 2.0], [float('nan'), 4.0]])

# Call the API
result = torch.Tensor.nanmean(data)

print(result)