import torch

# Prepare input data
data = torch.tensor([[1.0, 2.0], [torch.nan, 4.0]])

# Call the API
result = torch.Tensor.nanmean(data, dim=0)

print(result)