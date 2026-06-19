import torch

# Initialize LSTMCell
input_size = 10
hidden_size = 20
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Input data and hidden state initialization
input_data = torch.randn(1, input_size)  # batch of size 1
hidden_state = (torch.randn(1, hidden_size), torch.randn(1, hidden_size))  # h_t and c_t

# Forward pass through LSTMCell
next_hidden_state, next_cell_state = lstm_cell(input_data, hidden_state)

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)