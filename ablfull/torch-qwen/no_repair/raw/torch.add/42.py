import torch

# Prepare input data
a = torch.tensor([1, 2, 3], dtype=torch.float)
b = torch.tensor([4, 5, 6], dtype=torch.float)

# Call the API
result = torch.add(a, b)
print(result)