import torch

# Prepare input data
input_tensor = torch.tensor([[1, 2], [3, 4]])
repeats_tensor = torch.tensor([2, 1])

# Call the API
result = torch.repeat_interleave(input=input_tensor, repeats=repeats_tensor, dim=0)
print(result)