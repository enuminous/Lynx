# LYNX — EFMW Zoo #36

**Latent Yield and Novelty eXamination**

LYNX is an experimental EFMW-inspired framework for distinguishing genuinely novel or emergent behavior from ordinary variation, noise, interpolation, memorization, or rediscovery.

## Core question

> Is this behavior actually new, or does it only look new because we are measuring it poorly?

LYNX evaluates novelty relative to known behavior, expected variation, and historical context.

## Primary outputs

- novelty score
- behavioral distance
- rarity estimate
- rediscovery penalty
- latent-yield score
- stability under replication
- emergence confidence

## Repository contents

- `theory.md`
- `architecture.md`
- `novelty_model.md`
- `limitations.md`
- `lynx.py`
- `benchmark.py`
- `ablations.py`
- `test_lynx.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_lynx.py
```

## Zoo position

MOLE #35 detects hidden failure beneath healthy-looking telemetry.

**LYNX #36 asks whether a newly observed behavior is genuinely novel enough to deserve separate attention.**
