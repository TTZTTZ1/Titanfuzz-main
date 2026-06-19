import torch

# Generate input data
input_tensor = torch.tensor([1, 2, 3])
repeats = 2

# Call the API
result = torch.repeat_interleave(input_tensor, repeats)
print(result)