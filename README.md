![LangChain Academy](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/66e9eba1020525eea7873f96_LCA-big-green%20(2).svg)

## Introduction

Welcome to LangChain Academy, Introduction to LangGraph! 
This is a growing set of modules focused on foundational concepts within the LangChain ecosystem. 
Module 0 is basic setup and Modules 1 - 5 focus on building in LangGraph, progressively adding more advanced themes.  Module 6 addresses deploying your agents. 
In each module folder, you'll see a set of notebooks. A link to the LangChain Academy lesson is at the top of each notebook to guide you through the topic. Each module also has a `studio` subdirectory, with a set of relevant graphs that we will explore using the LangGraph API and Studio.

## Setup

### Python version

Make sure you're using Python version 3.11, 3.12, or 3.13.
```
python3 --version
```

### Clone repo
```
git clone https://github.com/langchain-ai/langchain-academy.git
$ cd langchain-academy
```
Or, if you prefer, you can download a zip file [here](https://github.com/langchain-ai/langchain-academy/archive/refs/heads/main.zip).

### Create an environment and install dependencies
#### Mac/Linux/WSL
```
$ python3 -m venv lc-academy-env
$ source lc-academy-env/bin/activate
$ pip install -r requirements.txt
```
#### Windows Powershell
```
PS> python3 -m venv lc-academy-env
PS> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
PS> .\lc-academy-env\Scripts\Activate.ps1
PS> pip install -r requirements.txt
```

### Running notebooks
If you don't have Jupyter set up, follow the installation instructions [here](https://jupyter.org/install).
```
$ jupyter notebook
```

### Setting up env variables
Briefly going over how to set up environment variables. 
#### Mac/Linux/WSL
```
$ export API_ENV_VAR="your-api-key-here"
```
#### Windows Powershell
```
PS> $env:API_ENV_VAR = "your-api-key-here"
```

### Set OpenAI API key
* If you don't have an OpenAI API key, you can sign up [here](https://openai.com/index/openai-api/).
*  Set `OPENAI_API_KEY` in your environment 

### OpenRouter API (alternative to OpenAI direct)

The notebooks also support [OpenRouter](https://openrouter.ai/) as an alternative provider, using the `openai/gpt-oss-120b` model via `ChatOpenAI` with a custom `base_url`. OpenRouter routes requests across multiple upstream inference providers.

* Sign up at [openrouter.ai](https://openrouter.ai/) and obtain an API key.
* Set `OPENROUTER_API_KEY` in your environment.
* Adding $10+ in credits unlocks 1,000 free-tier requests/day (vs 50 without credits).

#### Available providers for `openai/gpt-oss-120b`

The following table of model providers is ordered by a rough priority ranking:

1. **Top group (rows 1-7)** - Providers with known output speed, sorted descending — Cerebras (3,044), Together.ai (920), Fireworks (789), SambaNova (743), Lightning AI (734), Baseten (650), Clarifai (544)
2. **Middle group (rows 8-11)** - Providers with TTFT or pricing data but no output speed, sorted by TTFT then price ascending — Groq (0.14s), DeepInfra (0.21s, $0.08), Novita ($0.10), Google Vertex ($0.16)
3. **Bottom group (rows 12-20)** - Remaining providers with no benchmark data, loosely grouped by category — Enterprise (Amazon, Azure, Databricks, Snowflake), Budget (Nebius, Hyperbolic, Parasail), Niche (Cloudflare, Scaleway, Eigen AI)

| Provider | Output speed (tok/s) | TTFT (s) | Price ($/M tokens) | Notable for |
|---|---|---|---|---|
| Cerebras | ~3,044 | — | $0.25 in / $0.69 out | Fastest inference (custom silicon) |
| Together.ai | ~920 | — | — | High throughput, popular |
| Fireworks | ~789 | — | — | High throughput, low latency |
| SambaNova | ~743 | — | — | High throughput (custom silicon) |
| Lightning AI | ~734 | 0.18 | $0.17 blended | Fast + low latency + cheap |
| Baseten | ~650 | 0.09 | — | Lowest latency (TTFT) |
| Clarifai | ~544 | 0.23 | $0.16 blended | Fast on GPU, cost-effective |
| Groq | — | 0.14 | — | Low latency (custom silicon) |
| DeepInfra | — | 0.21 | $0.08 blended | Cheapest |
| Novita | — | — | $0.10 blended | Budget |
| Google Vertex | — | — | $0.16 blended | Enterprise |
| Amazon Bedrock | — | — | — | Enterprise |
| Microsoft Azure | — | — | — | Enterprise |
| Databricks | — | — | — | Enterprise |
| Snowflake | — | — | — | Enterprise |
| Nebius | — | — | — | Budget-friendly |
| Hyperbolic | — | — | — | Budget |
| Parasail | — | — | — | Budget |
| Cloudflare | — | — | — | Edge inference |
| Scaleway | — | — | — | EU-hosted |
| Eigen AI | — | — | — | Emerging |

Source: [Artificial Analysis gpt-oss-120b provider benchmarks](https://artificialanalysis.ai/models/gpt-oss-120b/providers) (median P50, trailing 72h).

Use `extra_body={"provider": {"sort": "latency", "allow_fallbacks": True}}` in `ChatOpenAI` to prioritize the lowest-latency provider, or pin to a specific one with `"order": ["Cerebras"]`. See the [OpenRouter provider routing docs](https://openrouter.ai/docs/guides/routing/provider-selection) for details.

### Sign up and Set LangSmith API
* Sign up for LangSmith [here](https://docs.langchain.com/langsmith/create-account-api-key#create-an-account-and-api-key), find out more about LangSmith and how to use it within your workflow [here](https://www.langchain.com/langsmith). 
*  Set `LANGSMITH_API_KEY`, `LANGSMITH_TRACING_V2="true"` `LANGSMITH_PROJECT="langchain-academy"`in your environment 
*  If you are on the EU instance also set `LANGSMITH_ENDPOINT`="https://eu.api.smith.langchain.com" as well.

### Set up Tavily API for web search

* Tavily Search API is a search engine optimized for LLMs and RAG, aimed at efficient, 
quick, and persistent search results. 
* You can sign up for an API key [here](https://tavily.com/). 
It's easy to sign up and offers a very generous free tier. Some lessons (in Module 4) will use Tavily. 

* Set `TAVILY_API_KEY` in your environment.

### Set up Studio

* Studio is a custom IDE for viewing and testing agents.
* Studio can be run locally and opened in your browser on Mac, Windows, and Linux.
* See documentation [here](https://docs.langchain.com/langsmith/studio#local-development-server) on the local Studio development server. 
* Graphs for LangGraph Studio are in the `module-x/studio/` folders for module 1-5.
* To start the local development server, make sure your virtual environment is active and run the following command in your terminal in the `/studio` directory in each module:

```
langgraph dev
```

You should see the following output:
```
- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs
```

Open your browser and navigate to the Studio UI: `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`.

* To use Studio, you will need to create a .env file with the relevant API keys
* Run this from the command line to create these files for module 1 to 5, as an example:
```
for i in {1..5}; do
  cp module-$i/studio/.env.example module-$i/studio/.env
  echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\"" > module-$i/studio/.env
done
echo "TAVILY_API_KEY=\"$TAVILY_API_KEY\"" >> module-4/studio/.env
```
