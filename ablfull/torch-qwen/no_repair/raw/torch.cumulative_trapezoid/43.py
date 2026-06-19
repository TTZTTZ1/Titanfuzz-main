import torch

# Generate valid input data
y = torch.tensor([1.0, 2.0, 4.0, 7.5])
x = torch.tensor([1.0, 2.0, 4.0, 8.0])

# Call the API
result = torch.cumulative_trapezoid(y, x=x)

print(result)