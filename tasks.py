from crewai import Task
from tools import tool  # Ensure `classtool` is also imported if needed
from agent import news_researcher, news_writer

# Research Task
research_task = Task(
    description=(
        "Identify the next big trend in {topic}. "
        "Focus on identifying pros and cons and the overall narratives. "
        "Your final report should clearly articulate the key points, "
        "its market opportunities, and potential risks."
    ),
    expected_output="A comprehensive 3-paragraph long report on the latest AI trends.",
    tools=[tool],  # Ensure the tool is correctly defined
    agent=news_researcher,
)

# Writing Task
write_task = Task(
    description=(
        "Compose an insightful article on {topic}. "
        "Focus on the latest trends and how they are impacting the industry. "
        "This article should be easy to understand, engaging, and positive."
    ),
    expected_output="A 4-paragraph article on {topic} advancements formatted as Markdown.",
    tools=[tool],  # Use `tool` instead of `classtool` (unless `classtool` exists)
    agent=news_writer,
    output_file="new-blog-post.md"  # Example of output customization
)
