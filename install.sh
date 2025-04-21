#!/bin/bash

# Set install path
INSTALL_PATH="$HOME/.local/share/MarkdownReader"

# Clone the repo
mkdir -p "$HOME/.local/share"
cd "$HOME/.local/share" || exit
git clone https://github.com/martinbojovnik/MarkdownReader.git "$INSTALL_PATH"
cd "$INSTALL_PATH" || exit

# Install Python dependencies
pip install --user -r requirements.txt

# Create the launcher script
mkdir -p "$HOME/.local/bin"
cat <<EOF > "$HOME/.local/bin/open-markdown"
#!/bin/bash
python3 "$INSTALL_PATH/main.py" "\$@"
EOF

chmod +x "$HOME/.local/bin/open-markdown"

# Add ~/.local/bin to PATH if it's not there already
if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
    echo '✅ Added ~/.local/bin to PATH. Run "source ~/.bashrc" or restart your terminal to apply it.'
fi

echo "✅ Installation complete. You can now run: open-markdown"
