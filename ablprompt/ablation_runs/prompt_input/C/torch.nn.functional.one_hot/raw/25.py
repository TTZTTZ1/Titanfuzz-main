import torch
import torch.nn.functional as F

# Example tensor of class indices
class_indices = torch.tensor([0, 2, 1])

# Convert to one-hot encoding
one_hot_encoded = F.one_hot(class_indices, num_classes=3)

print(one_hot_encoded)