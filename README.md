# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/dftaufiq/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/dftaufiq/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image summing up the world's news of Sunday 22 November 2026: a newspaper front page with 42 stories across 7 regions — 1 illustrated lead story, 4 illustrated features, a numbered dotted world map with 12 pinned stories, and 30 more briefs — every one of them dated to Sunday 22 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory. The image itself is drawn from scratch by `generate_image.py` (build-time only, needs Pillow) — no photographs or copied artwork: every panel, illustration and the dotted world map are drawn in code. Every story on the page was checked against reporting of 22 November 2026, with sources named beside each story:

- Antalya: COP31 slips into overtime with no deal — the draft drops every mention of fossil fuels and the $120bn adaptation target, and admits the 1.5°C goal has been missed
- Strait of Hormuz: Iran says it shot down two US drones, an MQ-9 over the Strait and an MQ-1 over Qeshm Island; tankers hit by projectiles near Oman
- Kyiv: Russia's 400-drone, 110-missile barrage, one of the war's largest; a missile and a drone come down in Poland, PM Tusk flags a "provocation"
- Shenzhen: Trump meets Xi and Putin at APEC; Trump says an Iran deal could last 20 years
- Gulf of Finland: drones set a Russian cargo ship bound for Kaliningrad ablaze; the crew evacuates
- Tallinn: Estonia to shut all five road crossings with Russia on 1 Dec after an alleged sabotage attempt
- Brasília: jailed ex-president Bolsonaro in intensive care with an acute bowel obstruction
- Sinaloa: FBI Top-10 fugitive "El Chapo Isidro" captured in a raid backed by US intelligence; cartel violence erupts, 11 killed
- Washington: US airlines warned of a possible al-Qaeda-linked terror threat before Thanksgiving; FBI probes a second hack of its crime database
- New Delhi: Modi opens the Nitish Setu bridge; Cyclone Akvan disrupts flights in Ranchi
- Plus the ATP Finals semi-finals in Turin, India v New Zealand in Wellington, Harden passing Kobe, Wall Street's worst week since 2020 — and 30 more briefs

The DATE CHECK box at the foot of the page names the big stories deliberately left out because they happened on earlier days (the Peru M6.9 quake of Fri 20 Nov, Iran's strikes on the US base in Kuwait and Bahrain of Wed 18 Nov, the US strike on Qeshm Island of Tue 17 Nov, the ADNOC vessel attack, Cyclone Akvan's landfall) — so the page shows Sunday's news and nothing else.

To redraw the image from its source data: `python3 generate_image.py`

---

<sub>Entered on [make.fun](https://make.fun/?ref=bqc0tvks&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
