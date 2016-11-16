alias cl='clear'
alias venv="virtualenv env"
alias aenv="source env/bin/activate"
alias denv="deactivate"

alias dirsize='du -sh ${1}'
alias server="python -m SimpleHTTPServer"
alias branch="git rev-parse --abbrev-ref HEAD"

alias hogs="ps wwaxr -o pid,stat,%cpu,time,name,comm | head -10"
alias llt="ls -lthUr"
alias llat="ls -althUr"
alias status='echo -n "Branch: " && git rev-parse --abbrev-ref HEAD && git status -s'
# alias cat='pygmentize -O style=tomorrownight -f console256 -g'
alias loc='find . -type f | xargs wc -l'
# alias ping='grc -es --colour=auto ping'
# alias traceroute='grc -es --colour=auto traceroute'

alias myip='curl ip.appspot.com'
# netCons: Show all open TCP/IP sockets
alias netcons='lsof -i'
# flushDNS: Flush out the DNS Cache
alias flushdns='dscacheutil -flushcache'
# lsock: Display open sockets
alias lsock='sudo /usr/sbin/lsof -i -P'
# lsockU: Display only open UDP sockets
alias lsockU='sudo /usr/sbin/lsof -nP | grep UDP'
# lsockT: Display only open TCP sockets
alias lsockT='sudo /usr/sbin/lsof -nP | grep TCP'
# ipInfo0: Get info on connections for en0
alias ipinfo0='ipconfig getpacket en0'
# ipInfo1: Get info on connections for en1
alias ipinfo1='ipconfig getpacket en1'
# openPorts: All listening connections
alias openports='sudo lsof -i | grep LISTEN'
# showBlocked: All ipfw rules inc/ blocked IPs
alias showblocked='sudo ipfw list'
