import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply log_softmax along dimension 1
output = F.log_softmax(input_tensor, dim=1)

print(output)