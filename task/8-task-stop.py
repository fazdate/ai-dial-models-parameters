from task.app.main import run

#  User massage: Explain the key components of a Large Language Model architecture

run(
    deployment_name='gpt-4o',
    print_only_content=False,
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
)

# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).
# The `finish_reason` will be set as `stop`. So, the users won't know what is the real reason why LLM has stopped generation.