import torch
from torch.nn import TransformerDecoderLayer, Embedding, PositionalEncoding

# Define model parameters
d_model = 512
nhead = 8
num_layers = 6

# Create embedding layers
src_embedding = Embedding(1000, d_model)
tgt_embedding = Embedding(1000, d_model)

# Create positional encoding
pos_encoder = PositionalEncoding(d_model, max_len=1000)

# Create transformer decoder layer
decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)

# Initialize source and target sequences
src = pos_encoder(src_embedding(torch.randint(0, 1000, (10, 32))))
tgt = pos_encoder(tgt_embedding(torch.randint(0, 1000, (10, 32))))

# Forward pass through the decoder layer
output = decoder_layer(tgt, src)

print(output.shape)