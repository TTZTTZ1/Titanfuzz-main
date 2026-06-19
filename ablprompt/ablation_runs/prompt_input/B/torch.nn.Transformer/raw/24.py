import torch
from torch.nn import Transformer, MultiHeadAttention, LayerNorm, Linear

# Define a simple model using Transformer
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward):
        super(SimpleTransformerModel, self).__init__()
        self.embedding = Linear(d_model, d_model)
        self.transformer = Transformer(
            d_model=d_model,
            nhead=nhead,
            num_encoder_layers=num_encoder_layers,
            num_decoder_layers=num_decoder_layers,
            dim_feedforward=dim_feedforward
        )
        self.fc_out = Linear(d_model, d_model)

    def forward(self, src, tgt):
        src = self.embedding(src)
        tgt = self.embedding(tgt)
        output = self.transformer(src, tgt)
        output = self.fc_out(output)
        return output

# Initialize the model
model = SimpleTransformerModel(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048)

# Dummy input data
src = torch.rand((10, 32, 512))
tgt = torch.rand((20, 32, 512))

# Forward pass
output = model(src, tgt)
print(output.shape)  # Should be (20, 32, 512)