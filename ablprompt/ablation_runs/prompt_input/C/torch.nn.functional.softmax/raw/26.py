import torch
import torch.nn.functional as F

# Create a random tensor
x = torch.randn(3, 4)

# Apply softmax along dimension 1
softmax_output = F.softmax(x, dim=1)

print("Input Tensor:")
print(x)
print("\nSoftmax Output:")
print(softmax_output)