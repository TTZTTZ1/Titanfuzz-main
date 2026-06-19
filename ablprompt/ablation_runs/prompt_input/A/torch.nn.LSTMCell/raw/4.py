import torch
import torch.nn as nn

# Define input size, hidden size, and number of layers for LSTM
input_size = 10
hidden_size = 20
num_layers = 1

# Create an instance of LSTMCell
lstm_cell = nn.LSTMCell(input_size, hidden_size)

# Generate random input tensor and hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = (torch.randn(1, hidden_size), torch.randn(1, hidden_size))

# Perform a single step through the LSTMCell
next_hidden_state, next_cell_state = lstm_cell(input_tensor, hidden_state)

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)