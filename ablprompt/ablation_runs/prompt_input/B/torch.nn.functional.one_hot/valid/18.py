import torch
import torch.nn.functional as F

# Create a random LongTensor of class indices
class_indices = torch.randint(0, 5, (3, 4))

# Convert the class indices to one-hot encoding
one_hot_encoded = F.one_hot(class_indices)

print(one_hot_encoded)