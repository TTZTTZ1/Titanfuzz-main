import torch

# Generate input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])

# Call the API
result = torch.Tensor.nanmean(input_tensor)

print(result)