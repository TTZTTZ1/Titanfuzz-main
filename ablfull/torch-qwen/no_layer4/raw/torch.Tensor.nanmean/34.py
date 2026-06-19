import torch

# Prepare valid input data
input_data = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])

# Call the API
result = torch.Tensor.nanmean(input_data, dim=1)

print(result)