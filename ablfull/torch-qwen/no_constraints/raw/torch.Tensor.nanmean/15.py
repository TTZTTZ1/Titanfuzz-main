import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])

# Task 3: Call the API torch.Tensor.nanmean
result = torch.Tensor.nanmean(input_tensor)

print(result)