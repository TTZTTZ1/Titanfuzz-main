import torch

# Create random tensors for demonstration
batch_size = 2
seq_len = 3
hidden_dim = 4

# Batched matrix multiplication example
a = torch.randn(batch_size, seq_len, hidden_dim)
b = torch.randn(batch_size, hidden_dim, seq_len)

result = torch.matmul(a, b)
print(result)