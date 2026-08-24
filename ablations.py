from lynx import LynxEvaluator, LynxConfig
from benchmark import reference, rare, cases

if __name__ == "__main__":
    full = LynxEvaluator(reference, rare, LynxConfig(novelty_threshold=0.25))
    no_archive = LynxEvaluator(reference, [], LynxConfig(novelty_threshold=0.25))

    b = cases["rediscovered_rare"]
    print("full:", full.evaluate(b, replication=0.9, yield_score=0.8))
    print("no rare archive:", no_archive.evaluate(b, replication=0.9, yield_score=0.8))
