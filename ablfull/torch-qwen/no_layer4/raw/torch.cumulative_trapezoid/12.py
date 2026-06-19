import torch

# Prepare valid input data
y = torch.tensor([1, 4, 9, 16])
x = torch.tensor([0, 1, 2, 3])

# Call the API
result = torch.cumulative_trapezoid(y=y, x=x)
print(result)