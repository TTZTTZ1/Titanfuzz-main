import torch
from torch.nn import MultiheadAttention

# Define input tensors
embed_dim = 128
num_heads = 4
batch_size = 32
seq_len = 50

query = torch.randn(seq_len, batch_size, embed_dim)
key = torch.randn(seq_len, batch_size, embed_dim)
value = torch.randn(seq_len, batch_size, embed_dim)

# Initialize MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Forward pass through the MultiheadAttention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should print: torch.Size([50, 32, 128])
print(attn_output_weights.shape)  # Should print: torch.Size([32, 4, 50, 50])