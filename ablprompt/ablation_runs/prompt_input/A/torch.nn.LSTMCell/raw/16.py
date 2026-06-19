import torch
import torch.nn as nn

# Define an LSTM cell
lstm_cell = nn.LSTMCell(input_size=10, hidden_size=20)

# Initialize input and hidden state
input_data = torch.randn(1, 10)
hidden_state = (torch.randn(1, 20), torch.randn(1, 20))

# Perform a single step of the LSTM
new_hidden_state = lstm_cell(input_data, hidden_state)

print(new_hidden_state)