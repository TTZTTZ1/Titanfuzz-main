import torch
from torch.nn import MultiheadAttention

# Define input tensors
query = torch.randn(10, 32, 512)  # (seq_len, batch_size, embed_dim)
key = query.clone()
value = query.clone()

# Initialize MultiheadAttention layer
multihead_attn = MultiheadAttention(embed_dim=512, num_heads=8)

# Forward pass through the MultiheadAttention layer
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should print: torch.Size([10, 32, 512])
print(attn_output_weights.shape)  # Should print: torch.Size([32, 8, 10, 10])