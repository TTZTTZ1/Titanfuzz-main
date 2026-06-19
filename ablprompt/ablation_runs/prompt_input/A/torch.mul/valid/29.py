import torch

# Create two tensors
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

# Call the torch.mul API to multiply the tensors
result = torch.mul(tensor1, tensor2)

print(result)