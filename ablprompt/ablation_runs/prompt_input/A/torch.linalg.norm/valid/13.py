import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0])

# Calculate the L2 norm of the tensor
norm = torch.linalg.norm(tensor)

print(f"The L2 norm of the tensor is: {norm}")