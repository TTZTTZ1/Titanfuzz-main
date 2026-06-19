import torch

# Create two tensors
tensor1 = torch.tensor([2.0, 3.0, 4.0])
tensor2 = torch.tensor([1.0, 1.0, 1.0])

# Call the torch.sub function
result = torch.sub(tensor1, tensor2)

print(result)