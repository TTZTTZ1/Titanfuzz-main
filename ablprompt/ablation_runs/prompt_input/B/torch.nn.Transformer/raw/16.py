import torch
from torch.nn import Transformer, MultiHeadAttention, Linear

# Define a simple model using Transformer
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, input_dim, output_dim, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward):
        super(SimpleTransformerModel, self).__init__()
        self.embedding = Linear(input_dim, d_model)
        self.transformer = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers, num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward)
        self.fc_out = Linear(d_model, output_dim)

    def forward(self, src, tgt):
        src = self.embedding(src)
        tgt = self.embedding(tgt)
        output = self.transformer(src, tgt)
        return self.fc_out(output)

# Initialize the model
model = SimpleTransformerModel(input_dim=10, output_dim=5, d_model=256, nhead=8, num_encoder_layers=3, num_decoder_layers=3, dim_feedforward=512)

# Dummy input data
src = torch.rand((10, 32, 10))
tgt = torch.rand((10, 32, 10))

# Forward pass
output = model(src, tgt)
print(output.shape)  # Should be (10, 32, 5)