import torch
import torch.nn.functional as F

# Example tensor with integer class indices
input_tensor = torch.tensor([1, 2, 3, 4])

# Convert to one-hot encoding with inferred number of classes
one_hot_encoded = F.one_hot(input_tensor)

print(one_hot_encoded)