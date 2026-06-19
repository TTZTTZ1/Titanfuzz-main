import torch
import torch.nn as nn

# Define an LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False, dropout=0.0):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional, dropout=dropout)
    
    def forward(self, x):
        h0 = torch.zeros(num_layers * (2 if bidirectional else 1), x.size(0), hidden_size).to(x.device)
        c0 = torch.zeros(num_layers * (2 if bidirectional else 1), x.size(0), hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
seq_length = 5

model = LSTMModel(input_size, hidden_size, num_layers)
input_data = torch.randn(seq_length, batch_size, input_size)
output = model(input_data)

print(output.shape)  # Should print: torch.Size([5, 3, 40])