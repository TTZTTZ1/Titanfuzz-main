import torch

# Example usage of torch.nn.functional.one_hot
input_tensor = torch.tensor([0, 1, 4])
one_hot_encoded = torch.nn.functional.one_hot(input_tensor, num_classes=5)
print(one_hot_encoded)