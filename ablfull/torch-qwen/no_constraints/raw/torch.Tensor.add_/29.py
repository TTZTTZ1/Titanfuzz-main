import torch

# Generate input data
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# Call the API
result = a.add_(b)
print(result)