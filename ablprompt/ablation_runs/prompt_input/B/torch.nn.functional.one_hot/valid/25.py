import torch
from torch.nn.functional import one_hot

# Create a random LongTensor of class indices
indices = torch.randint(0, 5, (3, 4))

# Convert the class indices to a one-hot encoded tensor
one_hot_tensor = one_hot(indices, num_classes=5)

print(one_hot_tensor)