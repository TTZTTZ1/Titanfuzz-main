import torch

# Define input tensors for MultiheadAttention
embed_dim = 256
num_heads = 8
batch_size = 32
seq_len = 10

query = torch.randn(batch_size, seq_len, embed_dim)
key = query.clone()
value = query.clone()

# Initialize MultiheadAttention layer
multihead_attn = torch.nn.MultiheadAttention(embed_dim, num_heads)

# Perform forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print(attn_output.shape)  # Output shape should be (batch_size, seq_len, embed_dim)