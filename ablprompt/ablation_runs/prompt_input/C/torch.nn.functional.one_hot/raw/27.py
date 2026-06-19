import torch
import torch.nn.functional as F

# Example tensor of class indices
class_indices = torch.tensor([0, 2, 3, 1])

# Convert to one-hot encoding
one_hot_encoded = F.one_hot(class_indices)

print(one_hot_encoded)