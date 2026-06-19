import torch

# Create a tensor
tensor = torch.tensor([3.0, 4.0])

# Calculate the Euclidean norm of the tensor
norm = torch.linalg.norm(tensor)

print(f"The Euclidean norm of the tensor is: {norm}")