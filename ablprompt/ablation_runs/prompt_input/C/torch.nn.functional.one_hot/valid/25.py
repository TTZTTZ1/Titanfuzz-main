import torch

# Example tensor of class indices
indices = torch.tensor([1, 3, 2, 0])

# Convert to one-hot encoding
one_hot_encoded = torch.nn.functional.one_hot(indices)

print(one_hot_encoded)