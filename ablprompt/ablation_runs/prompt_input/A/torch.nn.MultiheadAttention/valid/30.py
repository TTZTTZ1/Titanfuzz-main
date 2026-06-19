import torch

# Define input tensors
embed_dim = 256
num_heads = 8
batch_size = 32
seq_len = 10

query = torch.randn(seq_len, batch_size, embed_dim)
key = torch.randn(seq_len, batch_size, embed_dim)
value = torch.randn(seq_len, batch_size, embed_dim)

# Initialize MultiheadAttention layer
multihead_attn = torch.nn.MultiheadAttention(embed_dim, num_heads)

# Perform forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Should print: torch.Size([10, 32, 256])
print(attn_output_weights.shape)  # Should print: torch.Size([32, 10, 10])