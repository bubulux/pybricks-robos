
# Global Variables ------------------------------------------

v-pip=.venv/bin/pip
v-python=.venv/bin/python

builder=common/utils/build.py

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

build=build

# Robot config variables (simple assignment)
blue_body_name=NAME_OF_BLUE_BODY_ROBOT
blue_body_main=build/blue/body/index.py

blue_legs_name=NAME_OF_BLUE_LEGS_ROBOT
blue_legs_main=build/blue/legs/index.py

red_body_name=Lohm
red_body_main=build/red/body/index.py

red_legs_name=Fums
red_legs_main=build/red/legs/index.py


# BUILD ------------------------------------------------------

robots-purge-builds:
	@rm -rf $(build)/*

robots-build:
	@echo "Building Robots..."
	@$(v-python) $(builder) --silent
	@echo "Build Complete."

# DEPLOY ----------------------------------------------------


# Generic BLE deploy function
deploy-ble:
	@$(v-python) -m pybricksdev run ble -n $(ROBOT_NAME) $(MAIN_PY)

robots-deploy-blue-body:
	@echo "Deploying to Blue Body Robot..."
	-$(MAKE) robots-build --no-print-directory
	-$(MAKE) deploy-ble ROBOT_NAME=$(blue_body_name) MAIN_PY=$(blue_body_main) --no-print-directory

robots-deploy-blue-legs:
	@echo "Deploying to Blue Legs Robot..."
	-$(MAKE) robots-build --no-print-directory
	-$(MAKE) deploy-ble ROBOT_NAME=$(blue_legs_name) MAIN_PY=$(blue_legs_main) --no-print-directory

robots-deploy-red-body:
	@echo "Deploying to Red Body Robot..."
	-$(MAKE) robots-build --no-print-directory
	-$(MAKE) deploy-ble ROBOT_NAME=$(red_body_name) MAIN_PY=$(red_body_main) --no-print-directory

robots-deploy-red-legs:
	@echo "Deploying to Red Legs Robot..."
	-$(MAKE) robots-build --no-print-directory
	-$(MAKE) deploy-ble ROBOT_NAME=$(red_legs_name) MAIN_PY=$(red_legs_main) --no-print-directory