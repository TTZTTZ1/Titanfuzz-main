import torch

# Prepare valid input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])

# Call the API with specified parameters
result = torch.Tensor.nanmean(input_tensor, dim=1, keepdim=True)
print(result)