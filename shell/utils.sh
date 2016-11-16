export GITAWAREPROMPT=~/.gap/
source $GITAWAREPROMPT/main.sh

export PS1="\[\e[36;1m\]\w\[$txtcyn\]\$git_branch\[$txtred\]\$git_dirty\[$txtrst\] \$ "

export PATH="/usr/local/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:$HOME/bin:$PATH"
export EDITOR='subl'

# color modifications for brew grc
export CLICOLOR=1
export LSCOLORS=Exfxcxdxbxegedabagacad
export TERM=xterm-color
export GREP_OPTIONS='--color=auto' GREP_COLOR='1;32'
