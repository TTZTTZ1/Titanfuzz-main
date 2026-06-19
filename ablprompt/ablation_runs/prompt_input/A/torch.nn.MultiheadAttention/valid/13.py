import torch
from torch.nn import MultiheadAttention

# Initialize the MultiheadAttention layer
embed_dim = 256
num_heads = 8
multihead_attn = MultiheadAttention(embed_dim, num_heads)

# Prepare input tensors
batch_size = 10
seq_len = 30
query = torch.randn(batch_size, seq_len, embed_dim)
key = query.clone()
value = key.clone()

# Perform the forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should print: torch.Size([10, 30, 256])
print(attn_output_weights.shape)  # Should print: torch.Size([10, 8, 30, 30])