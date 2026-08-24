# LYNX Theory

## 1. Problem

Novelty is easy to overclaim.

A behavior may appear new because:
- the baseline is incomplete,
- noise is high,
- the representation changed,
- the system recombined known behaviors,
- a rare but previously known mode reappeared.

LYNX treats novelty as a comparative, probabilistic property.

## 2. Behavioral representation

Represent an observation as feature vector:

`b in R^d`

Let known reference behavior set be:

`K = {k_1, ..., k_n}`

## 3. Distance novelty

A basic novelty term:

`D(b) = min_k dist(b,k)`

Higher distance suggests less similarity to known behavior.

## 4. Density rarity

Novelty should also depend on local density.

If estimated density is `p(b)`:

`R(b) = -log(p(b)+eps)`

Rare behavior receives a higher score.

## 5. Rediscovery penalty

If behavior resembles archived rare behavior:

`Q(b) = max similarity to historical rare cases`

Then candidate adjusted novelty:

`N(b) = alpha*D + beta*R - gamma*Q`

## 6. Replication stability

A one-off anomaly is weak evidence of emergence.

For repeated observations of the same candidate pattern:

`S = successful_reproductions / trials`

Novelty confidence should increase with stability.

## 7. Latent yield

LYNX distinguishes novelty from usefulness.

Define yield:

`Y = utility_or_information_gain(b)`

A candidate combined score:

`L = N * S * Y`

This prevents useless random deviation from being treated as high-value emergence.

## 8. Emergence condition

Candidate condition:

`N > theta_N`
and
`S > theta_S`

Optionally require:
`Y > theta_Y`

## 9. EFMW interpretation

The EFMW-inspired element is recursive comparison against:
- prior state space,
- historical rare cases,
- replicated behavior,
- downstream informational yield.

## 10. Falsifiable prediction

LYNX should add value when:
- novelty is sparse,
- behavior space is high-dimensional,
- rare known modes exist,
- replication matters.

If standard outlier or density detection performs equivalently, LYNX's added structure is unnecessary.
