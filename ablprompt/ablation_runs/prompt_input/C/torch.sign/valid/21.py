import torch

# Create a sample tensor with mixed data types
sample_tensor = torch.tensor([-2, 0, 3, -4.5, 6])

# Use torch.sign to get the sign of each element
signed_tensor = torch.sign(sample_tensor)

print("Original Tensor:", sample_tensor)
print("Signed Tensor:", signed_tensor)