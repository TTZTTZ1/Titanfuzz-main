import torch

# Prepare input data
data = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])

# Call the API
result = torch.Tensor.nanmean(data, dim=1, keepdim=True)

print(result)