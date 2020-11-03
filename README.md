Smiles to Image
===============
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/simonboothroyd/smilestoimg/workflows/ci/badge.svg)](https://github.com/simonboothroyd/smilestoimg/actions?query=branch%3Amaster+workflow%3Aci)
[![codecov](https://codecov.io/gh/simonboothroyd/smilestoimg/branch/master/graph/badge.svg)](https://codecov.io/gh/simonboothroyd/smilestoimg/branch/master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A RESTful API for converting SMILES patterns into SVG images using RDKit.

### Getting Started

To start a webserver run:

```
uvicorn smilestoimg.app:app --reload
```

#### Copyright

Copyright (c) 2020, Simon Boothroyd

#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.3.
