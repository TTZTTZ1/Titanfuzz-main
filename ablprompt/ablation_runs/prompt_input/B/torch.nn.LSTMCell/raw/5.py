import torch
from torch.nn import LSTMCell

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = LSTMCell(input_size, hidden_size)

# Create input and initial states
batch_size = 3
input_tensor = torch.randn(batch_size, input_size)
h_0 = torch.zeros(batch_size, hidden_size)
c_0 = torch.zeros(batch_size, hidden_size)

# Forward pass through LSTMCell
h_1, c_1 = lstm_cell(input_tensor, (h_0, c_0))

print("Next hidden state:", h_1)
print("Next cell state:", c_1)