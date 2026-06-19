import torch
from torch.nn import TransformerEncoderLayer

# Define a simple model using TransformerEncoderLayer
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8, dim_feedforward=2048, num_layers=6):
        super(SimpleTransformerModel, self).__init__()
        encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward)
        self.transformer_encoder = torch.nn.TransformerEncoder(encoder_layer, num_layers)

    def forward(self, src):
        return self.transformer_encoder(src)

# Example usage
if __name__ == "__main__":
    model = SimpleTransformerModel()
    src = torch.rand(10, 32, 512)  # Batch size x Sequence length x Feature size
    output = model(src)
    print(output.shape)