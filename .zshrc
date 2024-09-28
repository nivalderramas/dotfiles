# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"
export TERM="kitty"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="superjarin" # set by `omz`

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)
plugins=( git z )

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
# alias code="flatpak run com.visualstudio.code ."
alias sshTesting="ssh ubuntu@34.197.208.27 -L 27018:127.0.0.1:27017 -i ~/dev/horus/horus_testing.pem"
alias r="ranger"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
alias debugQtile="tail -f ~/.local/share/qtile/qtile.log"
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export EDITOR=nvim
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.config/qtile/scripts:$PATH"

# Pywal support
# (cat ~/.cache/wal/sequences &)
# source ~/.cache/wal/colors-tty.sh
export USER_DB=mongo-root
export PASSWORD_DB=horus.mongo.2020
alias vpnUnal="sudo openconnect vpn.unal.edu.co"
export GOBIN=$HOME/go/bin
export GOPATH="$HOME/go"
export PATH=$PATH:/$GOBIN
#export GOROOT="/usr/local/go"
# export GOBIN="$GOPATH/bin"
export AWS_PROFILE=nvalderama_profile
export AWS_REGION=us-east-1
export DOWNLOAD_FOLDER=/home/nivalderramas/go/bin/

# TRUORA
alias setprod='export AWS_PROFILE=production'
alias fmt='tf fmt -recursive'
alias update_admin='applyprod -target=module.policies.module.admin_actions.aws_iam_policy.policy -auto-approve'
alias checkcode='./scripts/check_code.sh "origin...HEAD"'
alias checkformat='./scripts/check_format.sh "origin...HEAD"'
alias checkcoverage='./scripts/check_coverage.sh "origin...HEAD"'
alias checkerrors='./scripts/check_errors.sh "origin...HEAD"'
alias checksecurity='./scripts/check_security.sh "origin...HEAD"'
alias check='checkformat && checkerrors && checksecurity && checkcode && checkcoverage'

alias q="exit"
alias scaleHDMI="xrandr --output HDMI-A-0  --scale 1.30x1.30 --rate 60 --mode 1920x1080"

# WAYLAND VSCODE
#alias code='code --enable-ozone --ozone-platform=wayland'
#

eval "$(starship init zsh)"

alias cdStg="cd terraform/deploy/envs/staging"
alias cdProd="cd terraform/deploy/envs/production"
alias config='/usr/bin/git --git-dir=/home/nivalderramas/.cfg/ --work-tree=/home/nivalderramas'
