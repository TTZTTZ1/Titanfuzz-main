import torch

# Create a tensor with various elements including positive, negative, and zero
input_tensor = torch.tensor([-5, 0, 3, -2])

# Use torch.sign to get the sign of each element
result_tensor = torch.sign(input_tensor)

print(result_tensor)