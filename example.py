from lynx import LynxEvaluator

reference = [
    [0.0,0.0,0.0],
    [0.1,0.0,0.1],
    [0.0,0.1,0.0],
]

evaluator = LynxEvaluator(reference)

candidate = [0.7,0.8,0.6]

print(evaluator.evaluate(
    candidate,
    replication=0.85,
    yield_score=0.75
))
