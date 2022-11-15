---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# **projplot**: Utilities for Creating Projection Plots

**Kanika Chopra, Martin Lysy -- University of Waterloo**

**November 14, 2022**

+++


**projplot** provides a set of tools to assess whether or not an optimization algorithm has converged to a local optimum.  Its main function does this by visualizing the "projection plots" of the objective function $f(\boldsymbol{x})$ -- that is, by plotting $f$ against each coordinate of $\boldsymbol{x}$ with the other coordinates fixed at the corresponding elements of the candidate optimal solution $\boldsymbol{x}_{opt}$.  

This package has a similar goal to the R package [**optimCheck**](https://github.com/mlysy/optimCheck).

## Installation

This package is available on [PyPi](https://pypi.org/project/projplot/) and can be installed as follows:

```bash
pip install projplot
```

```{toctree}
:maxdepth: 1
:hidden:

example.md
faq.md
autoapi/index
```
