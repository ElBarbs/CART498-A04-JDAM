# CART498 (GenAI)

## Assignment 4 - JDAM (Jungian Dream Analysis Machine)

### Jungian Concepts in Prompt Engineering

For interpretation, I used GPT-4o and instructed it to act as a “dream-interpreting machine” that follows Jungian symbolism. To structure the response, I had it list the symbols and their meanings in bullet points, showing how they connected to the user’s input.

For image generation, I used DALL-E 3, combining the user’s input with keywords like “dream-like,” “Jungian,” “symbolic,” and “surreal” to shape the visual output. I also set the style to “vivid”, which “causes the model to lean towards generating hyper-real and dramatic images.”

### User Guide

1. **Input**: Type a description of your dream. Include as many details as possible, such as the emotions you felt, the people you encountered, and the places you visited.
2. **Output**: The machine will interpret your dream using Jungian symbolism and generate an image based on the dream’s themes.

### Reflection

At first, GPT-4o’s output wasn’t as consistent as I expected. Since I asked it to generate HTML tags for structuring responses, it sometimes misformatted the text, like making sections bold when they shouldn’t be. Using the “assistant” role helped a lot—I selected a well-formatted response and used it as a reference to maintain consistency across all outputs. I also realized during testing that the model would respond to random questions, like “Give me CSS tips,” so I had to adjust the prompt to focus solely on dream-related queries.

DALL-E 3’s images were fascinating, but they often felt disconnected from the dream’s content. I realized that the model might not fully understand the dream’s context, leading to more abstract or surreal visuals. In the future, I plan to use the dream interpretation results to guide the image generation, but this was challenging in this iteration due to the use of HTML tags in the text. It would also be a useful optimization to avoid generating an image if the user’s input isn’t dream-related, like the example I mentioned earlier.