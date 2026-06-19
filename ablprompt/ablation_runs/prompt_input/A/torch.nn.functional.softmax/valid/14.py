import torch
import torch.nn.functional as F

# Example input tensor
input_tensor = torch.tensor([1.0, 2.0, 3.0])

# Applying softmax function
output_tensor = F.softmax(input_tensor, dim=0)

print(output_tensor)