import torch

# Prepare input data
tensor = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([4.0, 5.0, 6.0])

# Call the API
result = tensor.add_(other)
print(result)