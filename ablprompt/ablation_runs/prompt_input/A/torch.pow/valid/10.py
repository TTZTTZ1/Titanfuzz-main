import torch

# Example usage of torch.pow
base = torch.tensor([2, 3, 4])
exponent = torch.tensor([3, 2, 1])
result = torch.pow(base, exponent)
print(result)  # Output: tensor([ 8,  9,  4])