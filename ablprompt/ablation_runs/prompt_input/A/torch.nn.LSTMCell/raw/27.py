import torch
import torch.nn as nn

# Define an LSTM cell
lstm_cell = nn.LSTMCell(input_size=10, hidden_size=20)

# Create some input data and initial hidden state
input_data = torch.randn(5, 10)  # sequence of 5 inputs, each of size 10
hidden_state = (torch.randn(1, 20), torch.randn(1, 20))  # initial hidden state and cell state

# Pass the input data through the LSTM cell
next_hidden_state, next_cell_state = lstm_cell(input_data, hidden_state)

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)