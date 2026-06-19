import torch

# Task 2: Generate input data
input_data = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])

# Task 3: Call the API torch.Tensor.nanmean
result = torch.nanmean(input_data)

print(result)