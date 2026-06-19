import torch

# Create some random tensors
batch_size = 2
seq_len = 3
hidden_dim = 4

a = torch.randn(batch_size, seq_len, hidden_dim)
b = torch.randn(seq_len, batch_size, hidden_dim)

# Perform batched matrix multiplication
result = torch.matmul(a, b)

print(result)