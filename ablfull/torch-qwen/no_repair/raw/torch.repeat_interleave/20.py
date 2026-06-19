import torch

# Prepare input data
input_tensor = torch.tensor([[1, 2], [3, 4]])
repeats = torch.tensor([2])
dim = 0

# Call the API
result = torch.repeat_interleave(input_tensor, repeats, dim=dim)
print(result)