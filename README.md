# I Ching Consultation

This is a simple chatbot that provides I Ching consultations and insights. You can choose to use Anthropic, OpenAI or your own locally deployed large langauge models. 

## Usage

The chatbot prompts the user to enter an inquiry. It then constructs a prompt for the LLM your have chosen, requesting an I Ching interpretation and insights related to the user's inquiry. 

The response from the LLM is printed to the console and also saved to a timestamped text file for future retrival.

## Requirements

- Anthropic API key (set as environment variable `ANTHROPIC_API_KEY`) OR
- OpenAI API key (set as environment variable `OPENAI_API_KEY`) OR
- Your locally deployed LLM on Text Generation WebUI with the OpenAI API plugin enabled
- `anthropic` and `openai` Python packages

## Example

Run the script:
```
python3 webui.py
```
A WebUI will be launched on localhost:7860 by default. So access it via your browser.
Then, enter an inquiry when prompted:

```
I want to change careers

```
```
Here is an I Ching interpretation for your situation of wanting to change careers:

The hexagram that relates to your situation is Hexagram 53 - Gradual Progress:

Hexagram 53 represents gradual development and steady progress. Though you seek major change, it must come about slowly, through small steps. Do not try to rush or force matters. Trust the process of natural growth.

To change careers, make incremental progress towards your goal. Research fields that interest you. Seek education and training to build relevant skills. Network and make connections in your desired industry. Look for opportunities to gain experience through volunteering or freelance work. Save money to cover the transition costs.

Be patient and keep moving forward one step at a time. With perseverance and hard work, you will build up to the big change you envision. The seeds you plant now will grow into a flourishing new career. Trust the timing of the universe. Your efforts will bear fruit at the right moment.

The key is to balance ambition with realism. Moderate your pace and expectations. Adapt as needed but don't lose sight of your aims. Progress may seem slow but each step brings you closer to your goal. With commitment and patience, you will in time attain the change you seek.

```
The response will be saved to a file like `20230309_151129_response.txt` in the `outputs` directory.

## License

This project is under MIT License.
