import torch
import torch.nn as nn

# Define an LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False, proj_size=0):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, bidirectional=bidirectional, proj_size=proj_size)
        self.fc = nn.Linear(hidden_size * (2 if bidirectional else 1), 1)

    def forward(self, x):
        h0 = torch.zeros(num_layers * (2 if self.lstm.bidirectional else 1), x.size(0), self.lstm.hidden_size).to(x.device)
        c0 = torch.zeros(num_layers * (2 if self.lstm.bidirectional else 1), x.size(0), self.lstm.hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
bidirectional = True
proj_size = 10

model = LSTMModel(input_size, hidden_size, num_layers, bidirectional, proj_size)
input_seq = torch.randn(5, 3, input_size)
output = model(input_seq)
print(output.shape)  # Should print torch.Size([3, 1])