import torch
import torch.nn.functional as F

# Example tensor with integer class indices
input_tensor = torch.tensor([0, 2, 3, 1])

# Convert to one-hot encoding
one_hot_encoded = F.one_hot(input_tensor)

print(one_hot_encoded)