import torch

# Prepare valid input data
input_tensor = torch.tensor([[1, 2], [3, 4]])
repeats_tensor = torch.tensor([2])
dim_value = 0

# Call the API
result = torch.repeat_interleave(input_tensor, repeats=repeats_tensor, dim=dim_value)
print(result)