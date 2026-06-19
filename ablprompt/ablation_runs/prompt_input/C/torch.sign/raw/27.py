import torch

# Create a sample tensor with mixed values
sample_tensor = torch.tensor([-2.5, 0.0, 3.14, -0.01])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(sample_tensor)

print("Original Tensor:", sample_tensor)
print("Signed Tensor:", signed_tensor)