from task.app.main import run

#  User massage: What is token when we are working with LLM?

run(
    deployment_name='gpt-4o',
    max_tokens=10,
    print_only_content=True,
)

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.