# Casanovo
**_De Novo_ Mass Spectrometry Peptide Sequencing with a Transformer Model**

<img src="casanovo.svg" alt="Casanovo logo" width="300">

[![PyPI](https://img.shields.io/pypi/v/casanovo)](https://pypi.org/project/casanovo/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-readthedocs-brightgreen)](https://casanovo.readthedocs.io/en/latest/)

---

## What is Casanovo?

Casanovo is a state-of-the-art deep learning tool designed for _de novo_ peptide sequencing.
Powered by a transformer neural network, Casanovo "translates" peaks in MS/MS spectra into
amino acid sequences with remarkable precision — without relying on a protein database.

Casanovo can be used to find unexpected peptide sequences in any data-dependent acquisition,
bottom-up tandem mass spectrometry dataset. It is particularly useful for:

- 🧬 **Immunopeptidomics** – Identify novel peptides presented by MHC molecules
- 🌿 **Metaproteomics** – Sequence peptides from complex microbial communities
- 🦴 **Paleoproteomics** – Recover peptide sequences from ancient or degraded samples
- 🐍 **Venomics** – Characterize toxin peptides from venom proteomes
- 🔬 **Any setting** where peptides of interest may not be present in a protein database

---

## Why Choose Casanovo?

- **Unmatched accuracy:** Cutting-edge transformer AI ensures precise and reliable peptide
  sequencing, even in challenging or noisy datasets.
- **No database required:** Unlike traditional database search tools, Casanovo sequences
  peptides entirely _de novo_, making it ideal for novel or unexpected discoveries.
- **Open-source & free:** Freely available under the Apache 2.0 license and easy to
  integrate into existing proteomics workflows.
- **Easy to install & use:** Available via `pip` with a simple command-line interface and
  pre-trained model weights ready to use out of the box.
- **Actively maintained:** Backed by the Noble Lab with regular updates, releases,
  and a growing community of researchers and developers.

---

## Quick Start

Install Casanovo via pip:

```bash
pip install casanovo
```

Run _de novo_ sequencing on your data:

```bash
casanovo sequence your_data.mgf
```

For full installation instructions, configuration options, and usage examples,
see the [Documentation](https://casanovo.readthedocs.io/en/latest/).

---

## Getting Started

- 📖 [Documentation](https://casanovo.readthedocs.io/en/latest/)
- 📝 [Citation Information](https://casanovo.readthedocs.io/en/latest/cite.html)
- 🤝 [Contributing Guidelines](CONTRIBUTING.md)
- 📋 [Changelog](CHANGELOG.md)
- 🐛 [Report an Issue](https://github.com/Noble-Lab/casanovo/issues)
