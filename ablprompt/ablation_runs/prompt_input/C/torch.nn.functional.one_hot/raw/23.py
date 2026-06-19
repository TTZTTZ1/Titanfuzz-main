import torch
import torch.nn.functional as F

# Example tensor of class indices
indices = torch.tensor([2, 1, 3])

# Convert to one-hot encoding with inferred number of classes
one_hot_encoded = F.one_hot(indices)

print(one_hot_encoded)