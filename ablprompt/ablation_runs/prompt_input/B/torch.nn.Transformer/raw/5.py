import torch
from torch.nn import Transformer, TransformerEncoderLayer, TransformerDecoderLayer

# Define a simple model using Transformer layers
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, input_dim, output_dim, nhead, num_encoder_layers, num_decoder_layers):
        super(SimpleTransformerModel, self).__init__()
        encoder_layer = TransformerEncoderLayer(d_model=input_dim, nhead=nhead)
        decoder_layer = TransformerDecoderLayer(d_model=input_dim, nhead=nhead)
        self.transformer = Transformer(
            encoder=TransformerEncoder(encoder_layer, num_encoder_layers),
            decoder=TransformerDecoder(decoder_layer, num_decoder_layers)
        )
        self.fc_out = torch.nn.Linear(input_dim, output_dim)

    def forward(self, src, tgt):
        output = self.transformer(src, tgt)
        return self.fc_out(output)

# Create an instance of the model
model = SimpleTransformerModel(input_dim=128, output_dim=64, nhead=8, num_encoder_layers=6, num_decoder_layers=6)

# Dummy data
src = torch.rand(10, 32, 128)  # (sequence length, batch size, input dim)
tgt = torch.rand(15, 32, 128)  # (sequence length, batch size, input dim)

# Forward pass
output = model(src, tgt)
print(output.shape)  # Should be (15, 32, 64)