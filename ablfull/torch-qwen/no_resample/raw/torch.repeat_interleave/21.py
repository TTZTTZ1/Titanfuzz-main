import torch

# Prepare valid input data
input_tensor = torch.tensor([[1, 2], [3, 4]])
repeats = torch.tensor([2, 3])

# Call the API
result = torch.repeat_interleave(input_tensor, repeats, dim=0)
print(result)