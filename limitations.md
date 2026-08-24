# Limitations and Falsification

LYNX is an experimental novelty-evaluation framework.

## Limitations

- Feature representation strongly affects distance.
- High-dimensional distance can be misleading.
- Rare behavior is not necessarily novel.
- Novelty is not necessarily useful.
- Archive incompleteness inflates novelty.
- Replication may be expensive.

## Falsification criteria

LYNX's central hypothesis is weakened if:

1. Standard outlier detection performs equivalently.
2. Historical rediscovery filtering adds no value.
3. Replication weighting does not improve precision.
4. Yield weighting does not improve practical relevance.
5. Results fail on held-out known-novelty datasets.
6. Novelty rankings are unstable across reasonable representations.

## Claim boundary

LYNX estimates novelty relative to its reference archive and feature representation. It cannot prove absolute novelty.
