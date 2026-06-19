import torch

# Create a square tensor
tensor = torch.tensor([[1., 2.], [3., 4.]])

# Calculate the determinant of the tensor
determinant = torch.linalg.det(tensor)

print("The determinant of the tensor is:", determinant)