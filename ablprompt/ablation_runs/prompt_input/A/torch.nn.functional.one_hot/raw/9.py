import torch
import torch.nn.functional as F

# Example tensor
tensor = torch.tensor([1, 2, 3])

# Using one_hot function from torch.nn.functional
one_hot_tensor = F.one_hot(tensor)

print(one_hot_tensor)