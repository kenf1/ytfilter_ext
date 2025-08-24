.PHONY: fmt clean

fmt: ##Format
	ruff format
	find . -type d -name ".ruff_cache" | xargs rm -rf

clean: fmt ##Tidy repo: rm unnec folders
	find . -type d -name "__pycache__" | xargs rm -rf