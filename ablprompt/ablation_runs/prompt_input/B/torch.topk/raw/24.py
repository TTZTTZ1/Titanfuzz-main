import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Use torch.topk to find the top 2 largest elements along dimension 1
topk_result = torch.topk(input_tensor, k=2, dim=1)

print("Input Tensor:")
print(input_tensor)
print("\nTop K Result:")
print(topk_result)