import torch

# Create a tensor
tensor = torch.tensor([3.0, 4.0])

# Calculate the L2 norm of the tensor
norm_value = torch.linalg.norm(tensor)

print("The L2 norm of the tensor is:", norm_value)