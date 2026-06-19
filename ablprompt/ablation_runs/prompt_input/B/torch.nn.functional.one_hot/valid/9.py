import torch

# Example usage of torch.nn.functional.one_hot
input_tensor = torch.tensor([2, 0, 3], dtype=torch.long)
one_hot_encoded = torch.nn.functional.one_hot(input_tensor, num_classes=4)
print(one_hot_encoded)