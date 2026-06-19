import torch

# Initialize LSTMCell
input_size = 10
hidden_size = 20
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Input data and initial hidden state
input_data = torch.randn(1, input_size)  # Batch size of 1
hidden_state = (torch.randn(1, hidden_size), torch.randn(1, hidden_size))

# Forward pass through LSTMCell
new_hidden_state = lstm_cell(input_data, hidden_state)
print(new_hidden_state)