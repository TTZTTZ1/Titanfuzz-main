import torch
import torch.nn as nn

# Define an LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False, dropout=0.0, proj_size=0):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional, dropout=dropout, proj_size=proj_size)

    def forward(self, x):
        h0 = torch.zeros(num_layers * (2 if bidirectional else 1), x.size(0), hidden_size).to(x.device)
        c0 = torch.zeros(num_layers * (2 if bidirectional else 1), x.size(0), hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        return out

# Create a sample input tensor
input_tensor = torch.randn(10, 3, 16)  # seq_len=10, batch=3, input_size=16

# Initialize the model
model = LSTMModel(input_size=16, hidden_size=32, num_layers=2, bidirectional=True, dropout=0.5, proj_size=16)

# Forward pass
output = model(input_tensor)
print(output.shape)  # Should print torch.Size([10, 3, 32])