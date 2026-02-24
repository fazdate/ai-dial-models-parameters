from task.app.main import run

#  User massage: Explain the water cycle in simple terms for children

run(
    deployment_name='gpt-4o',
    print_only_content=True,
    frequency_penalty=-2.0
)

# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).
# Copy the results and then check with separate request and ask LLM where is more repetitive blocks in texts.
# For Anthropic and Gemini this parameter will be ignored