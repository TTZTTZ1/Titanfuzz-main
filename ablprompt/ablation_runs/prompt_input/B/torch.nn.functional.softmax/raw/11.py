import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply softmax along dimension 1
softmax_output = F.softmax(input_tensor, dim=1)

print("Input Tensor:")
print(input_tensor)
print("\nSoftmax Output:")
print(softmax_output)