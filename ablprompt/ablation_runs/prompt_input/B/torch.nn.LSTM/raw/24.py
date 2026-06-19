import torch
import torch.nn as nn

# Define the LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional)
    
    def forward(self, x):
        h0 = torch.zeros(self.lstm.num_layers * (2 if self.lstm.bidirectional else 1), x.size(0), self.lstm.hidden_size).to(x.device)
        c0 = torch.zeros(self.lstm.num_layers * (2 if self.lstm.bidirectional else 1), x.size(0), self.lstm.hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        return out

# Create an instance of the model
input_size = 10
hidden_size = 20
num_layers = 2
model = LSTMModel(input_size, hidden_size, num_layers, bidirectional=True)

# Prepare the input data
sequence_length = 5
batch_size = 3
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass
output = model(input_data)
print(output.shape)  # Should print: torch.Size([5, 3, 40])