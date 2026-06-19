import torch
import torch.nn.functional as F

# Example tensor of class indices
indices = torch.tensor([0, 2, 1, 3])

# Convert to one-hot encoding
one_hot_encoded = F.one_hot(indices, num_classes=4)

print(one_hot_encoded)