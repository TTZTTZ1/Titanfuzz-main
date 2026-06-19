import torch

# Create two tensors
tensor1 = torch.tensor([2.0, 3.0])
tensor2 = torch.tensor([1.0, 2.0])

# Call the torch.sub function to subtract tensor2 from tensor1
result = torch.sub(tensor1, tensor2)

print(result)