import torch
import torch.nn.functional as F

# Example tensor with class indices
class_indices = torch.tensor([0, 1, 3, 2])

# Convert to one-hot encoding with automatically inferred number of classes
one_hot_encoded = F.one_hot(class_indices)

print(one_hot_encoded)