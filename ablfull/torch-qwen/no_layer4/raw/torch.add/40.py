import torch

# Prepare input data
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])

# Call the API
result = torch.add(x, y)
print(result)