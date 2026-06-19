import torch

# Task 2: Generate input data
data = torch.tensor([[1.0, 2.0], [torch.nan, 4.0]])

# Task 3: Call the API torch.Tensor.nanmean
result = torch.nanmean(data)
print(result)