from lynx import LynxEvaluator, LynxConfig

reference = [
    [0.0,0.0],
    [0.1,0.0],
    [0.0,0.1],
    [0.1,0.1],
    [0.2,0.1]
]

rare = [
    [0.8,0.8]
]

ev = LynxEvaluator(reference, rare, LynxConfig(novelty_threshold=0.25, replication_threshold=0.6))

cases = {
    "ordinary":[0.08,0.05],
    "rediscovered_rare":[0.82,0.79],
    "new_region":[0.55,0.95]
}

if __name__ == "__main__":
    for name,b in cases.items():
        print(name, ev.evaluate(b, replication=0.9, yield_score=0.8))
