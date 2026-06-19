import torch
import torch.nn.functional as F

# Create a random tensor of integers
input_tensor = torch.randint(0, 5, (3, 4))

# Convert the tensor to one-hot encoding
one_hot_encoded = F.one_hot(input_tensor)

print(one_hot_encoded)