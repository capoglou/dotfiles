#!/usr/bin/env python
import sys
import os
import shutil
import glob
import pwd
import subprocess as proc
import distutils.spawn as which
import distutils.dir_util as cp

# helper global variables
home_dir = os.path.expanduser("~")
current_dir = os.getcwd()

# helper functions for colorized stdout
def has_colours(stream):
  if not hasattr(stream, "isatty"):
    return False
  if not stream.isatty():
    return False
  try:
    import curses
    curses.setupterm()
    return curses.tigetnum("colors") > 2
  except:
    return False

def print_color(text, color = 7):
  colors = has_colours(sys.stdout)
  if colors:
    seq = "\x1b[1;%dm" % (30 + color) + text + "\x1b[0m"
    sys.stdout.write(seq+"\n")
  else:
    sys.stdout.write(text+"\n")

def search_and_replace(file_to_search, original_string, new_string):
  try:
    new_file = None
    with open(file_to_search, "r") as file:
      new_file = file.read()

    new_file = new_file.replace(original_string, new_string)

    with open(file_to_search, "r+") as file:
      file.write(new_file)
  except Exception, e:
    print_color("[ERR]\tSearching and replacing in " + original_string, 1)
    raise e

# install functions
def install_brew():
  print_color("==>\tInstalling brew", 4)
  try:
    if not which.find_executable("brew"):
      proc.call(["/usr/bin/ruby",
        "-e",
        "'$(curl",
        "-fsSL",
        "https://raw.githubusercontent.com/Homebrew/install/master/install)'"])
    else:
      print_color("[INF]\tBrew installed", 2)

    print_color("==>\tInstalling brew formulas", 4)
    formulas = current_dir+"/brew/formulas"
    with open(formulas) as formulas:
      for line in formulas:
        line = line[:-1] # strip last char bc each line ends w '\n' idk why
        proc.call(["brew", "install", line])
  except Exception, e:
    print_color("[ERR]\tInstalling brew", 1)
    raise e

def install_rubygems():
  print_color("==>\tInstalling ruby gems", 4)
  try:
    if not which.find_executable("gem"):
      user_msg1 = "[INF]\tPress return when Xcode Tools are installed. "
      user_msg2 = "I can wait..."
      usr_prompt = user_msg1 + user_msg2
      rubygem_url = "https://rubygems.org/rubygems/rubygems-2.6.8.tgz"
      proc.call(["xcode-select", "--install"])
      raw_input(usr_prompt)
      if not os.path.isdir("/usr/local/bin"):
        proc.call(["mkdir", "/usr/local/bin"])
        proc.call(["chown", "-R", "apas", "/usr/local/bin"])
      proc.call(["curl", "-O", rubygem_url])
      proc.call(["tar", "-xvzf", "rubygems-2.6.8.tgz"])
      proc.call(["sudo", "ruby", "rubygems-2.6.8/setup.rb"])

    echo = "'gem: -n /usr/local/bin'"
    proc.call(["echo", echo, ">>", "~/.gemrc"])
    gems = current_dir+"/gem/gems"
    with open(gems) as gemfile:
      for line in gemfile:
        line = line[:-1] # strip last char bc each line ends w '\n' idk why
        proc.call(["gem", "install", line,])
  except Exception, e:
    print_color("[ERR]\tInstalling ruby gems", 4)
    raise e

def install_macdefaults():
  print_color("==>\tInstalling macOSX defaults", 4)
  try:
    proc.call([current_dir+"/./defaults.sh"])
  except Exception, e:
    print_color("[ERR]\tInstalling macOSX defaults", 1)

# TODO: install through brew cask
def install_sublime():
  print_color("==>\tInstalling Sublime Text 2", 4)
  try:
    sublime_url = "https://download.sublimetext.com/Sublime%20Text%202.0.2.dmg"
    app_spprt = home_dir+"/Library/Application Support/Sublime Text 2/Packages"
    proc.call(["curl", "-o", "sublime.dmg", sublime_url])
    proc.call(["open", "sublime.dmg"])
    user_msg1 = "[INF]\tPress return when Sublime's installed. "
    user_msg2 = "I can wait..."
    usr_prompt = user_msg1 + user_msg2
    raw_input(usr_prompt)
    cp.copy_tree(current_dir+"/sublime", app_spprt)
  except Exception, e:
    print_color("[ERR]\tInstalling Sublime Text 2", 1)
    raise e

def install_fonts():
  print_color("==>\tInstalling fonts", 4)
  try:
    font_dir = home_dir+"/Library/Fonts"
    cp.copy_tree(current_dir+"/fonts", font_dir)
  except Exception, e:
    print_color("[ERR]\tInstalling fonts", 1)
    raise e

def install_hushlogin():
  print_color("==>\tHushing the bash login prompt", 4)
  try:
    shutil.copy(current_dir+"/hushlogin", home_dir+"/.hushlogin")
  except Exception, e:
    print_color("[ERR]\tHushing the bash login prompt", 1)
    raise e

def install_pip():
  print_color("==>\tInstalling pip packages", 4)
  try:
    reqs = current_dir+"/pip/requirements.txt"
    proc.call(["pip", "install", "-r", reqs])
  except Exception, e:
    print_color("[ERR]\tInstalling pip packages", 1)
    raise e

def install_tomorrownight_lexer():
  print_color("==>\tInstalling Tomorrow Night Pygmentize Lexer", 4)
  try:
    dir_string1 = "/Library/Frameworks/Python.framework/Versions/2.7/"
    dir_string2 = "lib/python2.7/site-packages/pygments/styles"
    style_dir = dir_string1 + dir_string2
    shutil.copy(current_dir+"/pip/tomorrownight.py", style_dir)
  except Exception, e:
    print_color("[ERR]\tInstalling Tomorrow Night Pygmentize Lexer", 1)
    raise e

# TODO: install through brew cask
def install_iterm():
  print_color("==>\tInstalling iTerm 2", 4)
  try:
    iterm_url = "https://iterm2.com/downloads/stable/iTerm2-3_0_10.zip"
    proc.call(["curl", "-o", "iterm.zip", iterm_url])
    proc.call(["unzip", "-a", "iterm.zip"])
    proc.call(["mv", "iTerm.app", "/Applications"])

    plist = current_dir+"/iterm/com.googlecode.iterm2.plist"
    shutil.copy(plist, home_dir+"/Library/Preferences/")
  except Exception, e:
    print_color("[ERR]\tInstalling iTerm 2", 4)
    raise e

def install_texpackages():
  print_color("==>\tInstalling tlmgr packages", 4)
  try:
    packages = current_dir+"/tlmgr/packages.txt"
    with open(packages) as packages_file:
      for line in packages_file:
        line = line[:-1] # strip last char bc each line ends w '\n' idk why
        proc.call(["sudo", "tlmgr", "install", line])
  except Exception, e:
    print_color("[ERR]\tInstalling tlmgr packages", 1)
    raise e

def install_pdoc():
  print_color("==>\tInstalling Pandoc templates", 4)
  try:
    shutil.copytree(current_dir+"/pdoc", home_dir+"/pdoc")
  except Exception, e:
    print_color("[ERR]\tInstalling Pandoc templates", 1)
    raise e

def install_nano():
  print_color("==>\tInstalling nano", 4)
  try:
    nano_home_dir = home_dir+"/.nano"
    username = pwd.getpwuid( os.getuid() )[ 0 ]

    search_and_replace(current_dir+"/nano/nanorc",
      "apas",
      username)
    shutil.copy(current_dir+"/nano/nanorc",home_dir+"/.nanorc")

    if not os.path.exists(nano_home_dir):
      os.makedirs(nano_home_dir)

    nanofiles = glob.iglob(os.path.join(current_dir+"/nano/", "*.nanorc"))
    for nanofile in nanofiles:
      if os.path.isfile(nanofile):
        shutil.copy(nanofile, nano_home_dir)
  except Exception, e:
    print_color("[ERR]\tInstalling nano", 1)
    raise e

def install_binaries():
  print_color("==>\tInstalling personal shell binaries", 4)
  try:
    shutil.copytree(current_dir+"/bin", home_dir+"/bin")
  except Exception, e:
    print_color("[ERR]\tInstalling personal shell binaries", 1)
    raise e

def install_gitconfig():
  print_color("==>\tInstalling .gitconfig", 4)
  try:
    shutil.copy(current_dir+"/git/gitconfig", home_dir+"/.gitconfig")
  except Exception, e:
    print_color("[ERR]\tInstalling .gitconfig", 1)
    raise e

def install_gap():
  print_color("==>\tInstalling Git-Aware-Prompt", 4)
  try:
    shutil.copytree(current_dir+"/gap", home_dir+"/.gap")
  except Exception, e:
    print_color("[ERR]\tInstalling Git-Aware-Prompt", 1)
    raise e

def install_shell():
  print_color("==>\tInstalling bash profile and paraphernalia", 4)
  try:
    search_and_replace("bash_profile", "shell", ".shell")
    shutil.copy(current_dir+"/bash_profile", home_dir+"/.bash_profile")
    shutil.copytree(current_dir+"/shell", home_dir+"/.shell")
  except Exception, e:
    print_color("[ERR]\tInstalling bash profile and paraphernalia", 1)
    raise e

if __name__ == '__main__':
  # TODO: install remote-server
  install_shell()
  install_gap()
  install_gitconfig()
  install_nano()
  install_hushlogin()
  install_pdoc()
  install_binaries()
  install_texpackages()
  install_brew()
  install_rubygems()
  install_macdefaults()
  install_sublime()
  install_pip()
  install_iterm()
  install_tomorrownight_lexer()
  print_color("""[INF]\t.dotfiles installation complete. You can now\t
  \tsource the new .bash_profile. The command is alreay copied in\t
  \tthe clipboard for your ease -- a cmd + v away.\t
  \t
  \tGodspeed.""", 2)
  proc.call(["open", "-a", "iTerm"])
  os.system("osascript -e 'quit app \"Terminal\"'")
  clipboard = "source ~/.bash_profile"
  os.system("echo '%s' | pbcopy" % clipboard)
