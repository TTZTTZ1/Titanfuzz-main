import torch
from torch.nn import LSTMCell

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = LSTMCell(input_size, hidden_size)

# Create random input and initial states
input_tensor = torch.randn(1, input_size)  # Batch size of 1
h0 = torch.randn(1, hidden_size)
c0 = torch.randn(1, hidden_size)

# Forward pass through LSTMCell
h1, c1 = lstm_cell(input_tensor, (h0, c0))

print("Next hidden state:", h1)
print("Next cell state:", c1)