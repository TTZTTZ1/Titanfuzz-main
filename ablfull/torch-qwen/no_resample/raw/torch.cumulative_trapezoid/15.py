import torch

# Prepare valid input data
y = torch.tensor([1.0, 2.0, 4.0, 7.0])
x = torch.tensor([0.0, 1.0, 2.0, 3.0])

# Call the API
result = torch.cumulative_trapezoid(y, x=x, dx=1.0, dim=-1)
print(result)