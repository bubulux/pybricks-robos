v-pip=.venv/bin/pip
v-python=.venv/bin/python

builder=global/utils/build.py

# Environment -------------------------------------------------

env-prerequisites:
	@sudo apt-get update
	@sudo apt-get install -y python3 python3-venv python3-pip

env-create:
	@python3 -m venv .venv
	@. .venv/bin/activate
	@$(v-pip) install -r requirements.txt

env-update:
	@$(v-pip) install --upgrade -r requirements.txt

# Robots ------------------------------------------------------

# VARS

bb=blue-body
bl=blue-legs
rb=red-body
rl=red-legs

build=build

$(bb)-src=robots/blue/body
$(bb)-main=$(build)/$($(bb)-src)/index.py
$(bb)-name=NAME_OF_BLUE_BODY_ROBOT

$(bl)-src=robots/blue/legs
$(bl)-main=$($(bl)-src)/index.py
$(bl)-name=NAME_OF_BLUE_LEGS_ROBOT

$(rb)-src=robots/red/body
$(rb)-main=$($(rb)-src)/index.py
$(rb)-name=NAME_OF_RED_BODY_ROBOT

$(rl)-src=robots/red/legs
$(rl)-main=$($(rl)-src)/index.py
$(rl)-name=NAME_OF_RED_LEGS_ROBOT


# ------------

# SCRIPTS

robots-purge-builds:
	@rm -rf $(build)/*

robots-build:
	@$(v-python) $(builder)

# ------------