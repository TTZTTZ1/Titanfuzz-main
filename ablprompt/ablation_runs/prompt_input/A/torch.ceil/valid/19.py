import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([-1.2, 3.5, -4.8, 2.0])

# Apply the ceil function to the tensor
result = torch.ceil(tensor)

print(result)