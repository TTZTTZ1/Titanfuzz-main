import torch
import torch.nn as nn

# Define an LSTM cell
lstm_cell = nn.LSTMCell(input_size=10, hidden_size=20)

# Input sequence and initial hidden state
input_sequence = torch.randn(5, 10)  # 5 time steps, each with 10 features
hidden_state = (torch.randn(1, 20), torch.randn(1, 20))  # Initial hidden state and cell state

# Forward pass through the LSTM cell
for input_t in input_sequence:
    hidden_state = lstm_cell(input_t, hidden_state)

print(hidden_state)