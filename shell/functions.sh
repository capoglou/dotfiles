dropbox() {
  local base_url="https://dl.dropboxusercontent.com/u/353609/"

  if [[ $# -eq 2 ]]; then
    cp ${1} ~/Dropbox/Public/
    local url=${base_url}${1}
    echo ${url} | pbcopy
    open -a Safari ${url}
  else
    cp ${1} ~/Dropbox/Public/
    local url=${base_url}${1}
    echo ${url} | pbcopy
  fi
}

gifcat() {
  boom gifs ${1} > /dev/null
  curl -s $(pbpaste) | imgcat
}

finder() {
  current_dir1=$(pwd)
  open ${current_dir1}
}

copy() {
  /bin/cat $1 | pbcopy
}

nsubl() {
  touch $1 && subl $1
}

json() {
  jo -p ${*} | pbcopy
}

wiktionary() {
  word_lookup=${1}
  open -a Safari "http://de.wiktionary.org/wiki/"${word_lookup}
}

randomizemac() {
  openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//' | \
    xargs sudo ifconfig en0 ether
}

# alias ll='ls -l'
ll() {
  current_dir=$(pwd)
  dls_dir="/Users/apas/Downloads"
  if [[ ${current_dir} == ${dls_dir} ]]; then
    llt
  else
    ls -lh
  fi
}

# alias lla='ls -al'
lla() {
  current_dir=$(pwd)
  dls_dir="/Users/apas/Downloads"
  if [[ ${current_dir} == ${dls_dir} ]]; then
    llat
  else
    ls -alh
  fi
}

changedfiles() {
  if [[ -z "${1}" ]]; then
    echo "Please specify a git commit."
  else
    git diff-tree --no-commit-id --name-only -r ${1}
  fi
}

latestcommits() {
  if [[ -z "${1}" ]]; then
    echo "Please specify an integer to determine number of commits."
  else
    git log --format="%h - %s - %an" -n ${1}
  fi
}

dash() {
  open dash://$1
}

facetime() {
  open facetime://${1}
}

call() {
  open tel://${1}
}

preview() {
  open -a Preview ${*}
}

count() {
  cat $1 | tr [:space:] '\n' | grep -v "^\s*$" | sort | uniq -c | sort -bnr
}

checkdiff() {
  comm -2 -3 $1 $2 > diff.txt && cat diff.txt
}

showchanged() {
  git log --name-status -$1
}

deploy() {
  python athena.py build
  cd build/ && git add . && git commit -m "automated deploy" && git push origin master && cd -
}

ck() {
  declare -a array=("‘I'm bored’ is a useless thing to say. You live in a great, big, vast world that you've seen none percent of." 
    "America's a family. We all yell at each other. It all works out." 
    "I don't stop eating when I'm full. The meal isn't over when I'm full. It's over when I hate myself." 
    "Life isn't something you possess. It's something you take part in, and you witness." 
    "It's more fun to experience things when you don't know what's going to happen." 
    "I think one reason TV has always done well is because there is something comforting where you kind of know what you're going to be taken through." 
    "Well, but maybe..." 
    )

  var=$[ 0 + $[ $RANDOM % 6 ]]
  echo ${array[$var]}
}

edit() {
  subl ~/.bash_profile
}

giddy() {
  source ~/.bash_profile
}

port() {
  lsof -i :$1
}

killport() {
  for i in `port 5000 | awk '{print $2}'`; do kill ${i}; done
}

git-undo() {
  git checkout HEAD $1
}

chrome() {
  open -a "Google Chrome" $1
}

movie() {
  imdb -t "$*"
}

mcd() {
  mkdir $1 && cd $1
}

#needs brew install ttytter
tw() {
  input=$@ && echo $input | ttytter
}

graph() {
  git log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
}

gh() {
  if [[ $# -eq 1 ]]; then
    giturl=$(git config --get remote.origin.url)
    if [ "$giturl" == "" ]
      then
       echo "Not a git repository or no remote.origin.url set"
       # exit 0;
    fi
   
    giturl=${giturl/git\@github\.com\:/https://github.com/}
    giturl=${giturl/\.git/\/tree}
    branch="$(git symbolic-ref HEAD 2>/dev/null)" ||
    branch="(unnamed branch)"     # detached HEAD
    branch=${branch##refs/heads/}
    giturl=$giturl/$branch/$1
    open $giturl
  fi

  if [[ $# -ne 1 ]]; then
    giturl=$(git config --get remote.origin.url)
    if [ "$giturl" == "" ]
      then
       echo "Not a git repository or no remote.origin.url set"
       # exit 0;
    fi
   
    giturl=${giturl/git\@github\.com\:/https://github.com/}
    giturl=${giturl/\.git/\/tree}
    branch="$(git symbolic-ref HEAD 2>/dev/null)" ||
    branch="(unnamed branch)"     # detached HEAD
    branch=${branch##refs/heads/}
    giturl=$giturl/$branch
    open $giturl
  fi
}

build() {
  if [[ $# -ne 1 ]]; then
    echo "build needs one .cpp file as parameter."
    echo "g++ -Wall -O3 <filename.cpp> -o <filename>"
  fi

  if [[ $# -eq 1 ]]; then
    source="$( cut -d '.' -f 1 <<< "$1" )"
    g++ -Wall -O3 $1 -o $source
  fi
}

brun() {
  if [[ $# -ne 1 ]]; then
    echo "brun needs one .cpp file as parameter."
    echo "g++ -Wall -O3 <filename.cpp> -o <filename> && ./<filename>"
  fi

  if [[ $# -eq 1 ]]; then
    source="$( cut -d '.' -f 1 <<< "$1" )"
    build $1 && ./$source
  fi
}

gifify() {
  if [[ -n "$1" ]]; then
    ffmpeg -i $1 -pix_fmt rgb32 -r 25 -f gif - | gifsicle --optimize=3 --delay=3 > out.gif
  else
    echo "proper usage: gifify <input_movie.mov>. You DO need to include extension."
  fi
}
