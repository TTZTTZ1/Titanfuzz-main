import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply softmax along the second dimension
output_tensor = F.softmax(input_tensor, dim=1)

print(output_tensor)