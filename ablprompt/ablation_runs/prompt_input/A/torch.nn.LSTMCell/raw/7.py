import torch
import torch.nn as nn

# Define an LSTM cell
lstm_cell = nn.LSTMCell(input_size=10, hidden_size=20)

# Input sequence and initial hidden state
input_seq = torch.randn(5, 1, 10)  # Sequence of length 5, batch size 1, input size 10
hidden_state = (torch.randn(1, 1, 20), torch.randn(1, 1, 20))  # Initial hidden state and cell state

# Forward pass through the LSTM cell
new_hidden_state, new_cell_state = lstm_cell(input_seq[0], hidden_state)

print("New Hidden State:", new_hidden_state)
print("New Cell State:", new_cell_state)