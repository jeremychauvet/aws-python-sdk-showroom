.PHONY: validate
INSTALL_CMD=pip3 install -r requirements.txt
RUN_CMD=python3 main.py

validate:
	pre-commit run --all-files

# KMS.
.PHONY: get-key-rotation-status

get-key-rotation-status:
	cd kms/get-key-rotation-status && $(INSTALL_CMD) && $(RUN_CMD)

# SQS
.PHONY: insert-fake-data-in-queue

insert-fake-data-in-queue:
	cd sqs/insert-fake-data-in-queue && $(INSTALL_CMD) && $(RUN_CMD)

# Cognito
.PHONY: get-parameters

get-parameters:
	cd cognito/get-parameters && $(INSTALL_CMD) && $(RUN_CMD)
