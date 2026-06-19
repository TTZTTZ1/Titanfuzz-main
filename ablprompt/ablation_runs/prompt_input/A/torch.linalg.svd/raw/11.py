import torch

# Create a sample tensor
tensor = torch.tensor([[1., 2.], [3., 4.]])

# Call the SVD function
U, s, Vh = torch.linalg.svd(tensor)

print("U:", U)
print("s:", s)
print("Vh:", Vh)