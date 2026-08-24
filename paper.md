# LYNX: Latent Yield and Novelty eXamination

## Abstract

LYNX is an experimental framework for distinguishing genuinely novel behavior from ordinary variation, known rare modes, and random deviation. It combines nearest-reference distance, rarity, historical rediscovery filtering, replication stability, and optional yield weighting.

## 1. Motivation

Novelty claims are frequently inflated by incomplete baselines.

LYNX requires novelty to be evaluated relative to known behavior and historical rare cases.

## 2. Model

Distance novelty:

`D = min distance to reference`

Rarity:

`R = local neighbor distance`

Rediscovery similarity:

`Q = similarity to known rare archive`

Adjusted novelty:

`N = alpha D + beta R - gamma Q`

Latent yield:

`L = N * replication * yield`

## 3. Metrics

- novelty score
- rarity
- rediscovery similarity
- replication stability
- yield
- emergence precision
- archive sensitivity

## 4. Baselines

- nearest-neighbor outlier score
- isolation forest
- one-class methods
- density estimation
- novelty search
- clustering residuals

## 5. Ablations

- remove rare archive
- remove replication
- remove yield
- distance only
- rarity only
- alternate representations

## 6. Falsification

If standard outlier or density methods match LYNX on held-out novelty tasks, its additional structure is not justified.

## 7. Claim boundary

LYNX measures relative novelty. It cannot establish absolute originality or scientific novelty beyond its archive.
