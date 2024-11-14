# Minimal makefile for Sphinx documentation
# Read tutorial of not working
# https://makepp.sourceforge.net/1.19/makepp_tutorial.html

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Fetch rule: Add a rule to fetch the latest stable branch
fetch:
	@echo "Fetching the latest stable branch..."
	git fetch origin --force --prune --prune-tags --depth 50 refs/heads/stable:refs/remotes/origin/stable

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile fetch

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: fetch Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
