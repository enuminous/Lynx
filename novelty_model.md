# Novelty Model

## Candidate schema

```json
{
  "features": [0.3, 0.8, 0.1],
  "utility": 0.7,
  "replication_rate": 0.9
}
```

## Reference archive

The archive should contain:
- common behaviors
- rare known behaviors
- prior anomalies
- previously confirmed novel modes

## Distance term

`D = nearest-neighbor distance`

## Rarity term

Approximate rarity can be estimated from k-nearest-neighbor distance:

`R = mean distance to k nearest neighbors`

## Rediscovery term

Similarity to rare known modes reduces the claim of novelty.

## Stability term

Repeated independent reproduction increases confidence.

## Yield term

Yield can represent:
- predictive gain
- compression gain
- task benefit
- information gain
- new capability value

## Composite

`Score = novelty * replication * yield`
