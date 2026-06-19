import torch

# Example tensor of integer class indices
indices = torch.tensor([0, 2, 1])

# Convert to one-hot encoding with inferred number of classes
one_hot_encoded = torch.nn.functional.one_hot(indices)

print(one_hot_encoded)