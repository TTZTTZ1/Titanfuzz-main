import torch

# Initialize LSTMCell
input_size = 10
hidden_size = 20
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Input sequence and initial hidden state
input_seq = torch.randn(5, input_size)  # 5 time steps, each of size input_size
hx = torch.randn(hidden_size)
cx = torch.randn(hidden_size)

# Forward pass through LSTMCell
hx_new, cx_new = lstm_cell(input_seq[0], (hx, cx))

print("New Hidden State:", hx_new)
print("New Cell State:", cx_new)