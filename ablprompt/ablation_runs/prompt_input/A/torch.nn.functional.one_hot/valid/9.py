import torch
import torch.nn.functional as F

# Example tensor
tensor = torch.tensor([1, 2, 3])

# Using one_hot function
one_hot_tensor = F.one_hot(tensor, num_classes=4)

print(one_hot_tensor)