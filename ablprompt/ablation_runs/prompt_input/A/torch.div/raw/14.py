import torch

# Create two tensors
tensor1 = torch.tensor([4.0, 8.0, 12.0])
tensor2 = torch.tensor([2.0, 2.0, 3.0])

# Call torch.div to divide the elements of tensor1 by those in tensor2
result = torch.div(tensor1, tensor2)

print(result)