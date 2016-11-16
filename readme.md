# dotfiles

**dotfiles** is the robust macOS configuration files and shell utilities
collection I've crafted and use for customizing and automatically setting up
the software development tools I use on a day-to-day basis.

dotfiles assumes it's being installed in a brand new computer and always
builds from scratch. Thus, the installer script has no dependencies outside
the Python standard library.

#### Why?

I was tired of having a (very) long `.bash_profile`. I also wanted some sort
of mechanism to easily customize new systems according to my preferences. And,
lastly, I also wanted a backup system in case things go south. That led to this
project. It's topic-centered (i.e., I structured the project accordingly,)
implements an installer, and acts as a backup.

## Installation

1. Git clone this repo and `cd` in.
2. `$ python pilgrim.py`

`pilgrim.py` will install the `.bash_profile` and other bash paraphernalia,
a [Git aware prompt][gap], the Git configuration scheme, nano syntax
highlighting and relevant settings, pandoc `LaTeX` templates, custom scripts
in the $PATH, required `LaTeX` packages, the DejaVu Sans Mono fonts, brew
formulas, Ruby gems, pip packages, sensible macOS defaults, Sublime Text 2 with
customized settings and installed packages, iTerm 2 with customized settings,
and a Tomorrow Night-themed Pygments lexer for enhanced `cat` support.

Furthermore, `pilgrim.py` hushes the login prompt and downloads both Sublime
Text 2 and iTerm 2 from their official websites. There's no `brew cask` for
now.

#### Caveats

:pushpin: `install_texpackages()` doesn't install a TeX distribution.
(It will install BasicTex in the future.)

## Components

- **bin/**: Scripts inside `bin/` will be added to your $PATH;
- **boom/**: The reaction gif archive repository;
- **brew/**: List of brew formulas to be installed;
- **fonts/**: The DejaVu Sans Mono fonts;
- **gap/**: The Git aware prompt;
- **gem/**: List of ruby gems to be installed;
- **git/**: Git configuration scheme;
- **iterm/**: iTerm2 settings and themes;
- **macos/**: Sensible macOS defaults;
- **nano/**: nano settings and syntax highlighting;
- **pdoc/**: Custom Pandoc templates accessed by `bin/` scripts;
- **pip/**: List of Python packages to be installed;
- **remote-server/**: Bare-bones dotfiles for my remote servers;
- **shell/**: Shell utilities, aliases, functions sourced by `bash_profile`
- **sublime/**: My Sublime Text 2 custom settings, environment, and icon
  replacement;
- **tlmgr/**: List of LaTeX packages to be installed.

## Features

dotfiles aspires to opinionated functional minimalism. Hence, for instance,
the rather utilitarian `PS1` prompt. It features only the current working 
path and, if inside a Git repo, the current branch name with a status change
indicator in case of untracked or uncommited file changes. However, when
inside a remote server I opt for a hardcoded server name in brackets along
with user name, host name, current working directory, and the aforementioned
Git aware prompt. (See relevant screenshots.) I could've gone without the
user and host names but in some cases I need to manage different users in
servers which provide different log in hosts. (Such as [Broad][broad].) In any
case, the bracketed naming scheme helps me quickly glance over the prompt and
remember where I am.

dotfiles also comes with cool features out of the box such as an integrated
reaction gif archive and gif display _within_ the terminal. `gifcat` is an
abstraction layer atop Holman's [`boom`][boom]. Manage your reaction archive
with `boom` and use `gifcat` to quickly access, view, and share it.

Moreover, there are lots of handy bash aliases and functions that make me a lot
more productive. My exact Sublime Text copy; packages, settings, and all: Git
gutters, my Markdown to beautiful PDFs by way of Pandoc publishing environment,
and more. As well as my iTerm 2 settings copy. It's a lot of stuff. Check them
out in the file browser above and see what components may mesh up with you.
[Fork the repo][fork], remove what you don't use, and build on what you do use.

## Screenshots

![Demo screenshot](https://i.imgur.com/9DQ0hXC.jpg)

## Bugs

I do use this as _my_ dotfiles, so there's a good chance it may break something
in your system. In any case, if you run into any blockers, please open an
issue and I'd love to get it fixed for you.

<!-- LINKS AND REFERENCES -->

[gap]: http://github.com/jimeh/git-aware-prompt
[broad]: http://broadinstitute.org
[boom]: http://github.com/holman/boom
[fork]: http://github.com/apas/dotfiles/fork

## License

MIT
