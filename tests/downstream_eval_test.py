import torch
from olmo.config import TrainConfig
from scripts.train import build_downstream_evaluator


def test_piqa():
    cfg = TrainConfig.load('test_fixtures/train_tiny_with_evaluator.yaml')
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    evaluator = build_downstream_evaluator(cfg.evaluators[1], train_cfg=cfg, tokenizer=tokenizer, is_unit_test=True)

    # mock logits as a random torch.tensor of size [224, 50304]
    logits = torch.rand(224, 50304)
    epoch, first_batch = next(evaluator.eval_batches)
    evaluator.reset_metrics()
    evaluator.update_metrics(first_batch, logits.sum(), logits)

    import ipdb; ipdb.set_trace()


if __name__ == "__main__":
    test_piqa()
