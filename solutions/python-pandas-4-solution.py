def get_len(x):
    return len(x.split())

S = Email['Email'].apply(get_len)
S

# or
# Email['Email'].str.split().str.len()