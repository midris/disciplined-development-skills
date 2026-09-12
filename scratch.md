> **Abandoned testing process — historical reference only (2026-09-11).**
> Testing-framework instructions, approvals and pending work below are no longer current. Follow the [new framework spec](plans/specs/2026-09-11-model-driven-skill-testing-framework.md) and [new testing plan](plans/2026-09-11-model-driven-skill-testing.md).
> The original text is preserved as history; this notice does not retire existing runner tooling or core skills.

Prompts:

- My dd skills have grown haphazardly over time. They are mostly agent written with some specific pieces being hand tuned. This was my first attempt at coding agents and the skillset grow organically over time. My overall goal is to rewrite the skills to be cleaner, lighter, more effective, and to use targeted tools whenever necessary. The combo of tools and hooks should follow the idea of "dumb tools for smart agents" and provide deterministic mechacnical tools whenver a model need to do something specific, mechanical, repeatable and deterministic. I attempted a full rewrite but the attempts were a little haphazard and really blew up around the fact that there was no simple or repeatable testing toolset or methodology. The first step was to build the simple testing tool. That is in place now. the next steps was to actually exercise to the tool set and set the baselines.

- I am using skill writing superpower to draft my skills. that requires RED/GREEN testing for any skills. even if I wasn't using that skill it just makes sense, having a fixed way to measure skill effectiveness is the cleanest way to go about editing skills.