import torch
from torch.nn import MultiheadAttention

# Initialize the MultiheadAttention layer
embed_dim = 512
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Prepare input tensors
batch_size = 32
seq_len = 64
query = torch.randn(batch_size, seq_len, embed_dim)
key = torch.randn(batch_size, seq_len, embed_dim)
value = torch.randn(batch_size, seq_len, embed_dim)

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should print: torch.Size([32, 64, 512])
print(attn_output_weights.shape)  # Should print: torch.Size([32, 8, 64, 64])