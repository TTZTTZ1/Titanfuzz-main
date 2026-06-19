```python
import torch
from torch.nn import Transformer, MultiHeadAttention, Linear, LayerNorm

# Define a simple model using Transformer
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout=0.5):
        super(SimpleTransformerModel, self).__init__()
        self.transformer = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers,
                                       num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward, dropout=dropout)
        self.src_pos_encoder = PositionalEncoding(d_model, dropout)
        self.tgt_pos_encoder = PositionalEncoding(d_model, dropout)
        self.encoder_layer = nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout)
        self.decoder_layer = nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout)
        self.encoder_norm = LayerNorm(d_model)
        self.decoder_norm = LayerNorm(d_model)
        self.fc_out = Linear(d_model, d_model)

    def forward(self, src, tgt):
        src = self.src_pos_encoder(src)
        tgt = self.tgt_pos_encoder(tgt)
        output = self.transformer(src, tgt)
        return self.fc_out(output)

# Helper class for positional encoding
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)

        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-torch.log(torch.tensor(10000.0)) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:x.size(0), :]
        return self.dropout(x)

# Example usage
model = SimpleTransformerModel(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers