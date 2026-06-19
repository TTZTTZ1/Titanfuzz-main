import torch
import torch.nn as nn

# Define an LSTMCell instance
lstm_cell = nn.LSTMCell(input_size=10, hidden_size=20)

# Initialize input and hidden state
input_data = torch.randn(5, 10)  # Sequence of 5 inputs, each with 10 features
hidden_state = torch.zeros(1, 20)
cell_state = torch.zeros(1, 20)

# Perform one step of LSTM computation
new_hidden_state, new_cell_state = lstm_cell(input_data, (hidden_state, cell_state))

print("New Hidden State:", new_hidden_state)
print("New Cell State:", new_cell_state)