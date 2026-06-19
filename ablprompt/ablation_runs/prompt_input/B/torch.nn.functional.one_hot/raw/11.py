import torch
from torch.nn.functional import one_hot

# Create a random tensor of class indices
indices = torch.randint(0, 5, (3, 4))

# Convert the indices to one-hot encoding
one_hot_encoded = one_hot(indices, num_classes=5)

print(one_hot_encoded)