import torch
import torch.nn.functional as F

# Example tensor
x = torch.tensor([1.0, 2.0, 3.0])

# Applying softmax function
softmax_output = F.softmax(x, dim=0)

print(softmax_output)