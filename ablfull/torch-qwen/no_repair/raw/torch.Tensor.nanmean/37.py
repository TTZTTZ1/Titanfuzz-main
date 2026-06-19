import torch

# Prepare input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, float('nan')]], dtype=torch.float32)

# Call the API
result = torch.Tensor.nanmean(input_tensor, dim=1, keepdim=True, dtype=None)
print(result)