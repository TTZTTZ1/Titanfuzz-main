import torch

# Create a tensor with values outside the desired range
input_tensor = torch.tensor([-10, 0, 5, 10, 15], dtype=torch.float)

# Define the minimum and maximum values for clamping
min_value = 0
max_value = 10

# Apply clamp operation
clamped_tensor = torch.clamp(input_tensor, min=min_value, max=max_value)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)