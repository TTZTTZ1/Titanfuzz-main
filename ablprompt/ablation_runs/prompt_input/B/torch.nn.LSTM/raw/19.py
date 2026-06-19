import torch
import torch.nn as nn

# Define an LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False, dropout=0.0):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, bidirectional=bidirectional, dropout=dropout)
        self.fc = nn.Linear(hidden_size * (2 if bidirectional else 1), 10)

    def forward(self, x):
        h0 = torch.zeros(self.lstm.num_layers * (2 if self.lstm.bidirectional else 1), x.size(0), self.lstm.hidden_size).to(x.device)
        c0 = torch.zeros(self.lstm.num_layers * (2 if self.lstm.bidirectional else 1), x.size(0), self.lstm.hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Example usage
model = LSTMModel(input_size=10, hidden_size=20, num_layers=2, bidirectional=True, dropout=0.5)
input_data = torch.randn(3, 5, 10)  # (batch_size=3, seq_len=5, input_size=10)
output = model(input_data)
print(output.shape)  # Should print torch.Size([3, 10])