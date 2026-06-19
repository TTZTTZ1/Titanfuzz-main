import torch
import torch.nn.functional as F

# Example tensor
input_tensor = torch.tensor([[1.0, 2.0, 3.0]])

# Applying softmax function
softmax_output = F.softmax(input_tensor, dim=1)

print(softmax_output)