import torch

# Example tensor of class indices
class_indices = torch.tensor([0, 2, 3, 1])

# Convert to one-hot encoding with inferred number of classes
one_hot_encoded = torch.nn.functional.one_hot(class_indices)

print(one_hot_encoded)