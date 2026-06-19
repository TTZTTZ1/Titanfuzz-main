import torch

# Task 2: Generate input data
data = torch.tensor([1.0, 2.0, float('nan'), 4.0])

# Task 3: Call the API
result = torch.Tensor.nanmean(data)

print(result)