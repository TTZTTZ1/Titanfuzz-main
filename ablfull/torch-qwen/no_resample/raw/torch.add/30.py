import torch

# Prepare input data
input_tensor = torch.tensor([1, 2, 3], dtype=torch.int)
other_tensor = torch.tensor([4, 5, 6], dtype=torch.int)

# Call the API
result = torch.add(input_tensor, other_tensor)

print(result)