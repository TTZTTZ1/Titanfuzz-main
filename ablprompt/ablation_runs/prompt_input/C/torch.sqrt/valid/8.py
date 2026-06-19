import torch

# Create a random tensor with positive and negative values
input_tensor = torch.tensor([-4.0, -1.0, 0.0, 1.0, 4.0], dtype=torch.float32)

# Compute the square root using torch.sqrt
result_tensor = torch.sqrt(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor:", result_tensor)