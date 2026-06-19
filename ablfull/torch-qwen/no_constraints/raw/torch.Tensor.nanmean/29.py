import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1.0, 2.0, float('nan'), 4.0])

# Task 3: Call the API
result = torch.Tensor.nanmean(input_tensor)

print(result)