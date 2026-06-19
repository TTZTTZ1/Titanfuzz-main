import torch
from torch.nn import TransformerDecoderLayer, Linear, Embedding

# Define some parameters for the TransformerDecoderLayer
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create an instance of TransformerDecoderLayer
decoder_layer = TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout, activation)

# Prepare input tensors (encoder_output and tgt)
encoder_output = torch.randn(10, 32, d_model)  # Shape: (seq_len, batch_size, d_model)
tgt = torch.randint(0, 100, (20, 32))          # Shape: (tgt_seq_len, batch_size)

# Create embeddings for tgt if needed
embedding = Embedding(num_embeddings=100, embedding_dim=d_model)
tgt = embedding(tgt)

# Pass the inputs through the decoder layer
output = decoder_layer(tgt, encoder_output)

print(output.shape)  # Should print: torch.Size([20, 32, 512])