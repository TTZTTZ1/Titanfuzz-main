import torch

# Create a 2x2 tensor
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Calculate the determinant of the tensor
determinant = torch.linalg.det(tensor)

print("The determinant of the tensor is:", determinant)