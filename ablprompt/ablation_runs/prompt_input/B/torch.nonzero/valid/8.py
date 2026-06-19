import torch

# Create a random tensor with some zero values
input_tensor = torch.randint(0, 5, (4, 4)).to(torch.float32)

# Use torch.nonzero to find indices of non-zero elements
indices = torch.nonzero(input_tensor, as_tuple=True)

print("Input Tensor:")
print(input_tensor)
print("Indices of Non-Zero Elements:")
print(indices)