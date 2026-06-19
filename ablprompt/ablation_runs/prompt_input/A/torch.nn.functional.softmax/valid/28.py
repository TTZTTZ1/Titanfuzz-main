import torch
import torch.nn.functional as F

# Example tensor
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Apply softmax function
softmax_output = F.softmax(x, dim=1)

print(softmax_output)