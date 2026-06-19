import torch

# Create a random tensor with floating-point numbers
input_tensor = torch.tensor([1.5, 2.3, -0.7, 4.8], dtype=torch.float32)

# Apply torch.floor to the tensor
result_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after applying torch.floor:", result_tensor)