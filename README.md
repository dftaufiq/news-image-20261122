# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/dftaufiq/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/dftaufiq/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image summing up the world's news of Sunday 22 November 2026: a newspaper front page with 44 stories across 7 regions — 1 illustrated lead story, 4 illustrated features, a numbered dotted world map with 12 pinned stories, and 32 more briefs — every one of them dated to Sunday 22 November 2026.

Round 2 (late morning WIB, 22 Nov): refreshed with the Bahrain industrial strike, the COP31 3am draft and closing plenary, the Peru quake aftermath and a new Africa section; the stale Shenzhen summit feature was replaced and weak filler briefs swapped for real Sunday news.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory. The image itself is drawn from scratch by `generate_image.py` (build-time only, needs Pillow) — no photographs or copied artwork: every panel, illustration and the dotted world map are drawn in code. Every story on the page was checked against reporting of 22 November 2026, with sources named beside each story:

- Antalya: COP31 nears a deal — the third draft lands at 3am Sunday, a closing plenary is set for 9am; the text still names no fossil fuels and no $120bn adaptation figure, but recalls the COP28 stocktake in full
- Manama: an Iranian strike sets a Bahrain industrial plant ablaze; air defences intercept attacks across the Gulf
- Strait of Hormuz: the IRGC claims strikes on two US Patriot radars; Araghchi says reopening the Strait "would not be difficult"
- Kyiv: Russia's 400-drone, 110-missile barrage, one of the war's largest; a missile and a drone come down in Poland; Zelenskyy says NATO is Ukraine's clearest guarantee
- Gulf of Finland: drones set a Russian cargo ship bound for Kaliningrad ablaze; the crew evacuates; Finland tightens security and probes a suspected helicopter incursion
- Lima: Peru quake aftermath — Sunday's revised inventory counts 152 homes uninhabitable
- Tallinn: Estonia to shut all five road crossings with Russia on 1 Dec after an alleged sabotage attempt
- Brasília: jailed ex-president Bolsonaro in intensive care with an acute bowel obstruction
- Sinaloa: FBI Top-10 fugitive "El Chapo Isidro" captured in a raid backed by US intelligence; cartel violence erupts, 11 killed
- Washington: US airlines warned of a possible al-Qaeda-linked terror threat before Thanksgiving; FBI probes a second hack of its crime database
- New Delhi: Modi opens the Nitish Setu bridge; Nepal's PM Shah visits for flood aid talks
- Plus a M4.1 quake in Myanmar, the Japan–India live-fire deal, TikTok's deepfake tool, Voyager-1 one light-day out, the first measles child death in Virginia since 1978, Lisbon inflation protests, UN autonomous-weapons talks, Norway's oil-licence ruling, the DRC Ebola toll, EU–Indonesia trade deals, Lagarde's resignation — and the ATP Finals semi-finals in Turin, Harden passing Kobe, Wall Street's worst week since 2020 — and 32 briefs

The DATE CHECK box at the foot of the page names the big stories deliberately left out because they happened on earlier days (Iran's strikes on the US base in Kuwait and Bahrain of Wed 18 Nov, the US strike on Qeshm Island of Tue 17 Nov, the ADNOC vessel attack, the Shenzhen APEC summit of Sat 21 Nov, Cyclone Akvan's landfall) — so the page shows Sunday's news and nothing else. The Peru quake IS included — Sunday's revised toll.

To redraw the image from its source data: `python3 generate_image.py`

---

<sub>Entered on [make.fun](https://make.fun/?ref=bqc0tvks&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
