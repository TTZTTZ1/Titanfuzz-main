import torch

# Create two tensors
tensor1 = torch.tensor([2, 3])
tensor2 = torch.tensor([3, 2])

# Call torch.pow to raise tensor1 to the power of tensor2
result = torch.pow(tensor1, tensor2)

print(result)