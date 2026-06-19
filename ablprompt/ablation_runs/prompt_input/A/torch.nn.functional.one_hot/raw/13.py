import torch
import torch.nn.functional as F

# Example tensor
x = torch.tensor([1, 2, 3])

# Using one_hot function from torch.nn.functional
one_hot_x = F.one_hot(x, num_classes=4)

print(one_hot_x)