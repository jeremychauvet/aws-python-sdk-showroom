.PHONY: lint

lint:
	pre-commit run --all-files

# KMS.
.PHONY: get-key-rotation-status

get-key-rotation-status:
	cd kms/get-key-rotation-status && python3 main.py
