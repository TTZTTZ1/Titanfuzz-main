import torch

# Example usage of torch.nn.functional.one_hot
input_tensor = torch.tensor([1, 3, 4, 8], dtype=torch.long)
one_hot_encoded = torch.nn.functional.one_hot(input_tensor, num_classes=9)
print(one_hot_encoded)