import torch
import torch.nn as nn

# Define a simple RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)  # Initialize hidden state
        out, _ = self.rnn(x, h0)  # Forward propagate RNN
        out = self.fc(out[:, -1, :])  # Output of the last time step
        return out

# Example usage
input_size = 10
hidden_size = 20
output_size = 5
batch_size = 3
seq_length = 4

model = SimpleRNN(input_size, hidden_size, output_size)
input_data = torch.randn(batch_size, seq_length, input_size)
output = model(input_data)
print(output.shape)  # Should print: torch.Size([3, 5])