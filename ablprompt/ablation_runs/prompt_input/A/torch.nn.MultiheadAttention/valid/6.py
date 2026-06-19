import torch
from torch.nn import MultiheadAttention

# Initialize the MultiheadAttention module
embed_dim = 512
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Prepare some input data
batch_size = 32
seq_len = 64
query = torch.randn(seq_len, batch_size, embed_dim)
key = value = query  # For simplicity, using the same query for key and value

# Forward pass through the MultiheadAttention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should print: torch.Size([64, 32, 512])
print(attn_output_weights.shape)  # Should print: torch.Size([32, 8, 64, 64])