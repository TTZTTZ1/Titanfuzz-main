import torch

# Prepare valid input data
x = torch.tensor([1, 2, 3], dtype=torch.float)
y = torch.tensor([4, 5, 6], dtype=torch.float)

# Call the API
result = torch.add(x, y)
print(result)