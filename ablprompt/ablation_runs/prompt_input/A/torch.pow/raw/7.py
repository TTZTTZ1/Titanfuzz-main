import torch

# Create two tensors
tensor1 = torch.tensor([2, 3])
tensor2 = torch.tensor([3, 2])

# Call the torch.pow function
result = torch.pow(tensor1, tensor2)

print(result)