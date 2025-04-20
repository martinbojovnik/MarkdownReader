echo Enter install path
read path

cd path
git clone https://github.com/martinbojovnik/MarkdownReader.git
cd MarkdownReader

pip install -r requirements.txt
alias open-markdown="cd $path/MarkdownReader && python main.py"