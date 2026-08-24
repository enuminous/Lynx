from dataclasses import dataclass
from typing import List, Optional
import math
from statistics import mean

@dataclass
class LynxConfig:
    alpha: float = 0.5
    beta: float = 0.5
    gamma: float = 0.5
    novelty_threshold: float = 0.4
    replication_threshold: float = 0.6

def euclidean(a, b):
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))

class LynxEvaluator:
    def __init__(self, reference: List[List[float]], rare_archive: Optional[List[List[float]]] = None, config: Optional[LynxConfig] = None):
        self.reference = reference
        self.rare_archive = rare_archive or []
        self.config = config or LynxConfig()

    def nearest_distance(self, b):
        if not self.reference:
            return 1.0
        return min(euclidean(b,k) for k in self.reference)

    def rarity(self, b, k=3):
        if not self.reference:
            return 1.0
        ds = sorted(euclidean(b,x) for x in self.reference)
        k = min(k, len(ds))
        return mean(ds[:k]) if k else 0.0

    def rediscovery_similarity(self, b):
        if not self.rare_archive:
            return 0.0
        d = min(euclidean(b,x) for x in self.rare_archive)
        return 1.0/(1.0+d)

    def evaluate(self, b, replication=1.0, yield_score=1.0):
        D = self.nearest_distance(b)
        R = self.rarity(b)
        Q = self.rediscovery_similarity(b)
        N = max(0.0, self.config.alpha*D + self.config.beta*R - self.config.gamma*Q)
        L = N * max(0.0,min(1.0,replication)) * max(0.0,min(1.0,yield_score))
        emergent = (
            N >= self.config.novelty_threshold and
            replication >= self.config.replication_threshold
        )
        return {
            "distance_novelty": D,
            "rarity": R,
            "rediscovery_similarity": Q,
            "novelty_score": N,
            "replication": replication,
            "yield": yield_score,
            "latent_yield_score": L,
            "emergent": emergent
        }
