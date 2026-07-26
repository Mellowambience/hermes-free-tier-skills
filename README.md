# Hermes Free-Tier Skills Library

A small, shareable collection of **Hermes Agent skills** built for the free /
zero-budget OpenRouter tier. Each skill is a single portable Python script
(stdlib only — no pip) plus a `SKILL.md`, ready to drop into
`~/.hermes/skills/<category>/<name>/` or submit to the Hermes `optional-skills/`
tree.

## Why this exists

OpenRouter's free models are great but rate-limited: a **daily** free-model
request cap means naive "call all free models" burns the whole day's quota on
one task. These skills are **quota-aware** — they probe the cap, run a small
strength-ordered set, and queue + report the exact UTC reset instead of failing.

## Skills

| Skill | What it does | Key command |
|-------|--------------|-------------|
| `moa-free` | Mixture-of-Agents: fan a prompt across several free chat models, synthesize into one answer. | `python moa_all.py "prompt"` |
| `model-advisor` | Task-aware router: classify prompt (code/creative/research/long/chat) and send to the best free model for that job. | `python model_advisor.py "prompt"` |

Both read `OPENROUTER_API_KEY` from the Hermes `.env` automatically and are
cross-platform (Windows / Linux / macOS).

## Install (local)

```bash
# copy into your Hermes skills dir
cp -r skills/moa-free   ~/.hermes/skills/mlops/moa-free
cp -r skills/model-advisor ~/.hermes/skills/mlops/model-advisor
```

Or just run the scripts directly — they're standalone.

## Usage

```bash
# MOA
python skills/moa-free/moa_all.py --list
python skills/moa-free/moa_all.py "your prompt"
python skills/moa-free/moa_all.py --run-queue   # replay prompts queued during cap

# Advisor
python skills/model-advisor/model_advisor.py --show-routes
python skills/model-advisor/model_advisor.py "write a python yaml parser"
python skills/model-advisor/model_advisor.py --llm-classify "prompt"
```

## Contributing

Add a folder under `skills/<category>/<name>/` with a `SKILL.md` (Hermes format)
and any script files. Keep scripts stdlib-only and quota-aware where they touch
rate-limited APIs. Update `library.json` and this README.

## License

MIT — see LICENSE.
