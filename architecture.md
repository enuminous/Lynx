# LYNX Architecture

## Pipeline

1. Behavior Encoder
2. Reference Archive
3. Nearest-Neighbor Comparator
4. Density/Rarity Estimator
5. Historical Rediscovery Scanner
6. Replication Tracker
7. Yield Estimator
8. Emergence Scorer
9. Audit Reporter

## Inputs

- candidate behavior vectors
- reference behavior archive
- rare-event archive
- replication evidence
- optional utility/yield metric

## Outputs

```json
{
  "distance_novelty": 0.42,
  "rarity": 0.51,
  "rediscovery_similarity": 0.07,
  "replication": 0.90,
  "yield": 0.72,
  "latent_yield_score": 0.49,
  "emergent": true
}
```

## Design principle

LYNX should not reward random deviation.

A stronger novelty claim requires:
- separation from known behavior,
- low historical similarity,
- reproducibility,
- meaningful yield.

## Integration

ELEPHANT can maintain the historical novelty archive.

SALMON can trace the origin of a new behavior.

CHAMELEON can test whether novelty persists across contexts.

MAGPIE can audit evidence supporting the novelty claim.
