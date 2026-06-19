import torch

# Prepare valid input data
input_tensor = torch.tensor([[1, 2], [3, 4]])
repeats = 2
dim = 1

# Call the API
result = torch.repeat_interleave(input_tensor, repeats, dim)