import torch
import torch.nn as nn

# Example usage of LayerNorm on a 3D tensor representing a sequence of token embeddings
input_tensor = torch.randn(10, 32, 64)  # Batch size 10, Sequence length 32, Embedding dimension 64
layer_norm = nn.LayerNorm(normalized_shape=(64,), eps=1e-06, elementwise_affine=True, bias=True)

output_tensor = layer_norm(input_tensor)
print(output_tensor.shape)  # Should be the same shape as input_tensor