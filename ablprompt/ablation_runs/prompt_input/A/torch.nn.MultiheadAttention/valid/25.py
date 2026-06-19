import torch

# Define the input tensors for MultiheadAttention
embed_dim = 256
num_heads = 8
batch_size = 32
seq_len = 10

query = torch.randn(batch_size, seq_len, embed_dim)
key = query.clone()
value = key.clone()

# Initialize MultiheadAttention layer
multihead_attn = torch.nn.MultiheadAttention(embed_dim, num_heads)

# Perform forward pass
attn_output, attn_output_weights = multihead_attn(query, key, value)

print("Output shape:", attn_output.shape)
print("Attention weights shape:", attn_output_weights.shape)